import time
from pathlib import Path

def getInput(filename):
    path = Path(__file__)
    input = open(f'{path.parent.absolute()}\\{filename}')
    lines = input.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].removesuffix('\n')
    return lines

split = ['2131','2132','2312','2313']
#         21113
#         231(13|23|33)
#         213(21|11)

def solve(lines):
    parts = {lines[0]:1}
    cache = {}
    for i in range(50):
        parts = solveParts(parts, cache)
    return sum([parts[k] * len(k) for k in parts.keys()])

def solveParts(parts, cache): 
    newparts = {}
    for k in parts.keys():
        nps = []
        if k in cache.keys():
            nps = cache[k]
        else:
            nl = ''
            last = ''
            count = 0
            for c in k:
                if c == last:
                    count += 1
                else:
                    if last != '':
                        nl = nl + str(count) + str(last)
                    last = c
                    count = 1
            nl = nl + str(count) + str(last)
            nps = []
            nnl = ''
            for c in nl:
                nnl += c
                if nnl[-4:] in split:
                    nps.append(nnl[:-3])
                    nnl = nnl[-3:]
            nps.append(nnl)
            cache[k] = nps
        for np in nps:
            if np not in newparts.keys():
                newparts[np] = 0
            newparts[np] += parts[k]
    return newparts

for type in ["test","real"]:
    input = getInput(f'{type}input.txt')
    if len(input) > 0:
        start = time.time()
        res = solve(input)
        end = time.time()
        print(f'Run "{type}" took {(end-start)} seconds.')
        print(f'Result: {res}')