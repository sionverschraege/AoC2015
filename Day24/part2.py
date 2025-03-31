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
    weights = [int(l) for l in lines]
    aim = sum(weights) // 4
    solution = []
    i = 1
    cache = {}
    while len(solution) == 0:
        sols = getWeightWithN(weights, aim, i, cache)
        for s in sols:
            left = weights.copy()
            for w in s:
                left.remove(w)
            if canSplitThreeWays(left, aim, cache, [0, 0, 0]):
                solution.append(s)
        i += 1
    best = 2**1000
    for s in solution:
        quant = reduce(lambda a,b: a*b, s)
        best = min(best,quant)
    return best

def getWeightWithN(wts, target, n, cache):
    # Assumes weights are sorted ascending
    if len(wts) < n:
        return []
    if wts[-1] <= target // n:
        return []
    if n == 1:
        return [[target]] if target in wts else []
    key = f'{wts} - {target} - {n}'
    if key in cache:
        return cache[key]
    subs = []
    for i in range(len(wts)):
        sub = getWeightWithN(wts[:-i-1], target-wts[-i-1], n-1, cache)
        for s in sub:
            subs.append(s + [wts[-i-1]])
    cache[key] = subs
    return subs

def canSplitThreeWays(left, aim, cache, split: list):
    if any([x > aim for x in split]):
        return False
    if len(left) == 0:
        return split[0] == split[1] and split[1] == split[2]
    split.sort()
    key = f'{left} - {aim} - {split}'
    if key in cache:
        return cache[key]
    next = left[-1]
    options = [[split[j] + (next if j == i else 0) for j in range(3)] for i in range(3)]
    res = any([canSplitThreeWays(left[:-1], aim, cache, option) for option in options])
    cache[key] = res
    return res

for type in ["test","real"]:
    input = getInput(f'{type}input.txt')
    if len(input) > 0:
        start = time.time()
        res = solve(input)
        end = time.time()
        print(f'Run "{type}" took {(end-start)} seconds.')
        print(f'Result: {res}')