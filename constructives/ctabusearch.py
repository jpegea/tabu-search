from constructives import cgrasp
from structure import solution
import random

def initialSolution(inst, initial, alpha):
    if initial == "random":
        sol = solution.createEmptySolution(inst)
        n = inst['n']
        while not solution.isFeasible(sol):
            u = random.randint(0, n-1)
            solution.addToSolution(sol, u)
        return sol
    elif initial == "greedy":
        sol = cgrasp.construct(inst, alpha)
    else:
        sol = cgrasp.construct(inst, 0)
    return sol
