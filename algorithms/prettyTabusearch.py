from tabusearch import tsfirstimp
from structure import solution
from algorithms import tabusearch
from tabusearch import tsbestimp

def execute(inst, iters, tabutenure, initial="greedySolution", alpha=0):
    tabulist = [None] * tabutenure
    sol = tabusearch.chooseInitialSolution(inst, initial, alpha)
    best = {'sol':sol['sol'].copy(), 'of':sol['of']}
    solution.prettyPrintSolution(sol)
    for i in range(iters):
        print("\t| Iter:", i)
        tsbestimp.move(sol, tabulist, True)
        if best['of'] < sol['of']:
            best = {'sol':sol['sol'].copy(), 'of':sol['of']}
            tabulistAtBest = tabulist.copy()
        print("\t| Best:")
        print("\t|     OF:  " + str(round(best['of'],2)))
        print("\t|     Sol: " + str(best['sol']))
        print("\t↓ Tabulist: " + str(tabulist))
        solution.prettyPrintSolution(sol)
        # input("\t|")
    return best