import time
from pathlib import Path
import heapq

def getInput(filename):
    path = Path(__file__)
    input = open(f'{path.parent.absolute()}\\{filename}')
    lines = input.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].removesuffix('\n')
    return lines

def toMolecule(s: str) -> str:
    m = ''
    for c in s:
        if c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZe':
            if m != '':
                m += '-'
            m += c
        else:
            m += c
    return m

def solve(lines):
    itoo = {}
    otoi = {}
    maxDiff = 0
    for line in lines[:-2]:
        i,_,o = line.split()
        if i not in itoo.keys():
            itoo[i] = []
        itoo[i].append(o)
        if o not in otoi.keys():
            otoi[o] = []
        otoi[o].append(i)
        maxDiff = max(maxDiff, len(o) - len(i))
    # estimate, estRemaining, done, str
    est = estimate(lines[-1], maxDiff)
    states = [(est, est, 0, lines[-1])]
    result = 0
    checked = {lines[-1]}
    while result == 0 and states:
        _, _, done, str = heapq.heappop(states)
        for i in range(len(str)):
            for di in range(1,10):
                if str[i:i+di] in otoi.keys():
                    for sub in otoi[str[i:i+di]]:
                        new = str[:i] + sub + str[i+di:]
                        if new == 'e':
                            result = done + 1
                        elif 'e' not in new and new not in checked:
                            est = estimate(new, maxDiff)
                            heapq.heappush(states, (est + 1 + done, est, 1 + done, new))
                            checked.add(new)
    return result

def estimate(str, maxDiff):
    return (len(str) - 1) // maxDiff

for type in ["test","real"]:
    input = getInput(f'{type}input.txt')
    if len(input) > 0:
        start = time.time()
        res = solve(input)
        end = time.time()
        print(f'Run "{type}" took {(end-start)} seconds.')
        print(f'Result: {res}')