#!/usr/bin/env python3
#
# Testing tool for the "Infection Estimation" problem from NCPC 2020.
#
# Usage:
#
#   python testing_tool.py <infected> <program>
#
# For example, if you have a Java solution that you would run using
# "java MyClass" and want to make a test-run with 4711 infected
# people, you could invoke the testing tool with:
#
#   python testing_tool.py 4711 java MyClass
#
#
# Note that this tool is only provided as a utility to assist you in
# testing your solution, and that the judging of your submission in
# the contest will not necessarily work exactly like this tool.
#
# The tool is provided as-is, and you should feel free to make
# whatever alterations or augmentations you like to it.
#
import argparse
import subprocess
import sys
import random

MAX_ROUNDS = 50
POPULATION = 10**7

def error(msg):
    print('ERROR: %s' % msg)
    sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description='''Testing tool for the "Infection Estimation" problem from NCPC 2020.

See source code for further info.''')
    parser.add_argument('infected', type=int,
                        help='Number of infected people')
    parser.add_argument('program', nargs='+',
                        help='Command to execute your solution program, for instance "./a.out" or "java MySolution"')
    args = parser.parse_args()

    infected = [1]*args.infected + [0]*(POPULATION-args.infected)
    
    process = subprocess.Popen(args.program, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    rounds_used = 0

    while True:
        action = process.stdout.readline().decode('utf8')
        rounds_used += 1
        
        tokens = action.split()
        if len(tokens) != 2:
            error('invalid action "%s"' % action)
        cmd = tokens[0]
        try:
            param = int(tokens[1])
        except:
            error('invalid parameter "%s" in action "%s"' % (param, action))
        if param < 1 or param > POPULATION:
            error('invalid parameter "%d" in action "%s"' % (param, action))
            
        
        if cmd == 'test':
            response = 0
            for i in range(param):
                j = random.randint(i, POPULATION-1)
                (infected[i], infected[j]) = (infected[j], infected[i])
                if infected[i]:
                    response = 1
            print('[*] Round %2d: received "test %d", response %d' % (rounds_used, param, response))
            if rounds_used > MAX_ROUNDS:
                error('Solution used too many rounds')
            process.stdin.write(('%d\n' % response).encode('utf8'))
            process.stdin.flush()
        elif cmd == 'estimate':
            rel_err = 100.0 * (param - args.infected) / args.infected
            print('[*] Round %2d: received "estimate %d", relative error %.2f%%' % (rounds_used, param, rel_err))
            if 2*param < args.infected or param > 2*args.infected:
                error('Too large error')
            break
        else:
            error('invalid action "%s"' % action)
        
    print('[*] OK, solution estimate is within tolerance!')


if __name__=='__main__':
    main()