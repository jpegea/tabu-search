from structure import instance, solution
from algorithms import tabusearch, grasp
import random, time

def executeInstance():
    path = "instances/MDG-a_2_n500_m50.txt"
    inst = instance.readInstance(path)
    sol = tabusearch.execute(inst, 10000, 20)
    #sol = grasp.execute(inst, 1000, 0.2)
    print("\nBEST SOLUTION:")
    solution.printSolution(sol)

if __name__ == '__main__':
    # random.seed(1)
    start = time.time()
    executeInstance()
    total_time = time.time() - start
    print("Time:", total_time)
