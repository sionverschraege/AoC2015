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
    ingredients = [(int(c[:-1]),int(d[:-1]),int(f[:-1]),int(t[:-1]),int(cal)) for _,_,c,_,d,_,f,_,t,_,cal in [l.split() for l in lines]]
    return max([reduce(lambda a,b: a*b if a > 0 and b > 0 else 0, [sum(ing[i] for ing in option) for i in range(4)]) for option in getOptions(ingredients, 0, 100, 500, {})])

def getOptions(ingredients, ni, n, cals, cache):
    if n == 0 and cals == 0:
        return [[]]
    elif ni >= len(ingredients) or n <= 0 or cals <= 0:
        return []
    elif (ni,n,cals) in cache.keys():
        return cache[(ni,n,cals)]
    else:
        options = []
        for nni in [ni, ni+1]:
            if nni < len(ingredients):
                i = ingredients[nni]
                if i[4] <= cals:
                    options += [[i] + so for so in getOptions(ingredients, nni, n - 1, cals - i[4], cache)]
        cache[(ni,n,cals)] = options
        return options

for type in ["test","real"]:
    input = getInput(f'{type}input.txt')
    if len(input) > 0:
        start = time.time()
        res = solve(input)
        end = time.time()
        print(f'Run "{type}" took {(end-start)} seconds.')
        print(f'Result: {res}')