import time
from pathlib import Path

def getInput(filename):
    path = Path(__file__)
    input = open(f'{path.parent.absolute()}\\{filename}')
    lines = input.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].removesuffix('\n')
    return lines

def shortestDist(start, rest, dists, cache):
    if len(rest) == 1:
        return dists[start + rest[0]]
    else:
        s = sum(rest) + 1024 * start
        if s in cache.keys():
            return cache[s]
        else:
            dist = min([dists[start + rest[i]] + shortestDist(rest[i], rest[:i] + rest[i+1:], dists, cache) for i in range(len(rest))])
            cache[s] = dist
            return dist

def solve(lines):
    dists = {}
    cities = {}
    curr = 1
    for line in lines:
        c,d = line.split(' = ')
        c = c.split(' to ')
        for city in c:
            if city not in cities.keys():
                cities[city] = curr
                curr *= 2
        dists[cities[c[0]] + cities[c[1]]] = int(d)
    rest = [v for v in cities.values()]
    return min([shortestDist(rest[i], rest[:i] + rest[i+1:], dists, {}) for i in range(len(rest))])

for type in ["test","real"]:
    input = getInput(f'{type}input.txt')
    if len(input) > 0:
        start = time.time()
        res = solve(input)
        end = time.time()
        print(f'Run "{type}" took {(end-start)} seconds.')
        print(f'Result: {res}')