#!/usr/bin/env python3
#
# Testing tool for the Gyrating Glyphs problem
#
# Usage:
#
#   python3 testing_tool.py -f inputfile <program invocation>
#
#
# Use the -f parameter to specify the input file, e.g. 1.in.
# The input file should contain two lines:
# - The first line contains the number of operators n
# - The second line contains a single string with n operators '+' or 'x'.
#
#
# You can compile and run your solution as follows.
# - You may have to replace "python3" by just "python".
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
import sys
import traceback


def write(p, line):
    assert p.poll() is None, "Program terminated early"
    print("Write: {}".format(line), flush=True)
    p.stdin.write("{}\n".format(line))
    p.stdin.flush()


def read(p):
    assert p.poll() is None, "Program terminated early"
    line = p.stdout.readline().strip()
    assert line != "", "Read empty line or closed output pipe"
    print("Read: {}".format(line), flush=True)
    return line


parser = argparse.ArgumentParser(description="Testing tool for problem Gyrating Glyphs.")
parser.add_argument("-f", dest="inputfile", metavar="inputfile", default=None, type=argparse.FileType("r"),
                    required=True, help="The input file to use.")
parser.add_argument("program", nargs="+", help="Invocation of your solution")

args = parser.parse_args()

with args.inputfile as f:
    lines = f.readlines()
    n = int(lines[0])
    ops = lines[1].rstrip()
    assert n == len(ops), "Length mismatch in input file"

M = 1000000007


def evalops(ops, vals):
    sm = vals[0]
    for op, val in zip(ops, vals[1:]):
        if op == "+":
            sm += val
        if op == "x":
            sm *= val
        sm %= M
    return sm


with subprocess.Popen(" ".join(args.program), shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE,
                      universal_newlines=True) as p:
    try:
        write(p, "{}".format(n))
        queries = 0
        while True:
            line = read(p).split()
            if line[0] == "?":
                queries += 1
                vals = list(map(int, line[1:]))
                assert len(vals) == n + 1, "Number of values is not n+1"
                for v in vals:
                    assert 0 <= v < M, "Value not in bounds"
                write(p, evalops(ops, vals))
            elif line[0] == "!":
                ops_guess = line[1]
                assert len(ops_guess) == n, "Guess has incorrect length"
                assert ops_guess == ops, "Incorrect guess"
                break
            else:
                assert False, "Line does not start with question or exclamation mark."

        assert p.stdout.readline() == "", "Your submission printed extra data after finding a solution."
        assert p.wait() == 0, "Your submission did not exit cleanly after finishing."

        sys.stdout.write("\nSuccess.\nQueries used: {}\n".format(queries))
    except:
        print()
        traceback.print_exc()
        print()
        try:
            p.wait(timeout=2)
        except subprocess.TimeoutExpired:
            print("Killing your submission after 2 second timeout.")
            p.kill()
    finally:
        sys.stdout.flush()
        sys.stderr.flush()
        sys.stdout.write("Exit code: {}\n".format(p.wait()))
        sys.stdout.flush()