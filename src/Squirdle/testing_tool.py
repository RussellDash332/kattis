import argparse
import subprocess
import sys
import traceback
import string

# RussellDash332's own testing tool
# python testing_tool.py python squirdle.py
# python testing_tool.py -f <input> python squirdle.py

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


parser = argparse.ArgumentParser(description='Testing tool for pizzastrengur')
parser.add_argument('-f', dest='inputfile', metavar='inputfile', default=None, type=argparse.FileType('r'),
                    help='Custom input file (defaults to sample 1)')
parser.add_argument('program', nargs='+', help='Your solution')

args = parser.parse_args()
guesses = 0

if args.inputfile is not None:
    # Read the input file
    with args.inputfile as f:
        squirdle = f.readline().strip()
        assert len(squirdle) == 5
        assert squirdle.islower(), 'Must be all lowercase'
        assert f.readline() == '', 'Extra data at end of input file'
else:
    squirdle = 'zubat'

with subprocess.Popen(" ".join(args.program), shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE,
                          universal_newlines=True) as p:
    try:
        while True:
            guess = read(p).strip().split()[1]
            assert guess.islower(), 'Must be all lowercase'
            assert len({*guess}) == 5, 'Must be distinct alphabets'
            assert len(guess) == 5, 'Guess is of the incorrect length'
            guesses += 1

            if guess == squirdle:
                write(p, '22222')
                assert p.stdout.readline() == '', 'Printed extra data after finding Squirdle'
                assert p.wait() == 0, 'Did not exit cleanly after finishing'
                break
            else:
                s = []
                for i in range(5):
                    if guess[i] == squirdle[i]: s.append('2')
                    elif guess[i] in squirdle: s.append('1')
                    else: s.append('0')
                write(p, ''.join(s))

            if guesses > 10:
                sys.stdout.write('Program used too many guesses\n')
                p.kill()
                break
    except:
        traceback.print_exc()
    finally:
        sys.stdout.flush()
        sys.stderr.flush()
        sys.stdout.write('Guessed {} times, exit code: {}\n'.format(guesses, p.wait()))
        sys.stdout.flush()