from structure import instance
from algorithms import grasp, tabusearch
import random, time


def test(inst):
    print("\t\t| OF \t\t| Time \t\t| Iterations \t|")
    print('-'*16+'+'+'-'*15+'+'+'-'*15+'+'+'-'*15+'+')
    
    iterGrasp = 500

    start = time.time()
    sol = grasp.execute(inst, iterGrasp, 0.3, False)
    end = time.time() - start
    print("Grasp α = 0.3 \t|", end=' ')
    print(str(round(sol['of'], 2)) + "\t|", end=' ')
    print(str(round(end, 4)) + "\t|", end=' ')
    print(str(iterGrasp) + "\t\t|")

    iterGrasp = 450

    start = time.time()
    sol = grasp.execute(inst, iterGrasp, 0.6, False)
    end = time.time() - start
    print("Grasp α = 0.6 \t|", end=' ')
    print(str(round(sol['of'], 2)) + "\t|", end=' ')
    print(str(round(end, 4)) + "\t|", end=' ')
    print(str(iterGrasp) + "\t\t|")

    iterGrasp = 300

    start = time.time()
    sol = grasp.execute(inst, iterGrasp, 0.8, False)
    end = time.time() - start
    print("Grasp α = 0.8 \t|", end=' ')
    print(str(round(sol['of'], 2)) + "\t|", end=' ')
    print(str(round(end, 4)) + "\t|", end=' ')
    print(str(iterGrasp) + "\t\t|")

    iterTS = 800

    start = time.time()
    sol = tabusearch.execute(inst, iterTS, 20, "random", 0, False)
    end = time.time() - start
    print("TS, tenure=20 \t|", end=' ')
    print(str(round(sol['of'], 2)) + "\t|", end=' ')
    print(str(round(end, 4)) + "\t|", end=' ')
    print(str(iterTS) + "\t\t|")

    start = time.time()
    sol = tabusearch.execute(inst, iterTS, 30, "random", 0, False)
    end = time.time() - start
    print("TS, tenure=30 \t|", end=' ')
    print(str(round(sol['of'], 2)) + "\t|", end=' ')
    print(str(round(end, 4)) + "\t|", end=' ')
    print(str(iterTS) + "\t\t|")

    start = time.time()
    sol = tabusearch.execute(inst, iterTS, 50, "random", 0, False)
    end = time.time() - start
    print("TS, tenure=50 \t|", end=' ')
    print(str(round(sol['of'], 2)) + "\t|", end=' ')
    print(str(round(end, 4)) + "\t|", end=' ')
    print(str(iterTS) + "\t\t|")


random.seed(1)
startTest = time.time()

path = "instances/MDG-a_2_n500_m50.txt"
inst = instance.readInstance(path)
print("\nInstance 2,", path)
test(inst)

path = "instances/MDG-a_5_n500_m50.txt"
inst = instance.readInstance(path)
print("\nInstance 5,", path)
test(inst)

path = "instances/MDG-a_6_n500_m50.txt"
inst = instance.readInstance(path)
print("\nInstance 6,", path)
test(inst)

path = "instances/MDG-a_9_n500_m50.txt"
inst = instance.readInstance(path)
print("\nInstance 9,", path)
test(inst)

path = "instances/MDG-a_13_n500_m50.txt"
inst = instance.readInstance(path)
print("\nInstance 13,", path)
test(inst)

path = "instances/MDG-a_16_n500_m50.txt"
inst = instance.readInstance(path)
print("\nInstance 16,", path)
test(inst)

path = "instances/MDG-a_17_n500_m50.txt"
inst = instance.readInstance(path)
print("\nInstance 17,", path)
test(inst)

path = "instances/MDG-a_19_n500_m50.txt"
inst = instance.readInstance(path)
print("\nInstance 19,", path)
test(inst)

path = "instances/MDG-a_20_n500_m50.txt"
inst = instance.readInstance(path)
print("\nInstance 20,", path)
test(inst)

timeTest = time.time() - startTest
minutes = int(timeTest / 60)
seconds = int(timeTest - minutes*60)
print("\nTime elapsed during the test:", end=' ')
print(str(minutes) + " minutes, " + str(seconds) + " seconds")
