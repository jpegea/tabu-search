from structure import instance
from algorithms import grasp, tabusearch
import random, time

def printOutput(alg, sol, iters):
    print(alg, end = ', ')
    print("OF: " + str(round(sol['of'], 2)), end=', ')
    print("Iters: " + str(iters))

    
def test(inst, testTime):
    alpha = [0.4, 0.7]
    tenure = [30, 40]
    for a in alpha:
        alg = "Grasp α = " + str(a)
        sol, iters = grasp.executeduring(inst, testTime, a)
        printOutput(alg, sol, iters)
    for t in tenure:
        alg = "TS tenure = " + str(t)
        sol, iters = tabusearch.executeduring(inst, testTime, t)
        printOutput(alg, sol, iters)
        

random.seed(1)
testTime = 10

start = time.time()

path = "instances/MDG-a_1_100_m10.txt"
inst = instance.readInstance(path)
print("\nInstance 1,", path)
test(inst, testTime)

path = "instances/MDG-a_4_100_m10.txt"
inst = instance.readInstance(path)
print("\nInstance 4,", path)
test(inst, testTime)

path = "instances/MDG-a_10_100_m10.txt"
inst = instance.readInstance(path)
print("\nInstance 10,", path)
test(inst, testTime)

path = "instances/MDG-a_12_100_m10.txt"
inst = instance.readInstance(path)
print("\nInstance 12,", path)
test(inst, testTime)

path = "instances/MDG-a_14_100_m10.txt"
inst = instance.readInstance(path)
print("\nInstance 14,", path)
test(inst, testTime)

end = time.time() - start
minutes = int(end / 60)
seconds = int(end - minutes*60)
print("\nTime elapsed during the test:", end=' ')
print(str(minutes) + " minutes, " + str(seconds) + " seconds")
