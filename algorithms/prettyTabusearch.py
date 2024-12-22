from localsearch import tabulsbestimp
from structure import solution
from algorithms import tabusearch

def execute(inst, iters, tabutenure, initial="greedySolution", alpha=0):
    tabulist = [None] * tabutenure
    sol = tabusearch.chooseInitialSolution(inst, initial, alpha)
    best = {'sol':sol['sol'].copy(), 'of':sol['of']}
    tabulistAtBest = None

    solution.prettyPrintSolution(sol)

    for i in range(iters):
        print("\t| Iter:", i)
        
        tabulsbestimp.moveAndPrint(sol, tabulist)

        # Alerta de ciclado
        if sol['sol'] == best['sol']:
            if tabulistAtBest is not None and set(tabulist) == set(tabulistAtBest):
                print("\033[41mCICLADO!\033[0m en Iter:", i)
            else:
                print("\033[105mPosible ciclado\033[0m en Iter:", i)

        if best['of'] < sol['of']:
            # print(str(round(best['of'],2))+'\t-> '+str(round(sol['of'],2)))
            best = {'sol':sol['sol'].copy(), 'of':sol['of']}
            tabulistAtBest = tabulist.copy()
        
        print("\t| Best:")
        print("\t|     OF:  " + str(round(best['of'],2)))
        print("\t|     Sol: " + str(best['sol']))
        print("\t↓ Tabulist: " + str(tabulist))

        solution.prettyPrintSolution(sol)
        input("\t|")
    return best