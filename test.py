from structure import instance
from algorithms import grasp, tabusearch
import random, time

def printOutput(alg, sol, iters):
    print(alg, end = '\t')
    print("OF: " + str(round(sol['of'], 2)), end='\t')
    print("Iters: " + str(iters))

    
def test(inst, testTime):
    for j in range(0, 11):
        alpha = round(0.3 + 0.05*j, 2)
        tenure = 20 + 2*j
        alg = "Grasp α = " + str(alpha)
        sol, iters = grasp.executeduring(inst, testTime, alpha)
        printOutput(alg, sol, iters)
        alg = "TS tenure = " + str(tenure)
        sol, iters = tabusearch.executeduring(inst, testTime, tenure)
        printOutput(alg, sol, iters)
        

random.seed(1)
testTime = 5

start = time.time()

path = "instances/MDG-a_1_100_m10.txt"
inst = instance.readInstance(path)
print("\nInstance 1,", path)
test(inst, testTime)

path = "instances/MDG-a_2_n500_m50.txt"
inst = instance.readInstance(path)
print("\nInstance 2,", path)
test(inst, testTime)

path = "instances/MDG-a_4_100_m10.txt"
inst = instance.readInstance(path)
print("\nInstance 4,", path)
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

path = "instances/MDG-a_10_100_m10.txt"
inst = instance.readInstance(path)
print("\nInstance 10,", path)
test(inst, testTime)

path = "instances/MDG-a_12_100_m10.txt"
inst = instance.readInstance(path)
print("\nInstance 12,", path)
test(inst, testTime)

path = "instances/MDG-a_13_n500_m50.txt"
inst = instance.readInstance(path)
print("\nInstance 13,", path)
test(inst, testTime)

path = "instances/MDG-a_14_100_m10.txt"
inst = instance.readInstance(path)
print("\nInstance 14,", path)
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
