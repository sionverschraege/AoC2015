import time
from pathlib import Path

def getInput(filename):
    path = Path(__file__)
    input = open(f'{path.parent.absolute()}\\{filename}')
    lines = input.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].removesuffix('\n')
    return lines

def solve(lines):
    l = [int(i) for i in lines[0]]
    for _ in range(50):
        nl = []
        last = 0
        count = 0
        for c in l:
            if c == last:
                count += 1
            else:
                if last > 0:
                    nl = nl + [count, last]
                last = c
                count = 1
        nl = nl + [count, last]
        last = c
        count = 1
        l = nl
    return len(l)

for type in ["test","real"]:
    input = getInput(f'{type}input.txt')
    if len(input) > 0:
        start = time.time()
        res = solve(input)
        end = time.time()
        print(f'Run "{type}" took {(end-start)} seconds.')
        print(f'Result: {res}')