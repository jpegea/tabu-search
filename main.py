from structure import instance, solution
from algorithms import tabusearch, grasp
import random

def executeInstance():
<<<<<<< HEAD
    m=11
    path = "instances/MDG-a_2_n500_m50.txt"
    inst = instance.readInstance(path)
    sol = tabu.execute(inst, 3000, 0, m)
=======
    path = "instances/MDG-a_2_n500_m50.txt"
    inst = instance.readInstance(path)
    sol = tabusearch.execute(inst, 3000, 11)
    # sol = grasp.execute(inst, 1000, 0.2)
>>>>>>> quim
    print("\nBEST SOLUTION:")
    solution.printSolution(sol)

if __name__ == '__main__':
    random.seed(1)
    executeInstance()
