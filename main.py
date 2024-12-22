from structure import instance, solution
from algorithms import tabusearch, grasp, prettyTabusearch
import random, time

def executeInstance():
    path = "instances/MDG-a_6_n500_m50.txt"
    inst = instance.readInstance(path)
    sol = prettyTabusearch.execute(inst, 50, 10, "greedyRandomized", 0.2)
    # sol = tabusearch.execute(inst, 30000, 10)
    # sol = grasp.execute(inst, 30, 0.3)
    print("\nBEST SOLUTION:")
    solution.prettyPrintSolution(sol)

if __name__ == '__main__':
    # random.seed(1)
    start = time.time()
    executeInstance()
    total_time = time.time() - start
    print("\nTime:", total_time)
