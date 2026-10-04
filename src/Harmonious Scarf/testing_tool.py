#!/usr/bin/env python3
#
# Testing tool for the Harmonious Scarf problem
#
# Usage:
#
#   python3 testing_tool.py -f inputfile <program invocation>
#
#
# Use the -f parameter to specify the input file, e.g. 1.in.
# The input file should contain the following:
# - The first line contains the number of segments of the scarf
# - The second line contains a description of the scarf
# Example:
# 5
# cabab

# You can compile and run your solution as follows:

# Java:
#   javac solution.java
#   python3 testing_tool.py -f 1.in java solution

# Python:
#   python3 testing_tool.py -f 1.in python3 ./solution.py

# C++:
#   g++ solution.cpp
#   python3 testing_tool.py -f 1.in ./a.out

# The tool is provided as-is, and you should feel free to make
# whatever alterations or augmentations you like to it.
#
# The tool attempts to detect and report common errors, but it is not an exhaustive test.
# It is not guaranteed that a program that passes this testing tool will be accepted.


import argparse
import random
import subprocess
import traceback

random.seed(43)

parser = argparse.ArgumentParser(description="Testing tool for problem Harmonious Scarf.")
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

with (
    args.inputfile as f,
    subprocess.Popen(
        " ".join(args.program),
        shell=True,
        stdout=subprocess.PIPE,
        stdin=subprocess.PIPE,
        universal_newlines=True,
    ) as p,
):
    assert p.stdin is not None and p.stdout is not None
    p_in = p.stdin
    p_out = p.stdout

    def write(line):
        assert p.poll() is None, "Program terminated early"
        print(f"Write: {line}", flush=True)
        p_in.write(f"{line}\n")
        p_in.flush()

    def read():
        line = p_out.readline().strip()
        if line == "":
            assert p.poll() is None, "Program terminated early"
        assert line != "", "Read empty line or closed output pipe"
        print(f"Read: {line}", flush=True)
        return line

    # Parse input
    lines = f.readlines()
    n = int(lines[0])
    scarf = lines[1]

    if n >= 1000:
        print("Warning: this tool might run very slow for big inputs")

    # pass input to submission
    write(n)

    # Simulate interaction
    try:
        queries = 0
        while True:
            query_type, *query = read().split()
            if query_type == "?":
                queries += 1
                assert len(query) == 2, "Invalid formatted query"
                l, r = map(int, query)
                assert 1 <= l <= r <= n, "Invalid query interval"
                segment = scarf[l - 1 : r]
                write("1" if segment == segment[::-1] else "0")
            elif query_type == "!":
                assert len(query) == 1, "Invalid formatted query"
                got = int(query[0])
                expected = 0
                for r in range(n + 1):
                    for l in range(r):
                        segment = scarf[l:r]
                        if segment == segment[::-1]:
                            expected = max(expected, len(segment))
                assert got == expected, "Wrong answer!"
                break
            else:
                assert False, "Invalid formatted query"
        print()
        if queries > 2 * n:
            assert False, f"Your submission used too many queries: {queries} > {2 * n}"
        print("Found longest harmonious scarf!")
        print(f"Queries used: {queries}", flush=True)
        extra = p_out.readline()
        assert extra == "", (
            f"Your submission printed extra data after finding a solution: '{extra[:100].strip()}{'...' if len(extra) > 100 else ''}'"
        )
        print(f"Exit code: {p.wait()}", flush=True)
        assert p.wait() == 0, "Your submission did not exit cleanly after finishing"

    except AssertionError as e:
        print()
        print(f"Error: {e}")
        print()
        print("Killing your submission.", flush=True)
        p.kill()
        exit(1)

    except Exception:
        print()
        print("Unexpected error:")
        traceback.print_exc()
        print()
        print("Killing your submission.", flush=True)
        p.kill()
        exit(1)