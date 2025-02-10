import time
from pathlib import Path
from functools import reduce

def getInput(filename):
    path = Path(__file__)
    input = open(f'{path.parent.absolute()}\\{filename}')
    lines = input.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].removesuffix('\n')
    return lines

def solve(lines):
    ingredients = [(int(c[:-1]),int(d[:-1]),int(f[:-1]),int(t[:-1])) for _,_,c,_,d,_,f,_,t,_,_ in [l.split() for l in lines]]
    dirs = []
    for i1 in ingredients:
        for i2 in ingredients:
            if i1 != i2:
                dirs.append([i1[i] - i2[i] for i in range(4)])
    d = 100/len(ingredients)
    current = [sum([d * ing[i] for ing in ingredients]) for i in range(4)]
    currentval = min(current) if min(current) < 0 else reduce(lambda a,b: a*b, current)
    changed = True
    while changed:
        changed = False
        for dir in dirs:
            next = [current[i] + dir[i] for i in range(4)]
            nextVal = min(next) if min(next) < 0 else reduce(lambda a,b: a*b, next)
            while nextVal > currentval:
                changed = True
                currentval = nextVal
                current = next
                next = [current[i] + dir[i] for i in range(4)]
                nextVal = min(next) if min(next) < 0 else reduce(lambda a,b: a*b, next)
    return currentval

for type in ["test","real"]:
    input = getInput(f'{type}input.txt')
    if len(input) > 0:
        start = time.time()
        res = solve(input)
        end = time.time()
        print(f'Run "{type}" took {(end-start)} seconds.')
        print(f'Result: {res}')