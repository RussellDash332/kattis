#!/usr/bin/python3
#
# Testing tool for the Mögnuð Mylla problem.
#
# Usage:
#
#   python3 testing_tool.py <program>
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
# The tool does not implement an opponent, and simply waits for the
# opponent's moves from standard input.

import argparse
import subprocess
import sys
import traceback


def flip(state):
    for i in range(9):
        state[i] = -state[i]
    for i in range(9, 11):
        state[i], state[i + 2] = state[i + 2], state[i]


def apply_board(state, board, x):
    d_ind_1, d_ind_2 = -1, -1
    for i in range(9):
        if state[i] != board[i]:
            if d_ind_1 == -1:
                d_ind_1 = i
            elif d_ind_2 == -1:
                d_ind_2 = i
            else:
                assert False, "Illegal move, too many changes"
    assert d_ind_1 != -1, "Illegal move, too few changes"
    if d_ind_2 == -1:
        placed = board[d_ind_1]
        if placed != 2 and placed != 1 and x:
            assert False, "Illegal move, must place x or X"
        if placed != -2 and placed != -1 and not x:
            assert False, "Illegal move, must place o or O"
        offs = 8 if x else 10
        assert state[offs + abs(placed)] != 0, "Illegal move, out of letters"
        assert abs(state[d_ind_1]) < abs(placed), "Illegal move, placed over upper case letter"
        state[d_ind_1] = placed
    else:
        if abs(state[d_ind_1]) > abs(state[d_ind_1]):
            d_ind_1, d_ind_2 = d_ind_2, d_ind_1
        assert abs(state[d_ind_1] == 2), "Illegal move, moved non upper case letter"
        wanted = 2 if x else -2
        assert state[d_ind_1] == wanted, "Illegal move, moved opponent's letter"
        assert abs(state[d_ind_2]) == 1, "Illegal move, placed over non lower case letter"
        assert board[d_ind_1] == 0, "Illegal move, did not leave empty space after moving"
        assert board[d_ind_2] == wanted, "Illegal move, did not overwrite letter correctly"
        state[d_ind_2] = state[d_ind_1]
        state[d_ind_1] = 0


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


def output_board(p, state):
    chars = "Oo.xX"
    for i in range(3):
        cur = []
        for j in range(3):
            cur.append(chars[state[3 * i + j] + 2])
        write(p, "".join(cur))


def input_board(p, std):
    lines = []
    for _ in range(3):
        if std:
            lines.append(sys.stdin.readline().strip())
            if lines[-1] == "Sigur!" or lines[-1] == "Tap!":
                return lines[-1]
        else:
            lines.append(read(p).strip())
        assert len(lines[-1]) == 3, "Line does not have 3 non-whitespace characters"
    board = [0 for _ in range(9)]
    for i in range(3):
        for j in range(3):
            k = 3 * i + j
            assert lines[i][j] in "Oo.xX", "Invalid character in input"
            board[k] = "Oo.xX".index(lines[i][j]) - 2
    return board


parser = argparse.ArgumentParser(description="Testing tool for vasaljos")
parser.add_argument("program", nargs="+", help="Your solution")

args = parser.parse_args()

with subprocess.Popen(
    " ".join(args.program), shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, universal_newlines=True
) as p:
    try:
        state = [0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 2, 4, 2]
        while True:
            sys.stdout.write("Asking submission for next move...\n")
            inp = input_board(p, False)
            apply_board(state, inp, True)
            sys.stdout.write("Please input opponent's move (or Sigur!/Tap!):\n")
            inp = input_board(p, True)
            if inp in ["Sigur!", "Tap!"]:
                write(p, inp)
                break
            apply_board(state, inp, False)
            sys.stdout.write("Writing move to submission...\n")
            output_board(p, state)
        assert p.stdout.readline() == "", "Printed extra data after finding answer"
        assert p.wait() == 0, "Did not exit cleanly after finishing"
        sys.stdout.flush()
        sys.stderr.flush()
        sys.stdout.write("Game finished.\n")
        sys.stdout.flush()
    except Exception:
        p.kill()
        traceback.print_exc()