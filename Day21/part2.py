import time
from pathlib import Path

def getInput(filename):
    path = Path(__file__)
    input = open(f'{path.parent.absolute()}\\{filename}')
    lines = input.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].removesuffix('\n')
    return lines

wcost = [8,10,25,40,74]
wstr = lambda x: x+4
acost = [0,13,31,53,75,102]
astr = lambda x: x
rcost = [0,20,25,40,50,80,100]
rwstr = lambda x: 0 if x <= 0 or x % 2 == 1 else (x) // 2
rastr = lambda x: 0 if x <= 0 or x % 2 == 0 else (x+1) // 2

def solve(lines):
    return fight(0,0,0,0,int(lines[0].split()[2]),int(lines[1].split()[1]),int(lines[2].split()[1]), {})

def fight(w, a, r1, r2, bhp, bd, ba, cache):
    if w >= len(wcost) or a >= len(acost) or r1 >= len(rcost) or r2 >= len(rcost):
        return 0
    else:
        if (w,a,r1,r2) not in cache.keys():
            best = 0 if (r1 > 0 and r1 == r2) or win(w, a, r1, r2, bhp, bd, ba) else wcost[w] + acost[a] + rcost[r1] + rcost[r2]
            cache[(w,a,r1,r2)] = max(best,
                    fight(w+1,a,r1,r2,bhp,bd,ba,cache),
                    fight(w,a+1,r1,r2,bhp,bd,ba,cache),
                    fight(w,a,r1+1,r2,bhp,bd,ba,cache),
                    fight(w,a,r1,r2+1,bhp,bd,ba,cache))
        return cache[(w,a,r1,r2)]

def win(w, a, r1, r2, bhp, bd, ba):
    dpt = max(1,wstr(w) + rwstr(r1) + rwstr(r2) - ba)
    dptb = max(1,bd - astr(a) - rastr(r1) - rastr(r2))
    return ((bhp - 1) // dpt + 1) <= ((100 - 1) // dptb + 1)

for type in ["test","real"]:
    input = getInput(f'{type}input.txt')
    if len(input) > 0:
        start = time.time()
        res = solve(input)
        end = time.time()
        print(f'Run "{type}" took {(end-start)} seconds.')
        print(f'Result: {res}')