from constructives import ctabusearch
from localsearch import tsbestimp, tsfirstimp
from structure import solution

def execute(inst, iters, tabutenure, initial="greedy", alpha=0):
    tabulist = [None] * tabutenure
    sol = chooseInitialSolution(inst, initial, alpha)
    best = {'sol':sol['sol'].copy(), 'of':sol['of']}
    tabulistAtBest = None

    for i in range(iters):
        
        tsfirstimp.move(sol, tabulist)

        # Alerta de ciclado
        if sol['sol'] == best['sol']:
            if tabulistAtBest is not None and set(tabulist) == set(tabulistAtBest):
                print("\033[41mCICLADO!\033[0m en Iter:", i)
            else:
                # print("\033[105mPosible ciclado\033[0m en Iter:", i)
                pass

        if best['of'] < sol['of']:
            print(str(round(best['of'],2))+'\t-> '+str(round(sol['of'],2)))
            best = {'sol':sol['sol'].copy(), 'of':sol['of']}
            tabulistAtBest = tabulist.copy()
        
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