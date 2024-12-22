from constructives import ctabusearch
from localsearch import tabulsbestimp

def execute(inst, iters, tabutenure):
    tabulist = [None] * tabutenure
    best = None
    sol = ctabusearch.greedySolution(inst)
    for i in range(iters):
        tabulsbestimp.move(sol, tabulist)
        if best is not None and sol['sol'] == best['sol']:
            print("Hem tornat a al pico")
        if best is None or best['of'] < sol['of']:
            if best is not None:
                print(str(round(best['of'],2))+'\t-> '+str(round(sol['of'],2)))
            best = sol.copy()
    return best
