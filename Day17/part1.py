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
    amount = int(input[0])
    containers = [int(l) for l in input[1:]]
    current = {amount:1}
    cneeded = {amount:0}
    for c in containers:
        next = {}
        nextcn = {}
        for k in current.keys():
            for nk,cn in [(k,cneeded[k]), (k-c,cneeded[k]+1)]:
                if nk not in next.keys() or cn < nextcn[nk]:
                    next[nk] = 0
                    nextcn[nk] = cn
                if cn == nextcn[nk]:
                    next[nk] += current[k]
        current = next
        cneeded = nextcn
    return current[0]

for type in ["test","real"]:
    input = getInput(f'{type}input.txt')
    if len(input) > 0:
        start = time.time()
        res = solve(input)
        end = time.time()
        print(f'Run "{type}" took {(end-start)} seconds.')
        print(f'Result: {res}')