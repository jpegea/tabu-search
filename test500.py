from structure import instance
from algorithms import grasp, tabusearch
import random, time

def printOutput(alg, sol, iters):
    print(alg, end = ', ')
    print(str(round(sol['of'], 2)), end=', ')
    print(str(iters))


def test(inst, testTime):
    alpha = [0.4, 0.7]
    tenure = [30, 40]
    for a in alpha:
        alg = "Grasp α = " + str(a)
        sol, iters = grasp.executeduring(inst, testTime, a)
        printOutput(alg, sol, iters)
    for t in tenure:
        alg = "TS tenure = " + str(t)
        sol, iters = tabusearch.executeduring(inst, testTime, t, "greedy", 0.7)
        printOutput(alg, sol, iters)

        
random.seed(1)
testTime = 10

start = time.time()

path = "instances/MDG-a_2_n500_m50.txt"
inst = instance.readInstance(path)
print("\nInstance 2,", path)
test(inst, testTime)

path = "instances/MDG-a_5_n500_m50.txt"
inst = instance.readInstance(path)
print("\nInstance 5,", path)
test(inst, testTime)

path = "instances/MDG-a_6_n500_m50.txt"
inst = instance.readInstance(path)
print("\nInstance 6,", path)
test(inst, testTime)

path = "instances/MDG-a_9_n500_m50.txt"
inst = instance.readInstance(path)
print("\nInstance 9,", path)
test(inst, testTime)

path = "instances/MDG-a_13_n500_m50.txt"
inst = instance.readInstance(path)
print("\nInstance 13,", path)
test(inst, testTime)

path = "instances/MDG-a_16_n500_m50.txt"
inst = instance.readInstance(path)
print("\nInstance 16,", path)
test(inst, testTime)

path = "instances/MDG-a_17_n500_m50.txt"
inst = instance.readInstance(path)
print("\nInstance 17,", path)
test(inst, testTime)

path = "instances/MDG-a_19_n500_m50.txt"
inst = instance.readInstance(path)
print("\nInstance 19,", path)
test(inst, testTime)

path = "instances/MDG-a_20_n500_m50.txt"
inst = instance.readInstance(path)
print("\nInstance 20,", path)
test(inst, testTime)

end = time.time() - start
minutes = int(end / 60)
seconds = int(end - minutes*60)
print("\nTime elapsed during the test:", end=' ')
print(str(minutes) + " minutes, " + str(seconds) + " seconds")
