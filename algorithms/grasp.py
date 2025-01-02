from structure import solution
from constructives import cgrasp
from localsearch import lsbestimp
import time

def execute(inst, iters, alpha, printIters=False):
    best = None
    for i in range(iters):

        if printIters:
            print("Iter "+str(i+1)+": ", end="")

        sol = cgrasp.construct(inst, alpha)
        if printIters:
            print("C -> "+str(round(sol['of'], 2)), end=", ")

        lsbestimp.improve(sol)
        if printIters:
            print("LS -> "+str(round(sol['of'], 2)))
        
        if best is None or best['of'] < sol['of']:
            best = sol
    return best


def executeduring(inst, execTime, alpha):
    start = time.time()
    iters = 0
    best = solution.createEmptySolution(inst)
    printAt = 0
    while time.time() - start < execTime:
        if time.time() - start > printAt:
            printAt += 1
            print(round(best['of'], 2), end=', ')
        sol = cgrasp.construct(inst, alpha)
        lsbestimp.improve(sol)
        iters += 1
        if best['of'] < sol['of']:
            best = sol
    return best, iters