from structure import instance, solution
from algorithms import tabu
import random
import time

def executeInstance():
    m=10
    path = "instances/MDG-a_4_100_m10.txt"
    inst = instance.readInstance(path)
    sol = tabu.execute(inst, 100, 1, m)
    print("\nBEST SOLUTION:")
    solution.printSolution(sol)

inicio = time.time()
if __name__ == '__main__':
    random.seed(1)
    executeInstance()
final = time.time()
print(final-inicio)