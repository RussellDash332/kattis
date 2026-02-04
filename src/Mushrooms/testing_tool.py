#!/usr/bin/env python3
#
# Judge for the task Svampar.
#
# Usage:
#
#   python3 judge.py <input_file> < output
#
# input.txt uses the following format:
#
#   N
#   w_1 w_2 ... w_N
#
# where N is the number of mushrooms, and w_i is the desired final
# weight at position i
#
# For example, if you have a Python solution that you would run using
# "python3 file.py", you could test it as follows:
#
#   python3 file.py < input.txt > ans.txt
#   python3 judge.py input.txt < ans.txt
#
# where input.txt is a file that contains e.g.
#
# 5
# 10 5 2 5 2
#
# The tool is provided as-is, and you should feel free to make
# whatever alterations or augmentations you like to it.
# Notably, this is not the program used to test your solution in Kattis
#

import sys

if len(sys.argv) != 2:
    print("Usage: python3 judge.py <input_file> < output")
    exit(1)

with open(sys.argv[1], 'r') as f:
    n = int(f.readline().strip())
    arr = list(map(int, f.readline().strip().split()))

if len(arr) != n:
    print("Wrong length of array")
    exit(1)

if any(x < 0 or x > 255 for x in arr):
    print("Array elements must be between 0 and 255")
    exit(1)

rounds = int(input())
curr_arr = [0] * n
for round in range(rounds):
    new_arr = [0] * n
    def parse_line():
        i = 0
        ops = []
        tokens = input().split()
        while i < len(tokens):
            token = tokens[i]
            if token == 'p':
                ops.append((token, None))
                i += 1
            else:
                if i + 1 >= len(tokens):
                    print("Invalid operation format")
                    exit(1)
                idx = tokens[i + 1]
                if not idx.isdigit():
                    print("Index must be an integer")
                    exit(1)
                idx = int(idx)
                if idx < 1 or idx > n:
                    print(f"Index out of bounds: {idx}")
                    exit(1)
                ops.append((token, idx - 1))
                i += 2
        if len(ops) != n:
            print("Number of operations does not match n")
            exit(1)
        return ops
    
    ops = parse_line()

    for i in range(n):
        op, idx = ops[i]
        if op == "p":
            new_arr[i] = curr_arr[i]
        else:
            if op == '+':
                new_arr[i] = curr_arr[idx] + 1
            elif op == '<':
                new_arr[i] = curr_arr[idx] << 1
            elif op == '>':
                new_arr[i] = curr_arr[idx] >> 1
            elif op == '^':
                new_arr[i] = curr_arr[i] ^ curr_arr[idx]
            elif op == '&':
                new_arr[i] = curr_arr[i] & curr_arr[idx]
            elif op == '|':
                new_arr[i] = curr_arr[i] | curr_arr[idx]
            else:
                print(f"Unknown operation: {op}")
                exit(1)
    curr_arr = new_arr

if curr_arr == arr:
    print(f"Correct: uses {rounds} rounds")
    exit(0)
else:
    print("Incorrect")
    print(f"Target array: {arr}")
    print(f"Final array: {curr_arr}")
    exit(1)