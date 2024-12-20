from constructives import cgrasp
from localsearch import lsbestimp
from tabusearch import tsbestimp


def execute(inst, iters, alpha,m):
    tabulist = [None] * m
    lolipop=-22222222222222222
    best = None
    sol = cgrasp.construct(inst, alpha)
    best = sol
    # lsbestimp.uploadlist(tabulist,sol['sol'][0])
    for i in range(iters):

        tsbestimp.move(sol,tabulist)
        # print("C -> "+str(round(sol['of'], 2)), end=", ")
        # lsbestimp.improve(sol)
        # print("LS -> "+str(round(sol['of'], 2)))
        
        if  lolipop < sol['of']:
            print('entrando al if')
            best = sol.copy()
            lolipop=sol['of']
            print(lolipop)

    return best
