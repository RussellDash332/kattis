#!/usr/bin/env python3
#
# Testing tool for the Jagged Skyline problem
#
# Usage:
#
#   python3 testing_tool.py -f inputfile <program invocation>
#
#
# Use the -f parameter to specify the input file, e.g. 1.in.
# Format of the input file:
# - One line with two integers, the width and height of the grid.
# - One line with one integer per column: the height of the building in this column.
# e.g.:
# 6 10
# 3 10 0 2 3 1
#
#
# You can compile and run your solution as follows.
# - You may have to replace 'python3' by just 'python'.
# - On Windows, you may have to to replace '/' by '\'.

# C++:
#   g++ solution.cpp
#   python3 testing_tool.py -f 1.in ./a.out

# Java
#   javac solution.java
#   python3 testing_tool.py -f 1.in java solution

# Python3
#   python3 testing_tool.py -f 1.in python3 ./solution.py


# The tool is provided as-is, and you should feel free to make
# whatever alterations or augmentations you like to it.
#
# The tool attempts to detect and report common errors, but it is not an
# exhaustive test. It is not guaranteed that a program that passes this testing
# tool will be accepted.


import argparse
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
    assert line != "", "Read empty line or closed output pipe"
    print(f"Read: {line}", flush=True)
    return line


parser = argparse.ArgumentParser(description="Testing tool for problem Jagged Skyline.")
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

hs = None
with args.inputfile as f:
    lines = f.readlines()
    assert len(lines) > 0
    width, height = map(int, lines[0].split())
    hs = list(map(int, lines[1].split()))
    assert len(hs) == width

assert hs is not None

with subprocess.Popen(
    " ".join(args.program),
    shell=True,
    stdout=subprocess.PIPE,
    stdin=subprocess.PIPE,
    universal_newlines=True,
) as p:
    try:
        write(p, f"{width} {height}")

        queries = 0
        while True:
            op, x, y = read(p).split()
            x = int(x)
            y = int(y)
            if op == "?":
                queries += 1

                if y <= hs[x - 1]:
                    write(p, "building")
                else:
                    write(p, "sky")
            elif op == "!":
                assert hs[x - 1] == y, f"The building at x={x} does not have height {y}"
                maxy = max(hs)
                assert (
                    y >= maxy
                ), f"You printed y={y}, but there is a building of height {maxy}!"
                assert y == maxy, "This should never fail!"
                break
            else:
                assert False, f"Operation {op} is not one of '?' or '!'."

        assert (
            p.stdout.readline() == ""
        ), "Your submission printed extra data after finding a solution."
        assert p.wait() == 0, "Your submission did not exit cleanly after finishing."

        assert (
            queries <= 11000
        ), f"Used {queries} queries, which is more than the allowed 11000."

        print(f"\nSuccess.\nQueries used: {queries}\n")

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