from constructives import ctabusearch
from tabusearch import tsfirstimp
from structure import solution
from tabusearch import tsbestimp

def execute(inst, iters, tabutenure, initial="greedy", alpha=0, printIters=False):
    tabulist = [None] * tabutenure
    sol = chooseInitialSolution(inst, initial, alpha)
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

def chooseInitialSolution(inst, initial, alpha):
    if initial == "random":
        sol = ctabusearch.randomSolution(inst)
    elif initial == "greedy":
        sol = ctabusearch.greedySolution(inst)
    elif initial == "greedyRandomized":
        sol = ctabusearch.greedyRandomizedSolution(inst, alpha)
    elif initial == "grasp":
        sol = ctabusearch.graspSolution(inst, alpha)
    else:
        sol = ctabusearch.greedySolution(inst)
    return sol