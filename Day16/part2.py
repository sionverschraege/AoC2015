import time
from pathlib import Path

def getInput(filename):
    path = Path(__file__)
    input = open(f'{path.parent.absolute()}\\{filename}')
    lines = input.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].removesuffix('\n')
    return lines

detected = {k:v for k,v in [l.split() for l in '''children: 3
cats: >7
samoyeds: 2
pomeranians: <3
akitas: 0
vizslas: 0
goldfish: <5
trees: >3
cars: 2
perfumes: 1'''.split('\n')]}

for k,v in detected.items():
    if v[0] == '<':
        detected[k] = lambda x,v=v: x < int(v[1:])
    elif v[0] == '>':
        detected[k] = lambda x,v=v: x > int(v[1:])
    else:
        detected[k] = lambda x,v=v: x == int(v)

def solve(lines):
    for line in lines:
        has = {k:v for k,v in [val.split() for val in line.split(': ',1)[1].split(', ')]}
        if all([detected[k](int(has[k])) for k in has.keys()]):
            return line.split()[1][:-1]


for type in ["test","real"]:
    input = getInput(f'{type}input.txt')
    if len(input) > 0:
        start = time.time()
        res = solve(input)
        end = time.time()
        print(f'Run "{type}" took {(end-start)} seconds.')
        print(f'Result: {res}')