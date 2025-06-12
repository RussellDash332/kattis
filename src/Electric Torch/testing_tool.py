#!/usr/bin/python3
#
# Testing tool for the Vasaljos problem.
#
# Usage:
#
#   python3 testing_tool.py [-f input_file] <program>
#
# If the -f parameter is not specified, a random sample with n = 10 is used.
# Otherwise, an input file is needed. The file should contain n on the first
# line, then n / 2 space separated indices on the second line giving the locations
# of the good batteries. For example:
#
# 5
# 7 1 4 10 3
#
# You can compile and run your solution as follows.
# - You may have to replace 'python3' by just 'python'.
# - On Windows, you may have to to replace '/' by '\'.

# C++:
#   g++ solution.cpp
#   python3 testing_tool.py ./a.out

# Java
#   javac solution.java
#   python3 testing_tool.py java solution

# Python3
#   python3 testing_tool.py python3 ./solution.py

# The tool is provided as-is, and you should feel free to make
# whatever alterations or augmentations you like to it.
#
# The tool attempts to detect and report common errors, but it
# is not guaranteed that a program that passes the testing tool
# will be accepted.
#

import argparse
import subprocess
import sys
import traceback
import random


def write(p, line):
    assert p.poll() is None, "Program terminated early"
    print("Write: {}".format(line), flush=True)
    p.stdin.write("{}\n".format(line))
    p.stdin.flush()


def read(p):
    assert p.poll() is None, "Program terminated early"
    line = p.stdout.readline().strip()
    assert line != "", "Read empty line or closed output pipe. Make sure that your program started successfully."
    print("Read: %s" % line, flush=True)
    return line


parser = argparse.ArgumentParser(description="Testing tool for vasaljos")
parser.add_argument(
    "-f",
    dest="inputfile",
    metavar="inputfile",
    default=None,
    type=argparse.FileType("r"),
    help="Custom input file (defaults to random)",
)
parser.add_argument("program", nargs="+", help="Your solution")

args = parser.parse_args()
n, k = 10, random.sample(range(1, 21), 10)

if args.inputfile is not None:
    # Read the input file
    with args.inputfile as f:
        n = int(f.readline().strip())
        assert 2 <= n <= 50, "n must be a positive integer from 2 to 100"
        assert n % 2 == 0, "n must be an even integer"
        k = list(map(int, f.readline().strip().split()))
        assert len(set(k)) == len(k), "The battery indices must be unique"
        assert len(k) == n // 2, "Exactly half the batteries must be good"
        for x in k:
            assert 1 <= x <= n, "The battery indices must be between 1 and n, inclusive"
        assert f.readline() == "", "Extra data at end of input file"

with subprocess.Popen(
    " ".join(args.program), shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, universal_newlines=True
) as p:
    try:
        write(p, f"{n}")
        query_count = 0
        while True:
            query = read(p).strip().split()
            query_count += 1
            assert query_count <= 4 * n * n, "Exceeded max guesses"
            assert len(query) == 2, "Guess does not have two values"
            b1, b2 = map(int, query)
            assert 1 <= b1 <= n, "Battery index 1 out of bounds"
            assert 1 <= b2 <= n, "Battery index 2 out of bounds"
            assert b1 != b2, "Battery appears twice in guess"
            if b1 in k and b2 in k:
                write(p, "Ljos!")
                break
            else:
                write(p, "Myrkur!")
        assert p.stdout.readline() == "", "Printed extra data after finding answer"
        assert p.wait() == 0, "Did not exit cleanly after finishing"
        sys.stdout.flush()
        sys.stderr.flush()
        sys.stdout.write(f"Solved case correctly in {query_count} guesses.\n")
        sys.stdout.flush()
    except Exception:
        p.kill()
        traceback.print_exc()