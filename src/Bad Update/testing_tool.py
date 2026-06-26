#!/usr/bin/python3
#
# Testing tool for the Bad Update problem.
#
# Usage:
#
#   python3 testing_tool.py [-f input_file] <program>
#
# If the -f parameter is not specified, a sample with 3 employees with 5 updates each is used,
# the bad update is chosen randomly.
# Otherwise, an input file is needed. The file should contain N on the first
# line, then N lines with the number of updates from each employee. The last
# line after this should contain two integers, the number of the person who
# made the bad update, and the number of the bad update among those that that
# person made.
# For example:
#
# 3
# 5
# 12
# 7
# 2 8
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


parser = argparse.ArgumentParser(description="Testing tool for bad update")
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
n = 3
lens = [5, 5, 5]
bad_person = random.randint(1, 3)
bad_update = random.randint(1, 5)

if args.inputfile is not None:
    # Read the input file
    with args.inputfile as f:
        n = int(f.readline())
        assert 1 <= n <= 100, "N must be a positive integer that is at most 100"
        lens = [None for _ in range(n)]
        for i in range(n):
            lens[i] = int(f.readline())
            assert 1 <= lens[i] <= 100, "Update number must be a positive integer that is at most 100"
        bad_person, bad_update = map(int, f.readline().strip().split())
        assert 1 <= bad_person <= n, f"Person making the bad update must be a value from 1 to {n}, got {bad_person}"
        assert 1 <= bad_update <= lens[bad_person - 1], (
            f"Bad update must be a value from 1 to {lens[bad_person - 1]}, got {bad_update}"
        )
        assert f.readline() == "", "Extra data at end of input file"

with subprocess.Popen(
    " ".join(args.program), shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, universal_newlines=True
) as p:
    try:
        write(p, f"{n}")
        for i in range(n):
            write(p, f"{lens[i]}")
        query_count = 0
        while True:
            query = read(p).strip().split()
            operation = query.pop(0)
            assert operation in "?!", f"Expected operation to be ? or ! but got {operation}"
            is_final_answer = operation == "!"
            if is_final_answer:
                assert len(query) == 2, "Incorrect number of values in final answer"
                person = int(query[0])
                update = int(query[1])
                assert 1 <= person <= n, f"Person guess must be between 1 and {n}, got {person}"
                assert 1 <= update <= lens[person - 1], (
                    f"Update guess must be between 1 and {lens[person - 1]}, got {update}"
                )
                assert bad_person == person, (
                    f"Final answer for person incorrect. Expected {bad_person}, but got {person}"
                )
                assert bad_update == update, (
                    f"Final answer for update incorrect. Expected {bad_update}, but got {update}"
                )
                break
            else:
                assert query_count < sum(lens), "Exceeded max queries"
                query_count += 1
                assert len(query) == n, f"Query is not of length {n}, actual length is {len(query)}"
                query = list(map(int, query))
                has_bad = False
                for j in range(n):
                    assert 0 <= query[j] <= lens[j], f"Query value {query[j]} at index {j} is out of bounds"
                    if j + 1 == bad_person and query[j] >= bad_update:
                        has_bad = True
                write(p, "Villa" if has_bad else "OK")
        assert p.stdout.readline() == "", "Printed extra data after finding answer"
        assert p.wait() == 0, "Did not exit cleanly after finishing"
        sys.stdout.flush()
        sys.stderr.flush()
        sys.stdout.write(f"Solved case correctly in {query_count} queries.\n")
        sys.stdout.flush()
    except Exception:
        write(p, "0")
        p.kill()
        traceback.print_exc()