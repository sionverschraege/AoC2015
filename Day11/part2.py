import time
from pathlib import Path

def getInput(filename):
    path = Path(__file__)
    input = open(f'{path.parent.absolute()}\\{filename}')
    lines = input.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].removesuffix('\n')
    return lines

alphabet = 'abcdefghijklmnopqrstuvwxyz'
la = len(alphabet)
forbidden = [alphabet.find(c) for c in 'oil']

def inc(pw, index):
    pw[index] = pw[index] + 1
    while pw[index] == 26 and index > 0:
        pw[index] = 0
        index -= 1
        pw[index] = pw[index] + 1
    return pw

def solve(lines):
    pw = [alphabet.find(c) for c in lines[1]]
    lp = len(pw)
    ok = False
    while not ok:
        # print(''.join([alphabet[c] for c in pw]))
        ok  = True
        for f in forbidden:
            if f in pw:
                fi = pw.index(f)
                inc(pw, fi)
                for i in range(fi+1, lp):
                    pw[i] = 0
                ok = False
        dubs = {}
        for i in range(1,len(pw)):
            if pw[i] not in dubs.keys() and pw[i-1] == pw[i]:
                dubs[pw[i]] = i-1
        if len(dubs) < 2:
            ok = False
            if len(dubs) == 1:
                if pw[-2] > pw[-1]:
                    pw[-1] = pw[-2]
                else:
                    if pw[-2] + 1 == pw[-3]:
                        pw[-2] = pw[-3]
                        pw[-1] = 0
                    else:
                        pw = inc(pw, lp-2)
                        pw[-1] = pw[-2]
            else:
                # ....aabb
                if pw[-4] > pw[-3]:
                    pw[-3] = pw[-4]
                    pw[-2] = 0
                    pw[-1] = 0
                else:
                    if pw[-4] + 1 == pw[-5]:
                        pw[-4] = pw[-5]
                        pw[-3] = 0 
                        pw[-2] = 0
                        pw[-1] = 0
                    else:
                        pw = inc(pw, lp-4)
                        pw[-3] = pw[-4]
                        pw[-2] = 0 if pw[-3] > 0 else 1
                        pw[-1] = pw[-2]
        xyz = -1
        for i in range(2,len(pw)):
            if xyz == -1 and pw[i-2] + 1 == pw[i-1] and pw[i-1] + 1 == pw[i]:
                xyz = i
        if xyz == -1:
            ok = False
            if pw[-3] > 23 or pw[-3] == 23 and pw[-2] > 24:
                pw = inc(pw, lp-3)
            elif pw[-3] > pw[-2] - 1 or pw[-3] == pw[-2] - 1 and pw[-2] > pw[-1] - 1:
                pw[-2] = pw[-3] + 1
                pw[-1] = pw[-2] + 1
            else:
                pw = inc(pw, lp-3)
    return ''.join([alphabet[c] for c in pw])


for type in ["test","real"]:
    input = getInput(f'{type}input.txt')
    if len(input) > 0:
        start = time.time()
        res = solve(input)
        end = time.time()
        print(f'Run "{type}" took {(end-start)} seconds.')
        print(f'Result: {res}')