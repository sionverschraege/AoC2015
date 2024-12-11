import time
from pathlib import Path
import hashlib

def getInput(filename):
    path = Path(__file__)
    input = open(f'{path.parent.absolute()}\\{filename}')
    lines = input.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].removesuffix('\n')
    return lines

def solve(lines):
    v = 0
    while True:
        key = lines[0] + str(v)
        hex = hashlib.md5(key.encode()).hexdigest()
        if hex[0:5] == '00000':
            return v
        v += 1

for type in ["test","real"]:
    input = getInput(f'{type}input.txt')
    if len(input) > 0:
        start = time.time()
        res = solve(input)
        end = time.time()
        print(f'Run "{type}" took {(end-start)} seconds.')
        print(f'Result: {res}')