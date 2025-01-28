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
    line = lines[0]
    total = 0
    while len(line) > 0:
        n,line = solveLine(line)
        total += n
    return total

def solveLine(line) -> tuple[int,str]:
    openingChar = line[0]
    if openingChar == '{':
        return solveDict(line)
    else:
        return solveArray(line)

def solveArray(line):
    cur = 1
    num = ''
    total = 0
    while cur < len(line):
        ch = line[cur]
        if ch in '-0123465789':
            num += ch
        else:
            if len(num) > 0:
                total += int(num)
                num = ''
            if ch == ']':
               # print(f'Total {total} for line {line[:cur+1]}')
                return (total, line[cur+1:])
            elif ch in '{[':
                n2,l2 = solveLine(line[cur:])
                total += n2
                line = line[:cur] + 'X' + l2
        cur += 1

def solveDict(line):
    cur = 1
    num = ''
    total = 0
    key = True
    red = 0
    isRed = False
    while cur < len(line):
        ch = line[cur]
        if ch in '-0123465789':
            if not key:
                num += ch
            red = 0
        else:
            if len(num) > 0:
                total += int(num)
                num = ''
            if not isRed and ch == '"red"'[red]:
                red += 1
                if red == 5:
                    isRed = True
            else:
                red = 0
            if ch == '}':
               # print(f'Total {0 if isRed else total} for line {line[:cur+1]}')
                return (0 if isRed else total, line[cur+1:])
            elif ch == ',':
                key = True
            elif ch == ':':
                key = False
            elif ch in '{[':
                n2,l2 = solveLine(line[cur:])
                total += n2
                line = line[:cur] + 'X' + l2
        cur += 1

for type in ["test","real"]:
    input = getInput(f'{type}input.txt')
    if len(input) > 0:
        start = time.time()
        res = solve(input)
        end = time.time()
        print(f'Run "{type}" took {(end-start)} seconds.')
        print(f'Result: {res}')

# 45383 too low
# 73822 too high