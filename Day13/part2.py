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
    pts = {}
    options = set()
    for line in lines:
        p1,_,gl,n,_,_,_,_,_,_,p2 = line.split()
        p1 = p1[0]
        p2 = p2[0]
        pts[p1+p2] = int(n) if gl[0] == 'g' else -int(n)
        pts[p1+'Z'] = 0
        pts['Z'+p1] = 0
        options.add(p1)
    return best('Z','Z',options,pts)

def best(start,end,options,pts):
    if len(options) == 0:
        return pts[start+end] + pts[end+start]
    else:
        return max([best(o,end,options.difference({o}),pts) + pts[start+o]+pts[o+start] for o in options])

for type in ["test","real"]:
    input = getInput(f'{type}input.txt')
    if len(input) > 0:
        start = time.time()
        res = solve(input)
        end = time.time()
        print(f'Run "{type}" took {(end-start)} seconds.')
        print(f'Result: {res}')