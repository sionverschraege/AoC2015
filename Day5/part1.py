import time
from pathlib import Path

def getInput(filename):
    path = Path(__file__)
    input = open(f'{path.parent.absolute()}\\{filename}')
    lines = input.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].removesuffix('\n')
    return lines

vowels = 'aeiou'
forbidden = ['ab','cd','pq','xy']
def nice(s):
    v = 0
    d = False
    last = ''
    for c in s:
        if c in vowels:
            v += 1
        elif last + c in forbidden:
            return False
        if last == c:
            d = True
        last = c
    return d and v >= 3


def solve(lines):
    return sum([nice(l) for l in lines])

for type in ["test","real"]:
    input = getInput(f'{type}input.txt')
    if len(input) > 0:
        start = time.time()
        res = solve(input)
        end = time.time()
        print(f'Run "{type}" took {(end-start)} seconds.')
        print(f'Result: {res}')