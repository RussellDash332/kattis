#!/usr/bin/env python3
#
# Testing tool for the Going in Circles problem
#
# Usage:
#
#   python3 testing_tool.py [-s sequence] <program>
#
# The sequence must consist of characters '0' and '1' and have length at least 3.
# If no initial sequence is specified, the sample (011) is used.
#
# You can compile and run your solution as follows.
# - You may have to replace 'python3' by just 'python'.
# - On Windows, you may have to replace '/' by '\'.
#
# If you have a Java solution that you would run using
# "java MyClass", you could invoke the testing tool with:
#
#   python3 testing_tool.py java MyClass
#
# If you have a Python solution that you would run using
# "python solution.py", you could invoke the testing tool with:
#
#   python3 testing_tool.py python solution.py
#
# If you have a C++ solution stored in a file called "sol.cpp",
# you must first compile using "g++ sol.cpp -o sol" and then
# invoke the testing tool with:
#
#   python3 testing_tool.py ./sol
#
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


def wrong_answer(p, reason):
    sys.stdout.write('%s\n' % reason)
    p.kill()


parser = argparse.ArgumentParser(description='Testing tool for the Going in Circles problem')
parser.add_argument('-s', dest='sequence', metavar='sequence', default="011")
parser.add_argument('program', nargs='+', help='Invocation of your solution')

args = parser.parse_args()

sequence = list(args.sequence)
for c in sequence:
    assert c in '01', f'Character {c} may not appear in the input sequence.'
n = len(sequence)
assert n >= 3, f'Sequence must have length at least 3'
position = 0

queries = 0
queries_limit = 3 * n + 500

with subprocess.Popen(" ".join(args.program), shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE,
                      universal_newlines=True) as p:
    try:
        write(p, sequence[position])

        while True:
            response = read(p)

            if response.startswith('? '):
                if queries == 50000:
                    wrong_answer(p, 'Program used too many queries, aborting')
                    break
                queries += 1
                action = response[2:]
                if action == 'right':
                    position = (position + 1) % n
                elif action == 'left':
                    position = (position - 1) % n
                elif action == 'flip':
                    sequence[position] = str(1 - int(sequence[position]))
                else:
                    wrong_answer(p, 'Program gave unrecognized action')
            elif response.startswith('! '):
                answer = response[2:]
                assert answer.isnumeric(), 'Expected final guess to be a positive integer'
                answer = int(answer)
                if answer == n:
                    assert queries <= queries_limit, 'Program printed correct solution, but used too many queries'
                    assert p.stdout.readline() == '', 'Printed extra data after finding solution'
                    assert p.wait() == 0, 'Did not exit cleanly after finishing'
                    break
                else:
                    wrong_answer(p, 'Program printed incorrect solution')
                    break
            else:
                wrong_answer(p, 'Program gave invalid response')
                break

            write(p, sequence[position])
    except:
        traceback.print_exc()
    finally:
        sys.stdout.flush()
        sys.stderr.flush()
        sys.stdout.write(f'Used {queries} queries, limit is {queries_limit}.\nProgram exit code: {p.wait()}\n')
        sys.stdout.flush()