from structure import instance, solution
from algorithms import tabusearch, grasp, prettyTabusearch
import random, time

def executeInstance():
    path = "instances/MDG-a_2_n500_m50.txt"
    inst = instance.readInstance(path)
    sol = prettyTabusearch.execute(inst, 1000, 20, "random")
    # sol = tabusearch.execute(inst, 2000, 10)
    # sol = grasp.execute(inst, 100, 0.3)
    print("\nBEST SOLUTION:")
    solution.prettyPrintSolution(sol)

if __name__ == '__main__':
    random.seed(1)
    start = time.time()
    executeInstance()
    total_time = time.time() - start
    print("\nTime:", total_time)
