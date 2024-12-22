from structure import solution
from constructives import cgrasp

def greedySolution(inst):
    sol = cgrasp.construct(inst, 0)
    return sol
