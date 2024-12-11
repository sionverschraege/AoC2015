import time
from pathlib import Path

def getInput(filename):
    path = Path(__file__)
    input = open(f'{path.parent.absolute()}\\{filename}')
    lines = input.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].removesuffix('\n')
    return lines

def nice(s):
    pairs = []
    hasPair = False
    last = ['','']
    hasTrip = False
    for c in s:
        newPair = last[-1] + c
        if newPair in pairs[:-1]:
            hasPair = True
        pairs.append(newPair)
        if c == last[-2]:
            hasTrip = True
        last = [last[-1], c]
    return hasPair and hasTrip

def solve(lines):
    return sum([nice(l) for l in lines])

for type in ["test","real"]:
    input = getInput(f'{type}input.txt')
    if len(input) > 0:
        start = time.time()
        res = solve(input)
        end = time.time()
        print(f'Run "{type}" took {(end-start)} seconds.')
        print(f'Result: {res}')