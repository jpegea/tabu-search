from structure import instance
from algorithms import grasp, tabusearch
import random, time


def test(inst, testTime):
    
    start = time.time()
    sol, iters = grasp.executeduring(inst, testTime, 0.35)
    end = time.time() - start
    print("Grasp α = 0.35", end='\t')
    print("OF: " + str(round(sol['of'],2)), end='\t')
    print("Time: " + str(round(end, 2)), end='\t')
    print("Iters: " + str(iters))

    start = time.time()
    sol, iters = grasp.executeduring(inst, testTime, 0.5)
    end = time.time() - start
    print("Grasp α = 0.5", end='\t')
    print("OF: " + str(round(sol['of'],2)), end='\t')
    print("Time: " + str(round(end, 2)), end='\t')
    print("Iters: " + str(iters))

    start = time.time()
    sol, iters = tabusearch.executeduring(inst, testTime, 30)
    end = time.time() - start
    print("TS tenure = 30", end='\t')
    print("OF: " + str(round(sol['of'], 2)), end='\t')
    print("Time: " + str(round(end, 2)), end='\t')
    print("Iters: " + str(iters))

    start = time.time()
    sol, iters = tabusearch.executeduring(inst, testTime, 40)
    end = time.time() - start
    print("TS tenure = 40", end='\t')
    print("OF: " + str(round(sol['of'], 2)), end='\t')
    print("Time: " + str(round(end, 2)), end='\t')
    print("Iters: " + str(iters))
    

random.seed(1)
testTime = 50

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

# path = "instances/MDG-a_9_n500_m50.txt"
# inst = instance.readInstance(path)
# print("\nInstance 9,", path)
# test(inst)

# path = "instances/MDG-a_13_n500_m50.txt"
# inst = instance.readInstance(path)
# print("\nInstance 13,", path)
# test(inst)

# path = "instances/MDG-a_16_n500_m50.txt"
# inst = instance.readInstance(path)
# print("\nInstance 16,", path)
# test(inst)

# path = "instances/MDG-a_17_n500_m50.txt"
# inst = instance.readInstance(path)
# print("\nInstance 17,", path)
# test(inst)

# path = "instances/MDG-a_19_n500_m50.txt"
# inst = instance.readInstance(path)
# print("\nInstance 19,", path)
# test(inst)

# path = "instances/MDG-a_20_n500_m50.txt"
# inst = instance.readInstance(path)
# print("\nInstance 20,", path)
# test(inst)

end = time.time() - start
minutes = int(end / 60)
seconds = int(end - minutes*60)
print("\nTime elapsed during the test:", end=' ')
print(str(minutes) + " minutes, " + str(seconds) + " seconds")
