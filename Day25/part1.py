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
    l = lines[0].split('.')[1].split('at row ')[1]
    line, col = [int(x) for x in l.split(', column ')]
    # 1 + 2 + .... + n-1 + n
    #   = 1+n * (n/2)
    trirow = line + col - 2
    n = (((1+trirow)*trirow)//2) + col - 1
    c = 20151125
    for i in range(n):
        c *= 252533
        c %= 33554393
    return c

for type in ["test","real"]:
    input = getInput(f'{type}input.txt')
    if len(input) > 0:
        start = time.time()
        res = solve(input)
        end = time.time()
        print(f'Run "{type}" took {(end-start)} seconds.')
        print(f'Result: {res}')