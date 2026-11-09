#!/usr/bin/env python3

"""
Local testing tool for 2SAT Queries.

This tool helps with debugging interaction. It checks answers, the query
budget, extra output and your program's exit status, but does not enforce the
contest's time or memory limits. A program that does not flush its output or
stops responding may hang the tool; press Ctrl+C to interrupt it.

Run it with a judge-input file followed by your program and its arguments:

    python3 testing_tool.py 1.in ./myprogram
    python3 testing_tool.py 1.in java -cp . MyProgram
    python3 testing_tool.py 1.in python3 myprogram.py
    python3 testing_tool.py --quiet 1.in pypy3 myprogram.py

The input file contains the number of games, then n and a string of n
uppercase T/F letters for each game. For example:

    2
    2
    TF
    3
    FTT

The hidden variable assignments are fixed by this file. Your program
receives the number of games and each n, but never the hidden strings. The
10,400-query budget is shared by all games; answers do not count as queries.
Like the judge, the tool replies X to an invalid query or to the query that
exceeds the budget.

By default, '<' marks data sent to your program and '>' marks its output.
Use --quiet before the input filename to hide this transcript. A final verdict
is always printed. Exit status is 0 for acceptance, 1 for a rejected program,
and 2 for a command-line, input-file, or program-launch error.
"""

import argparse
import subprocess
import sys
from typing import NoReturn, TextIO


QUERY_LIMIT = 10400


class WrongAnswer(RuntimeError):
    """Raised when the program violates the interaction protocol."""


class NonzeroExit(RuntimeError):
    """Raised when the program exits with a nonzero status."""


def vprint(*args, verbose: bool, file: TextIO, **kwargs) -> None:
    """Send a line to the program and optionally log it."""
    if verbose:
        print('< ', end='')
        print(*args, **kwargs)
        sys.stdout.flush()
    print(*args, file=file, **kwargs)


def vreadline(data: TextIO, verbose: bool) -> str:
    """Read a line from the program and optionally log it."""
    line = data.readline()
    if verbose and line:
        print('>', line.rstrip(), flush=True)
    return line


def read_cases(filename: str) -> list[tuple[int, str]]:
    with open(filename) as data:
        tokens = iter(data.read().split())
    t = int(next(tokens))
    cases = []
    for _ in range(t):
        n = int(next(tokens))
        cases.append((n, next(tokens)))
    return cases


def literal(hidden: str, index: int) -> bool:
    return hidden[index - 1] == 'T' if index > 0 else hidden[-index - 1] == 'F'


def reject_query(process: subprocess.Popen, verbose: bool, message: str) -> NoReturn:
    """Reply X to a query, then reject the program."""
    vprint('X', file=process.stdin, flush=True, verbose=verbose)
    raise WrongAnswer(message)


def check_exit(process: subprocess.Popen) -> None:
    """Reject a program that stopped with a nonzero status, as the judge does."""
    status = process.wait()
    if status < 0:
        raise NonzeroExit(f'program was killed by signal {-status}')
    if status:
        raise NonzeroExit(f'program exited with status {status}')


def check_done(process: subprocess.Popen, verbose: bool) -> None:
    """Check for extra output after the last answer."""
    while line := vreadline(process.stdout, verbose):
        if line.strip():
            raise WrongAnswer('extra output after the last answer')


def run_judge(cases: list[tuple[int, str]], process: subprocess.Popen,
              verbose: bool) -> int:
    queries = 0
    vprint(len(cases), file=process.stdin, flush=True, verbose=verbose)
    for game, (n, hidden) in enumerate(cases, 1):
        vprint(n, file=process.stdin, flush=True, verbose=verbose)
        while True:
            line = vreadline(process.stdout, verbose)
            if not line:  # end of output: the program has stopped
                check_exit(process)
                raise WrongAnswer(f'game {game}: program exited prematurely')
            line = line.strip()
            if not line:
                reject_query(process, verbose, f'game {game}: expected a query or answer')
            if line[0] in 'TF':
                if line != hidden:
                    raise WrongAnswer(f'game {game}: incorrect answer')
                break

            try:
                a, b = map(int, line.split())
            except ValueError:
                reject_query(process, verbose, f'game {game}: expected two integer literals')
            if not 1 <= abs(a) <= n or not 1 <= abs(b) <= n:
                reject_query(process, verbose, f'game {game}: literal out of range')
            if abs(a) == abs(b):
                reject_query(process, verbose, f'game {game}: both literals name the same variable')

            queries += 1
            if queries > QUERY_LIMIT:
                reject_query(process, verbose, f'game {game}: more than {QUERY_LIMIT} queries')
            reply = 'T' if literal(hidden, a) or literal(hidden, b) else 'F'
            vprint(reply, file=process.stdin, flush=True, verbose=verbose)
    return queries


def main() -> int:
    parser = argparse.ArgumentParser(
        description='Run a program against a fixed 2SAT Queries input file.',
        usage='%(prog)s [-h] [-q] filename program [args...]')
    parser.add_argument('-q', '--quiet', action='store_true',
                        help='hide the interaction transcript')
    parser.add_argument('filename', help='judge-input file containing the hidden strings')
    parser.add_argument('program', nargs=argparse.REMAINDER,
                        help='program to run, followed by its arguments')
    args = parser.parse_args()
    if not args.program:
        parser.error('must specify a program to run')
    try:
        cases = read_cases(args.filename)
    except (OSError, UnicodeError, ValueError, StopIteration) as error:
        parser.error(f'could not read input file: {error}')
    try:
        process = subprocess.Popen(args.program, stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE,
                                   encoding='utf-8', errors='surrogateescape')
    except OSError as error:
        parser.error(f'could not start program: {error}')

    try:
        try:
            queries = run_judge(cases, process, verbose=not args.quiet)
            check_done(process, verbose=not args.quiet)
        except BrokenPipeError:
            check_exit(process)
            raise WrongAnswer('program exited prematurely')
        check_exit(process)
        print(f'Accepted: {len(cases)} games, {queries}/{QUERY_LIMIT} queries.')
        return 0
    except NonzeroExit as error:
        print(f'Run Time Error: {error}', file=sys.stderr)
        return 1
    except WrongAnswer as error:
        print(f'Wrong Answer: {error}', file=sys.stderr)
        return 1
    finally:
        try:
            process.stdin.close()
            process.wait(timeout=1)
        except (OSError, subprocess.TimeoutExpired):
            process.kill()
            process.wait()
        process.stdout.close()


if __name__ == '__main__':
    sys.exit(main())
