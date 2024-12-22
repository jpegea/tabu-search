from structure import instance, solution
from algorithms import tabu
import random
import time

def executeInstance():
    m=11
    path = "instances/MDG-a_2_n500_m50.txt"
    inst = instance.readInstance(path)
    sol = tabu.execute(inst, 3000, 0, m)
    print("\nBEST SOLUTION:")
    solution.printSolution(sol)

inicio = time.time()
if __name__ == '__main__':
    random.seed(1)
    executeInstance()
final = time.time()
print(final-inicio)