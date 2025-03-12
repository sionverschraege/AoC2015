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
    ptr = 0
    reg = {'a':1,'b':0}
    while ptr < len(input):
        split = input[ptr].split()
        if len(split) == 2:
            inst, op = split
        else:
            inst, op1, op2 = split
            op1 = op1[:-1]
        match inst:
            case 'hlf':
                reg[op] /= 2
            case 'tpl':
                reg[op] *= 3
            case 'inc':
                reg[op] += 1
            case 'jmp':
                ptr += int(op) - 1
            case 'jie':
                ptr += int(op2)-1 if reg[op1] % 2 == 0 else 0
            case 'jio':
                ptr += int(op2)-1 if reg[op1] == 1 else 0
        ptr += 1
    return reg

for type in ["test","real"]:
    input = getInput(f'{type}input.txt')
    if len(input) > 0:
        start = time.time()
        res = solve(input)
        end = time.time()
        print(f'Run "{type}" took {(end-start)} seconds.')
        print(f'Result: {res}')