from constructives import ctabusearch
from localsearch import tabulsbestimp
from structure import solution

def execute(inst, iters, tabutenure, initial="greedySolution", alpha=0):
    tabulist = [None] * tabutenure
    sol = chooseInitialSolution(inst, initial, alpha)
    best = None
    for i in range(iters):
        # old = {'sol':sol['sol'].copy(), 'of':sol['of']}
        tabulsbestimp.move(sol, tabulist)
        if best is not None and sol['sol'] == best['sol']:
            print("Iter: "+str(i)+" Ciclado: hem tornat a Best")
            pass
        if best is None or best['of'] < sol['of']:
            if best is not None:
                print(str(round(best['of'],2))+'\t-> '+str(round(sol['of'],2)))
            best = {'sol':sol['sol'].copy(), 'of':sol['of']}
        # print("Best: "+str(round(best['of'],2))+", Now: "+str(round(sol['of'],2)))
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