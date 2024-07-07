#!/usr/bin/env python3
#
# Testing tool for the Ordla problem
#
# Usage:
#
#   python3 testing_tool.py [-f input_file] <program>
#
# If the -f parameter is not specified, sample 1 is used. Otherwise,
# an input file is needed. The file starts with the number of words
# in the dictionary, followed by the words in the dictionary, one per
# line. For example:
#
# 5
# tolva
# ordla
# stoll
# skjar
# skoli

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
from collections import Counter


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


parser = argparse.ArgumentParser(description='Testing tool for the Ordla problem')
parser.add_argument('-f', dest='inputfile', metavar='inputfile', default=None, type=argparse.FileType('r'),
                    help='Custom input file (defaults to sample 1)')
parser.add_argument('program', nargs='+', help='Your solution')

args = parser.parse_args()
guesses = 0

if args.inputfile is not None:
    # Read the input file
    with args.inputfile as f:
        n = int(f.readline().strip())
        assert 1 <= n <= 500, 'n must be between 1 and 500'
        words = []
        for i in range(n):
            word = f.readline().strip()
            assert len(word) == 5, 'Each word must consist of 5 letters'
            assert set(word) <= set(string.ascii_lowercase), 'Each word must consist of lowercase English letters'
            words.append(word)
        assert f.readline() == '', 'Extra data at end of input file'
else:
    words = [
        'tolva',
        'ordla',
        'stoll',
        'skjar',
        'skoli',
    ]

correct_word = random.choice(words)
print('Hidden word: {}'.format(correct_word), flush=True)

with subprocess.Popen(" ".join(args.program), shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE,
                          universal_newlines=True) as p:
    try:
        write(p, '%d' % len(words))
        for word in words:
            write(p, word)
        while True:
            guess = read(p)
            assert len(guess) == 5, 'Each guess must consist of 5 letters'
            assert set(guess) <= set(string.ascii_lowercase), 'Each guess must consist of lowercase English letters'
            assert guess in words, 'Each guess must be from the dictionary'
            guesses += 1

            rem = Counter(correct_word)
            pattern = ['X']*5
            for i, c in enumerate(guess):
                if correct_word[i] == c:
                    pattern[i] = 'O'
                    rem[c] -= 1
                elif rem[c] >= 1:
                    pattern[i] = '/'
                    rem[c] -= 1

            write(p, ''.join(pattern))

            if guess == correct_word:
                assert p.stdout.readline() == '', 'Printed extra data after finding hidden word'
                assert p.wait() == 0, 'Did not exit cleanly after finishing'
                break
            if guesses == 10000:
                sys.stdout.write('Solution has guessed {} times without finding the hidden word. Is it stuck in a loop?\n'.format(guesses))
                sys.stdout.flush()

    except:
        traceback.print_exc()
    finally:
        sys.stdout.flush()
        sys.stderr.flush()
        sys.stdout.write('Solution found the word in {} guesses, exit code: {}\n'.format(guesses, p.wait()))
        sys.stdout.flush()
