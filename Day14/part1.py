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
    best = 0
    for line in lines:
        _,_,_,k,_,_,a,_,_,_,_,_,_,b,_ = line.split()
        k,a,b = [int(x) for x in [k,a,b]]
        wh = dist // (a+b)
        r = dist % (a+b)
        best = max(k*(wh*a + min(a,r)), best)
    return best

for type in ["test","real"]:
    input = getInput(f'{type}input.txt')
    if len(input) > 0:
        start = time.time()
        res = solve(input)
        end = time.time()
        print(f'Run "{type}" took {(end-start)} seconds.')
        print(f'Result: {res}')