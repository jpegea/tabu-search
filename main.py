from structure import instance, solution
from algorithms import tabusearch, grasp
import random, time

def executeInstance():
    path = "instances/MDG-a_6_n500_m50.txt"
    inst = instance.readInstance(path)
    sol = tabusearch.execute(inst, 800, 20, "random", 0, True)
    sol = grasp.execute(inst, 500, 0.4)
    print("\nBEST SOLUTION:")
    solution.prettyPrintSolution(sol)

if __name__ == '__main__':
    random.seed(1)
    start = time.time()
    executeInstance()
    total_time = time.time() - start
    print("\nTime:", total_time)
