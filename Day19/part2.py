import time
from pathlib import Path

def getInput(filename):
    path = Path(__file__)
    input = open(f'{path.parent.absolute()}\\{filename}')
    lines = input.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].removesuffix('\n')
    return lines

def toMolecule(s: str) -> str:
    m = ''
    for c in s:
        if c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZe':
            if m != '':
                m += '-'
            m += c
        else:
            m += c
    return m

def solve(lines):
    itoo = {}
    otoi = {}
    for line in lines[:-2]:
        i,_,o = line.split()
        i,o = (toMolecule(i),toMolecule(o)) 
        if i not in itoo.keys():
            itoo[i] = []
        itoo[i].append(o)
        if o not in otoi.keys():
            otoi[o] = []
        otoi[o].append(i)
    notJustAtStart = set()
    maybeJustAtStart = set()
    for key in otoi.keys():
        atom = key.split('-')[0]
        if atom not in notJustAtStart:
            maybeJustAtStart.add(atom)
        for atom in key.split('-')[1:]:
            notJustAtStart.add(atom)
            maybeJustAtStart.discard(atom)
    for key in itoo.keys():
        atom = key.split('-')[0]
        if atom not in notJustAtStart:
            maybeJustAtStart.add(atom)
    changed = True
    while changed:
        changed = False
        toSwitch = set()
        for n in notJustAtStart:
            if n in itoo.keys():
                for tg in itoo[n]:
                    toSwitch.add(tg.split('-')[0])
        if maybeJustAtStart.intersection(toSwitch):
            changed = True
            notJustAtStart = notJustAtStart.union(toSwitch)
            maybeJustAtStart = maybeJustAtStart.difference(toSwitch)
    
    justAtStart = maybeJustAtStart

    options = {toMolecule(lines[-1])}
    steps = 0
    while 'e' not in options:
        steps += 1
        nopts = set()
        for o in options:
            for i in range(len(o)):
                for di in range(15):
                    if o[i:i+di] in otoi.keys():
                        for tg in otoi[o[i:i+di]]:
                            if i == 0 or tg.split('-')[0] not in justAtStart:
                                nopt = o[:i] + tg + o[i+di:]
                                if nopt == 'e' or nopt[0] != 'e':
                                    nopts.add(nopt)
        options = nopts
    return steps
    # lastStep = (lines[-1],0,None)
    # while lastStep[0] != 'e':


for type in ["test","real"]:
    input = getInput(f'{type}input.txt')
    if len(input) > 0:
        start = time.time()
        res = solve(input)
        end = time.time()
        print(f'Run "{type}" took {(end-start)} seconds.')
        print(f'Result: {res}')