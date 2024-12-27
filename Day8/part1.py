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
    diff = 0
    for line in lines:
        lastSlash = False
        inHex = 0
        for c in line:
            if lastSlash:
                lastSlash = False
                if c == 'x':
                    inHex = 1
                else:
                    diff += 1
            elif inHex > 0:
                if c in '0123456789abcdef':
                    inHex += 1
                    if inHex == 3:
                        diff += 3
                        inHex = 0
                else:
                    diff += 1
            else:
                if c == '"':
                    diff += 1
                if c == '\\':
                    lastSlash = True
    return diff

for type in ["test","real"]:
    input = getInput(f'{type}input.txt')
    if len(input) > 0:
        start = time.time()
        res = solve(input)
        end = time.time()
        print(f'Run "{type}" took {(end-start)} seconds.')
        print(f'Result: {res}')