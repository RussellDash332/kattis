#!/usr/bin/env python3
#
# Testing tool for the Even Odd Game problem
#
# Usage:
#
#   python3 testing_tool.py -f inputfile <program>
#
#
# Use the -f parameter to specify the input file, e.g. 1.in.
# The format of the input file is the same as that of the first block
# sent by the interactor. See the problem statement for details.
#
# If you have a C++ solution stored in a file called "sol.cpp",
# you must first compile it using "g++ sol.cpp -o sol" and then
# invoke the testing tool with:
#
#   python3 testing_tool.py -f 1.in ./sol
#
# If you have a Python solution that you would run using
# "pypy3 sol.py", you could invoke the testing tool with:
#
#   python3 testing_tool.py -f 1.in pypy3 sol.py
#
# If you have a Java solution that you would run using
# "java MyClass.java", you could invoke the testing tool with:
#
#   python3 testing_tool.py -f 1.in java MyClass.java
#
# If you have a Haskell solution that you would run using
# "runhaskell sol.hs", you could invoke the testing tool with:
#
#   python3 testing_tool.py -f 1.in runhaskell sol.hs
#
# The tool is provided as-is, and you should feel free to make
# whatever alterations or augmentations you like to it.
#
# The tool attempts to detect and report common errors, but it is not guaranteed
# that a program that passes the testing tool will be accepted.

import argparse
import random
import subprocess
import traceback


def write(p, line):
    assert p.poll() is None, "Program terminated early"
    print(f"Write: {line}", flush=True)
    p.stdin.write(f"{line}\n")
    p.stdin.flush()


def read(p):
    assert p.poll() is None, "Program terminated early"
    line = p.stdout.readline().strip()
    assert (
        line != ""
    ), "Read empty line or closed output pipe. Make sure that your program started successfully."
    print(f"Read: {line}", flush=True)
    return line


parser = argparse.ArgumentParser(
    description="Testing tool for the Even Odd Game problem"
)
parser.add_argument(
    "-f",
    dest="inputfile",
    metavar="inputfile",
    default=None,
    type=argparse.FileType("r"),
    required=True,
    help="The input file to use.",
)
parser.add_argument("program", nargs="+", help="Invocation of your solution")

args = parser.parse_args()

with args.inputfile as f:
    n = int(f.readline())
    cards = []
    for _ in range(n):
        op, x = f.readline().split()
        cards.append((op, int(x)))
    value = int(f.readline())

with subprocess.Popen(
    " ".join(args.program),
    shell=True,
    stdout=subprocess.PIPE,
    stdin=subprocess.PIPE,
    universal_newlines=True,
) as p:
    try:
        write(p, f"{n}")
        for op, x in cards:
            write(p, f"{op} {x}")
        write(p, f"{value}")

        who = read(p)
        assert (
            who in ["me", "you"]
        ), f"Expected 'me' or 'you', received {who}."

        want_odd = who == "me"
        if want_odd:
            print("Elected to go first. Final value must be odd.")
        else:
            print("Elected to go second. Final value must be even.")

        while cards:
            if who == "me":
                rr = read(p)
                if rr.startswith('DEBUG'): continue
                op, x = rr.split()
                x = int(x)

                assert (
                    (op, x) in cards
                ), f"Card '{op} {x}' is not (or no longer) in the deck."
            else:
                op, x = random.choice(cards)
                write(p, f"{op} {x}")

            cards.remove((op, x))
            if op == '+':
                value += x
            else:
                value *= x
            print(f"New value: {value}")

            who = "me" if who == "you" else "you"


        assert (
            p.stdout.readline() == ""
        ), "Your submission printed extra data after the end of the game."
        assert p.wait() == 0, "Your submission did not exit cleanly after finishing."

        print(f"The final value is {value}, which is {'odd' if value % 2 else 'even'}.")

        assert (
            value % 2 == want_odd
        ), f"This results in a loss."

        print(f"This results in a win.\n")

    except AssertionError as e:
        print()
        print(f"Error: {e}")
        print()
        try:
            p.wait(timeout=2)
        except subprocess.TimeoutExpired:
            print("Killing your submission after 2 second timeout.")
            p.kill()

    except Exception as e:
        print()
        traceback.print_exc()
        print()
        try:
            p.wait(timeout=2)
        except subprocess.TimeoutExpired:
            print("Killing your submission after 2 second timeout.")
            p.kill()
        raise e

    finally:
        print(f"Exit code: {p.wait()}\n", flush=True)