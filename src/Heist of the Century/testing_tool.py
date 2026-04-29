#!/usr/bin/env python3

"""
Local testing tool for Heist of the Century.

Note: This tool is intended to help with debugging interaction.
It is *not* the same code used to test your solution when it
is submitted.

To run the testing tool, run::

    ./testing_tool.py <input_file> <program> <arguments>

where `program` is the contestant solution and `arguments` are optional.

The following show examples for different languages:

    python3 testing_tool.py sample1.in ./myprogram
    python3 testing_tool.py sample1.in -- java -cp . MyProgram
    python3 testing_tool.py sample1.in python3 myprogram.py

To view the inputs / outputs, pass the --verbose flag before the input file:

    python3 testing_tool.py --verbose sample1.in ./myprogram
"""

import argparse
import subprocess
import sys
from typing import TextIO

class WrongAnswer(RuntimeError):
    """Raised whenever an incorrect answer is received."""
    pass

def vprint(*args, verbose: bool, file: TextIO, **kwargs) -> None:
    """Print to `file`, and also to stdout if `verbose is true."""
    if verbose:
        print('< ', end='')
        print(*args, **kwargs)
        sys.stdout.flush()
    print(*args, file=file, **kwargs)

def vreadline(data: TextIO, verbose: bool) -> str:
    """Read a line from `data`, and also log it to stdout if `verbose` is true."""
    line = data.readline()
    if verbose and line:
        print('>', line.rstrip('\n'))
    return line

def check_done(process: subprocess.Popen) -> None:
    """Check for extra output from program."""
    line = vreadline(process.stdout, True)
    if line != '':
        raise WrongAnswer('Program gave extra output')
    
def parse_int_strict(token: str):
    if not token.isdigit():
        raise WrongAnswer(f"Guess provides non-integers")
    return int(token)

def read_exactly_n_ints(N: int, low: int, high: int, source: TextIO, *, verbose: bool):
    line = vreadline(source, verbose=verbose)
    if not line:
        raise WrongAnswer("End of file received from contestant program")
    tokens = line.strip().split()
    if len(tokens) != N:
        raise WrongAnswer(f"Guess does not contain N numbers")
    result = []
    for token in tokens:
        val = parse_int_strict(token)
        if val < low or val > high:
            raise WrongAnswer(f"Guess is not in range [1,2N]")
        result.append(val)
    return result

def run_judge(input_file: str, process: subprocess.Popen, *, verbose: bool) -> int:
    with open(input_file) as f:
        N_line = f.readline()
        N = int(N_line)
        
        secret_tokens = f.readline().split()
        
        secret = [int(x) for x in secret_tokens]
        
    
    # Send N to contestant
    vprint(N, file=process.stdin, flush=True, verbose=verbose)

    guesses = 0
    # Interactive guessing loop
    while True:
        if guesses == 4*N:
            raise WrongAnswer("Used more than 4N guesses")
        guess = read_exactly_n_ints(N, 1, 2*N, process.stdout, verbose=verbose)
        guesses += 1
        answer = max(abs(s - g) for s, g in zip(secret, guess))
        vprint(answer, file=process.stdin, flush=True, verbose=verbose)
        if answer == 0:
            return guesses

def main() -> int:
    parser = argparse.ArgumentParser(
        usage="%(prog)s [-h] input_file program [args...]"
    )
    parser.add_argument(
        "--verbose", "-v", action="store_true", help="Show interactions"
    )
    parser.add_argument("input_file")
    parser.add_argument("program", nargs=argparse.REMAINDER)
    args = parser.parse_args()

    if not args.program:
        parser.error("Must specify program to run")

    process = subprocess.Popen(
        args.program, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
        encoding='utf-8', errors='surrogateescape'
    )

    try:
        guesses = run_judge(args.input_file, process, verbose=args.verbose)
        check_done(process)
        print(f"OK! Contestant program correctly determined the hidden sequence in {guesses} guesses")
    except WrongAnswer as e:
        print('ERROR: %s' % e)
        return 1
    except BrokenPipeError:
        print('ERROR: error when communicating with program - exited prematurely?')
        return 2
    return 0

if __name__ == '__main__':
    sys.exit(main())