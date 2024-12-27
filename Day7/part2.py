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
    out = 'i' if len(lines) < 100 else 'a'
    solved = {}
    ops = {}
    triggers = {}
    tocheck = set()
    for line in lines:
        op,to = line.split(' -> ')
        if to == 'b':
            op = '3176'
        opa = op.split()
        if opa[0] == 'NOT':
            op = ('NOT',[opa[1]])
        elif len(opa) == 3:
            op = (opa[1], [opa[0], opa[2]])
        else:
            op = ('', [opa[0]])
        if all([s.isnumeric() for s in op[1]]):
            tocheck.add(to)
        else:
            for s in op[1]:
                if not s.isnumeric():
                    if s not in triggers.keys():
                        triggers[s] = []
                    triggers[s].append(to)
        ops[to] = op
    
    while len(tocheck) > 0:
        to = tocheck.pop()
        op = ops[to]
        if all([s.isnumeric() or s in solved.keys() for s in op[1]]):
            facs = [int(s) if s.isnumeric() else solved[s] for s in op[1]]
            operation = op[0]
            if operation == 'NOT':
                solved[to] = 65535 - facs[0]
            elif operation == 'LSHIFT':
                solved[to] = facs[0] << facs[1]
            elif operation == 'RSHIFT':
                solved[to] = facs[0] >> facs[1]
            elif operation == 'AND':
                solved[to] = facs[0] & facs[1]
            elif operation == 'OR':
                solved[to] = facs[0] | facs[1]
            else:
                solved[to] = facs[0]
            if to in triggers.keys():
                for tr in triggers[to]:
                    tocheck.add(tr)

    return solved[out]

for type in ["test","real"]:
    input = getInput(f'{type}input.txt')
    if len(input) > 0:
        start = time.time()
        res = solve(input)
        end = time.time()
        print(f'Run "{type}" took {(end-start)} seconds.')
        print(f'Result: {res}')