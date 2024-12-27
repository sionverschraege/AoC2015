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
    xcos = set()
    ycos = set()
    commands = []
    for line in lines:
        s = line.split()
        offset = 0 if s[0][1] == 'o' else 1
        comm = tuple((s[offset], int(s[offset+1].split(',')[0]), int(s[offset+1].split(',')[1]), int(s[offset+3].split(',')[0]) + 1, int(s[offset+3].split(',')[1]) + 1))
        xcos.add(comm[1])
        xcos.add(comm[3])
        ycos.add(comm[2])
        ycos.add(comm[4])
        commands.append(comm)
    xcos = [x for x in xcos]
    ycos = [y for y in ycos]
    xcos.sort()
    ycos.sort()
    xmap = {v:i for i,v in enumerate(xcos)}
    ymap = {v:i for i,v in enumerate(ycos)}
    on = [[0 for _ in xcos[1:]] for _ in ycos[1:]]
    for c in commands:
        for x in range(xmap[c[1]],xmap[c[3]]):
            for y in range(ymap[c[2]],ymap[c[4]]):
                if c[0] == 'off':
                    on[y][x] = max(0, on[y][x]-1)
                else:
                    on[y][x] += 1 if c[0] == 'on' else 2
    total = 0
    for x in range(len(xcos) - 1):
        for y in range(len(ycos) - 1):
            total += on[y][x] * (xcos[x+1] - xcos[x]) * (ycos[y+1] - ycos[y])
    return total

for type in ["test","real"]:
    input = getInput(f'{type}input.txt')
    if len(input) > 0:
        start = time.time()
        res = solve(input)
        end = time.time()
        print(f'Run "{type}" took {(end-start)} seconds.')
        print(f'Result: {res}')