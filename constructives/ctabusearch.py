from structure import solution
from constructives import cgrasp
from localsearch import lsbestimp
import random

def greedySolution(inst):
    sol = cgrasp.construct(inst, 0)
    return sol


def greedyRandomizedSolution(inst, alpha):
    sol = cgrasp.construct(inst, alpha)
    return sol


def graspSolution(inst, alpha):
    sol = cgrasp.construct(inst, alpha)
    lsbestimp.improve(sol)
    return sol


def randomSolution(inst):
    sol = solution.createEmptySolution(inst)
    n = inst['n']
    while not solution.isFeasible(sol):
        print("No factible:", sol['sol'])
        add = True
        while add:
            u = random.randint(0, n-1)
            print(str(u)+', '+str(solution.contains(sol,u)))
            if not solution.contains(sol, u):
                solution.addToSolution(sol, u)
                add = False
    return sol