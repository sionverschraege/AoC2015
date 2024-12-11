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
    total = 0
    for line in lines:
        dims = [int(d) for d in line.split('x')]
        perims = [2*(dims[i] + dims[(i+1)%3]) for i in range(3)]
        vol = 1
        for dim in dims:
            vol *= dim
        total += vol + min(perims) 
    return total

for type in ["test","real"]:
    input = getInput(f'{type}input.txt')
    if len(input) > 0:
        start = time.time()
        res = solve(input)
        end = time.time()
        print(f'Run "{type}" took {(end-start)} seconds.')
        print(f'Result: {res}')