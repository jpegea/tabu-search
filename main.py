from structure import instance, solution
from algorithms import tabusearch, grasp
import random, time

def executeInstance():
    path = "instances/MDG-a_16_n500_m50.txt"
    inst = instance.readInstance(path)
    sol = tabusearch.execute(inst, 2000, 10, "greedyRandomized", 0.2)
    # sol = grasp.execute(inst, 50, 0.3)
    print("\nBEST SOLUTION:")
    solution.printSolution(sol)

if __name__ == '__main__':
    # random.seed(1)
    start = time.time()
    executeInstance()
    total_time = time.time() - start
    print("Time:", total_time)
