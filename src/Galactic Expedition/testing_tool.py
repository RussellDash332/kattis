#!/usr/bin/env python3
#
# Testing tool for the Galactic Expedition problem
#
# Usage:
#
#   python3 testing_tool.py -f inputfile <program invocation>
#
#
# Use the -f parameter to specify the input file, e.g. 1.in.
# Format of the input file:
# - One line with two integers n and d, the number of points in space and the travel distance with a full fuel tank.
# - n lines with two integers, the x- and y-coordinates of a point in space.
# e.g.:
# 6 20
# 0 0
# 0 5
# 95 100
# -5 0
# -100 0
# 100 100
#
#
# You can compile and run your solution as follows:

# C++:
#   g++ solution.cpp
#   python3 testing_tool.py -f 1.in ./a.out

# Python3
#   python3 testing_tool.py -f 1.in python3 ./solution.py

# Java
#   javac solution.java
#   python3 testing_tool.py -f 1.in java solution

# Kotlin
#   kotlinc solution.kt
#   python3 testing_tool.py -f 1.in kotlin solutionKt


# The tool is provided as-is, and you should feel free to make
# whatever alterations or augmentations you like to it.
#
# The tool attempts to detect and report common errors, but it is not an exhaustive test.
# It is not guaranteed that a program that passes this testing tool will be accepted.


import argparse
import math
import subprocess
import traceback

parser = argparse.ArgumentParser(description="Testing tool for problem Galactic Expedition.")
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

    def write(line: str):
        assert p.poll() is None, "Program terminated early"
        print(f"Write: {line}", flush=True)
        p.stdin.write(f"{line}\n")
        p.stdin.flush()


    def read():
        assert p.poll() is None, "Program terminated early"
        line = p.stdout.readline().strip()
        assert line != "", "Read empty line or closed output pipe"
        print(f"Read: {line}", flush=True)
        return line


    # Parse input
    lines = f.readlines()
    assert len(lines) > 2

    n, d = map(int, lines[0].split()[:2])
    points = [-1, *(tuple(map(int, line.split())) for line in lines[1:])]

    # Link two adjacent points in space together as a wormhole.
    targets = [-1] * (n + 1)
    for i in range(2, n, 2):
        targets[i] = i + 1
        targets[i + 1] = i

    # Simulate interaction
    try:
        write(f"{n} {d}")
        for x, y in points[1:]:
            write(f"{x} {y}")

        pos = points[1]
        refuels_left = n // 2
        fuel_left = d
        while True:
            target = int(read())

            fuel_left -= math.dist(pos, points[target])
            assert fuel_left >= 0, "Used too much fuel."

            if target == 1:
                assert refuels_left > 0, f"Refueling more than n / 2 (= {n // 2}) times"
                refuels_left -= 1
                fuel_left = d
                write("1")
            elif target == n:
                break
            else:
                target = targets[target]
                pos = points[target]
                write(f"{target}")

        assert (
            p.stdout.readline() == ""
        ), "Your submission printed extra data after finding a solution"
        assert p.wait() == 0, "Your submission did not exit cleanly after finishing"

        print(f"\nSuccess.\nNumber of times refueled: {n // 2 - refuels_left} out of {n // 2}\n")

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