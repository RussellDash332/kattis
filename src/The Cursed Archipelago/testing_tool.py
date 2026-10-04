#!/usr/bin/env python3
#
# Testing tool for the task The Cursed Archipelago.
#
# Usage:
#
#   python3 testing_tool.py [--silent] program... < input.txt
#
# input.txt uses the following format:
#
#   N Z L Q p [T]
#   idx1 val1
#   idx2 val2
#   ...
#
# where N is length, Z max non-zeros, L max lies, Q max queries, p prime.
# The following lines list the actual non-zero indices and values.
#

import subprocess
import sys
import random

def error(msg):
    print("ERROR:", msg)
    sys.exit(1)

def main():
    silent = False
    args = sys.argv[1:]
    if args and args[0] == "--silent":
        args = args[1:]
        silent = True

    if not args or args == ["--help"] or args == ["-h"]:
        print("Usage:", sys.argv[0], "[--silent] program... < input.txt")
        sys.exit(0)
    
    try:
        line = sys.stdin.readline().split()
        if not line: error("Empty input")
        N, Z, L, Q, p = map(int, line[:5])
    except Exception as e:
        error(f"bad input format for first line: {e}")
    
    A = {}
    try:
        for line in sys.stdin:
            if not line.strip(): continue
            idx, val = map(int, line.split())
            A[idx] = val
    except Exception as e:
        error(f"bad input format for non-zero elements: {e}")

    if len(A) > Z:
        error(f"Too many non-zero elements: {len(A)} > {Z}")

    proc = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=sys.stderr, text=True)

    if not silent:
        print(f"[*] Running with {N=}, {Z=}, {L=}, {Q=}, {p=}")

    # Send parameters to program
    proc.stdin.write(f"{N} {Z} {L} {Q} {p}\n")
    proc.stdin.flush()
    if not silent:
        print(f"< {N} {Z} {L} {Q} {p}")

    queries_used = 0
    lies_used = 0
    memo = {} # Track previous queries to be consistent

    while True:
        line = proc.stdout.readline()
        if not line:
            break
        line = line.strip()
        if not line: continue
        
        parts = line.split()
        cmd = parts[0]

        if cmd == "?":
            if not silent:
                print(f"> {line}")
            queries_used += 1
            if queries_used > Q:
                error(f"Too many queries: {queries_used} > {Q}")
            
            if len(parts) - 1 != N:
                error(f"Query vector has wrong length: {len(parts)-1} != {N}")
            
            X = list(map(int, parts[1:]))
            
            query_tuple = tuple(X)
            if query_tuple in memo:
                proc.stdin.write(f"{memo[query_tuple]}\n")
                proc.stdin.flush()
                if not silent:
                    print(f"< {memo[query_tuple]} (cached)")
                continue

            result = 0
            for idx, val in A.items():
                result = (result + val * X[idx-1]) % p
            
            # Simple random lie logic for testing tool.
            # In the real judge, lies are adversarial and maliciously calculated.
            should_lie = False
            if lies_used < L and random.random() < 0.1:
                should_lie = True
            
            if should_lie:
                lies_used += 1
                result = random.randint(0, p-1)
                if result == (sum(v * X[i-1] for i, v in A.items()) % p):
                    result = (result + 1) % p
            
            memo[query_tuple] = result
            proc.stdin.write(f"{result}\n")
            proc.stdin.flush()
            if not silent:
                print(f"< {result}")
            
        elif cmd == "!":
            if not silent:
                print(f"> {line}")
            try:
                K = int(parts[1])
                contestant_A = {}
                for _ in range(K):
                    l = proc.stdout.readline().split()
                    if not silent:
                        print(f"> {' '.join(l)}")
                    idx, val = map(int, l)
                    contestant_A[idx] = val
                
                if contestant_A == A:
                    print(f"[*] OK: Correct answer in {queries_used} queries ({lies_used} lies).")
                    sys.exit(0)
                else:
                    print(f"[*] WRONG ANSWER: Incorrect state vector.")
                    # Optional: print differences
                    sys.exit(1)
            except Exception as e:
                error(f"Failed to parse answer: {e}")
        else:
            error(f"Unknown command: {cmd}")

    if proc.wait() != 0:
        error("Program exited with non-zero status")

if __name__ == "__main__":
    main()