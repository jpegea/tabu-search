from tabusearch import tsfirstimp, tsbestimp
from constructives import ctabusearch
from structure import solution
import time

def execute(inst, iters, tabutenure, initial="random", alpha=0, printIters=False):
    tabulist = [None] * tabutenure
    sol = ctabusearch.initialSolution(inst, initial, alpha)
    best = {'sol' : sol['sol'].copy(), 'of' : sol['of']}
    for i in range(iters):
        if printIters:
            print("\t| Iter:", i)

        tsfirstimp.move(sol, tabulist, printIters)
        if best['of'] < sol['of']:
            best = {'sol' : sol['sol'].copy(), 'of' : sol['of']}

        if printIters:
            print("\t| Best:\n\t|     OF:  " + str(round(best['of'],2)) +
                  "\t|     Sol: " + str(best['sol']) +
                  "\t↓ Tabulist: " + str(tabulist))
            solution.prettyPrintSolution(sol)
    return best


def executeduring(inst, execTime, tabutenure, initial="random", alpha=0):
    tabulist = [None] * tabutenure
    best = solution.createEmptySolution(inst)
    start = time.time()
    sol = ctabusearch.initialSolution(inst, initial, alpha)
    iters = 0
    while time.time() - start < execTime:
        tsfirstimp.move(sol, tabulist)
        iters += 1
        if best['of'] < sol['of']:
            best = {'sol' : sol['sol'].copy(), 'of' : sol['of']}
    return best, iters