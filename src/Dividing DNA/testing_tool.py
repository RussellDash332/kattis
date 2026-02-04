#!/usr/bin/env python3
#
# Testing tool for the Dividing DNA problem
#
# Usage:
#
#   python3 testing_tool.py -f inputfile <program invocation>
#
#
# Use the -f parameter to specify the input file, e.g. 1.in.
# Format of the input file:
# - One line with two integers:
#   n (the width of the full interval) and k (the number of 'minimal' OK intervals).
# - One line with the answer to the problem for this testcase.
# - k lines, each with two integers 0 <= l < r <= n, indicating that
#   interval [l, r) is OK, while [l+1, r) and [l, r-1) are not OK.
# NOTE: You have to make sure the intervals are indeed minimal, and that the
# corresponding answer is correct.
# e.g.:
# 6 4
# 3
# 0 2
# 1 4
# 3 5
# 5 6
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


parser = argparse.ArgumentParser(description="Testing tool for problem Dividing DNA.")
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

intervals = None
with args.inputfile as f:
    lines = f.readlines()
    assert len(lines) > 0
    n, k = map(int, lines[0].split())
    ans = int(lines[1])
    intervals = [[int(x) for x in line.split()] for line in lines[2:]]

assert intervals is not None

with subprocess.Popen(
    " ".join(args.program),
    shell=True,
    stdout=subprocess.PIPE,
    stdin=subprocess.PIPE,
    universal_newlines=True,
) as p:
    try:
        write(p, f"{n}")

        queries = 0
        while True:
            query = read(p).split()
            op = query[0]
            if op == "?":
                i, j = int(query[1]), int(query[2])
                queries += 1
                present = False
                for (l, r) in intervals:
                    if l <= i and j <= r:
                        present = True
                        break

                write(p, "present" if present else "absent")
            elif op == "!":
                team_ans = int(query[1])
                assert (
                    team_ans == ans
                ), f"Your answer {team_ans} does not match the number of minimal intervals {ans}"
                break
            else:
                assert False, f"Operation {op} is not one of '?' or '!'."

        assert (
            p.stdout.readline() == ""
        ), "Your submission printed extra data after finding a solution."
        assert p.wait() == 0, "Your submission did not exit cleanly after finishing."

        assert (
            queries <= 2 * n
        ), f"Used {queries} queries, which is more than the allowed 2*n = {2*n}"

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