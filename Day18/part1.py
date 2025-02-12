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
    state = [[False for _ in range(len(lines[0])+2)]] + [[False] + [c == '#' for c in line] + [False] for line in lines] \
        + [[False for _ in range(len(lines[0])+2)]]
    for x in (1,len(state)-2):
        for y in (1,len(state)-2):
            state[x][y] = True
    for _ in range(100):
        newState = [[False for b in l] for l in state]
        for x in range(1,len(state[0])-1):
            for y in range(1,len(state)-1):
                if x in (1,len(state)-2) and y in (1,len(state)-2):
                    newState[x][y] = True
                else:
                    nb = sum([state[x+dx][y+dy] for dx,dy in [(-1,0),(1,0),(0,1),(0,-1),(1,1),(-1,-1),(-1,1),(1,-1)]])
                    newState[x][y] = nb == 3 or (nb == 2 and state[x][y])
        state = newState
    return sum([sum([b for b in l]) for l in state])

for type in ["test","real"]:
    input = getInput(f'{type}input.txt')
    if len(input) > 0:
        start = time.time()
        res = solve(input)
        end = time.time()
        print(f'Run "{type}" took {(end-start)} seconds.')
        print(f'Result: {res}')