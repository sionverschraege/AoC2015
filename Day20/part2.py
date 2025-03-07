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
    target = (int(lines[0])-1) // 11 + 1
    divisors = {}
    maxd = 0
    current = 0
    while maxd < target:
        current += 1
        currentd = 2
        while current % currentd != 0 and currentd * currentd < current:
            currentd += 1
        divisors[current] = {1,current}
        if currentd * currentd <= current:
            divisors[current] = divisors[current].union(set([a*b for a in divisors[currentd] for b in divisors[current // currentd]]))
        min = (current - 1) // 50 + 1
        total = sum([d for d in divisors[current] if d >= min])
        maxd = max(maxd, total)
    return current

for type in ["test","real"]:
    input = getInput(f'{type}input.txt')
    if len(input) > 0:
        start = time.time()
        res = solve(input)
        end = time.time()
        print(f'Run "{type}" took {(end-start)} seconds.')
        print(f'Result: {res}')