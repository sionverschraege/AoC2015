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
    coords = {(0,0)}
    dir = {'>':(1,0),'<':(-1,0),'^':(0,1),'v':(0,-1)}
    x = 0
    y = 0
    for c in lines[0][::2]:
        dx,dy = dir[c]
        x += dx
        y += dy
        coords.add((x,y))
    x = 0
    y = 0
    for c in lines[0][1::2]:
        dx,dy = dir[c]
        x += dx
        y += dy
        coords.add((x,y))
    return len(coords)

for type in ["test","real"]:
    input = getInput(f'{type}input.txt')
    if len(input) > 0:
        start = time.time()
        res = solve(input)
        end = time.time()
        print(f'Run "{type}" took {(end-start)} seconds.')
        print(f'Result: {res}')