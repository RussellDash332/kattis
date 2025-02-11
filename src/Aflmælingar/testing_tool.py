#!/usr/bin/python3
#
# Testing tool for the Aflmaelingar problem.
#
# Usage:
#
#   python3 testing_tool.py [-f input_file] <program>
#
# If the -f parameter is not specified, a random sample with k = 2 is used. 
# Otherwise, an input file is needed. The file should contain K, q on the first
# line and the base powers on the second line. For example:
#
# 2 300
# 0 0 0 1 1 1 ... 99 99 99
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
import string
import random

def write(p, line):
    assert p.poll() is None, 'Program terminated early'
    print('Write: {}'.format(line), flush=True)
    p.stdin.write('{}\n'.format(line))
    p.stdin.flush()


def read(p):
    assert p.poll() is None, 'Program terminated early'
    line = p.stdout.readline().strip()
    assert line != '', 'Read empty line or closed output pipe. Make sure that your program started successfully.'
    print('Read: %s' % line, flush=True)
    return line


parser = argparse.ArgumentParser(description='Testing tool for aflmaelingar')
parser.add_argument('-f', dest='inputfile', metavar='inputfile', default=None, type=argparse.FileType('r'),
                    help='Custom input file (defaults to random)')
parser.add_argument('program', nargs='+', help='Your solution')

args = parser.parse_args()
k, q, n = 2, 300, 300
base = [random.randint(0, 99) for i in range(n)]

if args.inputfile is not None:
    # Read the input file
    with args.inputfile as f:
        k, q = map(int, f.readline().strip().split())
        base = list(map(int, f.readline().strip().split()))
        assert 2 <= k <= 4, "K must be 2, 3 or 4"
        assert len(base) == n, "n must be 300"
        if k == 2:
            assert q == 300, "If K == 2, q must be 300"
        if k == 3:
            assert q == 200, "If K == 3, q must be 200"
        if k == 4:
            assert q == 150, "If K == 4, q must be 150"
        assert f.readline() == '', 'Extra data at end of input file'

with subprocess.Popen(" ".join(args.program), shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE,
                          universal_newlines=True) as p:
    try:
        write(p, str(k) + " " + str(q))
        for i in range(q):
            guess = list(map(int, read(p).strip().split()))
            assert len(guess) == n, f'Query is not of length {n}, actual length is {len(guess)}'
            
            sm = 0
            for j in range(n):
                assert 0 <= guess[j] <= 100, f'Percentage value {guess[j]} at index {j} is out of bounds'
                sm += guess[j] * base[j]

            sm %= 10 ** k
            write(p, str(sm))
        result = list(map(int, read(p).strip().split()))
        assert len(result) == n, f'Final answer is not of length {n}, actual length was {len(result)}'
        assert result == base, f'Final answer incorrect. Expected:\n{base}\nGot:\n{result}'
        assert p.stdout.readline() == '', 'Printed extra data after finding answer'
        assert p.wait() == 0, 'Did not exit cleanly after finishing'
        sys.stdout.flush()
        sys.stderr.flush()
        sys.stdout.write('Solved case correctly.\n')
        sys.stdout.flush()
    except:
        traceback.print_exc()
        p.kill()