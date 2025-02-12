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
    replacements = {}
    for line in lines[:-2]:
        i,_,o = line.split()
        if i not in replacements.keys():
            replacements[i] = []
        replacements[i].append(o)
    options = set()
    molecule = lines[-1]
    for i in range(len(molecule)):
        if molecule[i] in replacements.keys():
            for r in replacements[molecule[i]]:
                options.add(molecule[:i] + r + molecule[i+1:])
        if molecule[i:i+2] in replacements.keys():
            for r in replacements[molecule[i:i+2]]:
                options.add(molecule[:i] + r + molecule[i+2:])
    return len(options)

for type in ["test","real"]:
    input = getInput(f'{type}input.txt')
    if len(input) > 0:
        start = time.time()
        res = solve(input)
        end = time.time()
        print(f'Run "{type}" took {(end-start)} seconds.')
        print(f'Result: {res}')