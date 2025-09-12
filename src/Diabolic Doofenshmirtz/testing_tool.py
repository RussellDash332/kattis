#!/usr/bin/env python3

# Run 'python3 testing_tool.py -h' for information on usage.

import argparse
import subprocess
import sys
import traceback
import math

parser = argparse.ArgumentParser(description="""
  Testing tool for the Running Track problem

  You can compile and run your solution as follows.
  - Replace N with the length of one lap you want to test.
  - You may have to replace 'python3' by just 'python'.
  - On Windows, you may have to to replace '/' by '\\'.

  C++:
    g++ solution.cpp
    python3 testing_tool.py -n N ./a.out

  Java:
    javac solution.java
    python3 testing_tool.py -n N java solution

  Python 3:
    python3 testing_tool.py -n N python3 ./solution.py


  The tool is provided as-is, and you should feel free to make
  whatever alterations or augmentations you like to it.

  The tool attempts to detect and report common errors, but it is not an
  exhaustive test. It is not guaranteed that a program that passes this testing
  tool will be accepted.""", formatter_class=argparse.RawDescriptionHelpFormatter)

parser.add_argument('-f', dest='inputfile', metavar='inputfile', default=None, type=argparse.FileType('r'),
                    help='custom input file containing the length of one lap (defaults to sample 1)')
parser.add_argument('-n', dest='x', metavar='N', type=int,
                    help='use N as length of one lap; this overwrites the -f flag')
parser.add_argument('-q', action='store_true', dest='quiet', default=False,
                    help='only output the number of queries required')
parser.add_argument('program', nargs='+', help='your solution, as described above')

args = parser.parse_args()

def write(p, line):
    assert p.poll() is None, 'Program terminated early'
    if not args.quiet: print('Write: {}'.format(line), flush=True)
    p.stdin.write('{}\n'.format(line))
    p.stdin.flush()

def read(p):
    assert p.poll() is None, 'Program terminated early'
    tokens = p.stdout.readline().strip().split(' ')
    assert len(tokens) == 2, 'Read invalid line or closed output pipe'
    assert tokens[0] == '!' or tokens[0] == '?', 'Read invalid line or closed output pipe'
    if not args.quiet: print('Read:', tokens[0], tokens[1], flush=True)
    return tokens

if args.x is not None:
    x = args.x
elif args.inputfile is not None:
    # Read the input file
    with args.inputfile as f:
        x = int(f.readline())
else:
    x = 42

last = -1

def evaluate(y):
    assert y > last, 'Tried to use the Timetravellinator :('
    return y % x

with subprocess.Popen(" ".join(args.program), shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE,
                          universal_newlines=True) as p:
    try:
        queries = 1
        while True:
            tokens = read(p)
            y = int(tokens[1])

            if tokens[0] == '!':
                assert queries <= 42, 'Used too many queries'
                assert y == x, 'Wrong solution'
                assert p.stdout.readline() == '', 'Printed extra data after finding solution'
                assert p.wait() == 0, 'Did not exit cleanly after finishing'
                break;
            else:
                assert queries <= 42, 'Used too many queries'

                ans = evaluate(y)
                last = y
                write(p, ans)

            queries += 1
    except:
        traceback.print_exc()
        p.kill()
    finally:
        sys.stdout.flush()
        sys.stderr.flush()
        if args.quiet:
            print(queries)
        else:
            print()
            print('Number of guesses:', queries)
            print('Exit code:', p.wait())