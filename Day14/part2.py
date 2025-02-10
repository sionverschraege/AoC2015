import time
from pathlib import Path

def getInput(filename):
    path = Path(__file__)
    input = open(f'{path.parent.absolute()}\\{filename}')
    lines = input.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].removesuffix('\n')
    return lines

dist = 2503

def solve(lines):
    deers = []
    dists = []
    pts = []
    for line in lines:
        _,_,_,k,_,_,a,_,_,_,_,_,_,b,_ = line.split()
        k,a,b = [int(x) for x in [k,a,b]]
        deers.append((k,a,a+b))
        dists.append(0)
        pts.append(0)
    for t in range(dist):
        best = 0
        for i in range(len(deers)):
            deer = deers[i]
            if(t % deer[2] < deer[1]):
                dists[i] += deer[0]
            best = max(best,dists[i])
        for i in range(len(deers)):
            if dists[i] == best:
                pts[i] += 1
    return max(pts)

for type in ["test","real"]:
    input = getInput(f'{type}input.txt')
    if len(input) > 0:
        start = time.time()
        res = solve(input)
        end = time.time()
        print(f'Run "{type}" took {(end-start)} seconds.')
        print(f'Result: {res}')