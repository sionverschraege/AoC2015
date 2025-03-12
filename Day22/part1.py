import time
import heapq
from pathlib import Path

def getInput(filename):
    path = Path(__file__)
    input = open(f'{path.parent.absolute()}\\{filename}')
    lines = input.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].removesuffix('\n')
    return lines

mm = lambda u,b,m,h,p,s,r: (u+53,b-4,m-53,h,p,s,r)
dr = lambda u,b,m,h,p,s,r: (u+73,b-2,m-73,h+2,p,s,r)
sh = lambda u,b,m,h,p,s,r: (u+113,b,m-113,h,p,s+6,r)
po = lambda u,b,m,h,p,s,r: (u+173,b,m-173,h,p+6,s,r)
re = lambda u,b,m,h,p,s,r: (u+229,b,m-229,h,p,s,r+5)

def bosss(c,bdmg):
    u,b,m,h,p,s,r = c
    return boss(u,b,m,h,p,s,r,bdmg)

def boss(u,b,m,h,p,s,r,bdmg):
    if b > 0:
        if s > 0:
            h -= bdmg - 7
        else:
            h -= bdmg
    return (u,b,m,h,p,s,r)

def tickk(c):
    u,b,m,h,p,s,r = c
    return tick(u,b,m,h,p,s,r)

def tick(u,b,m,h,p,s,r):
    if p > 0:
        p -= 1
        b -= 3
    if s > 0:
        s -= 1
    if r > 0:
        r -= 1
        m += 101
    return (u,b,m,h,p,s,r)

def solve(lines):
    # used, bhp, mana, hp, ptmr, stmr, rtmr
    bhp = int(input[0].split()[2])
    bdmg = int(input[1].split()[1])
    php = int(input[2].split()[1])
    pm = int(input[3].split()[1])
    states = [(0, bhp, pm, php, 0, 0, 0, '')]
    u,b,m,h,p,s,r,hist = heapq.heappop(states)
    #print("popping",u,b,m,h,p,s,r)
    while b > 0 or m < 0 or h < 0:
        if m < 0 or h < 0 or (m <= 52 and r == 0):
            u,b,m,h,p,s,r = heapq.heappop(states)
            #print("popping",u,b,m,h,p,s,r)
        else:
            u,b,m,h,p,s,r = tick(u,b,m,h,p,s,r)
            heapq.heappush(states,bosss(tickk(mm(u,b,m,h,p,s,r)),bdmg))
            if m >= 73:
                heapq.heappush(states,bosss(tickk(dr(u,b,m,h,p,s,r)),bdmg))
            if m >= 113 and s == 0:
                heapq.heappush(states,bosss(tickk(sh(u,b,m,h,p,s,r)),bdmg))
            if m >= 173 and p == 0:
                heapq.heappush(states,bosss(tickk(po(u,b,m,h,p,s,r)),bdmg))
            if m >= 229 and r == 0:
                heapq.heappush(states,bosss(tickk(re(u,b,m,h,p,s,r)),bdmg))
            u,b,m,h,p,s,r = heapq.heappop(states)
            #print("popping",u,b,m,h,p,s,r)

    return u

for type in ["test","real"]:
    input = getInput(f'{type}input.txt')
    if len(input) > 0:
        start = time.time()
        res = solve(input)
        end = time.time()
        print(f'Run "{type}" took {(end-start)} seconds.')
        print(f'Result: {res}')