from structure import instance
from algorithms import grasp, tabusearch
import random, time


def test(inst):
    print("\t\t| OF \t\t| Time \t\t| Iterations \t|")
    print('-'*16+'+'+'-'*15+'+'+'-'*15+'+'+'-'*15+'+')
    
    iterGrasp = 600

    start = time.time()
    sol = grasp.execute(inst, iterGrasp, 0.35)
    end = time.time() - start
    print("Grasp α = 0.35 \t|", end=' ')
    print(str(round(sol['of'], 2)) + "\t|", end=' ')
    print(str(round(end, 2)) + "\t\t|", end=' ')
    print(str(iterGrasp) + "\t\t|")

    iterGrasp = 500

    start = time.time()
    sol = grasp.execute(inst, iterGrasp, 0.5)
    end = time.time() - start
    print("Grasp α = 0.5 \t|", end=' ')
    print(str(round(sol['of'], 2)) + "\t|", end=' ')
    print(str(round(end, 2)) + "  \t|", end=' ')
    print(str(iterGrasp) + "\t\t|")

    iterTS = 800

    start = time.time()
    sol = tabusearch.execute(inst, iterTS, 30, "random")
    end = time.time() - start
    print("TS, tenure=30 \t|", end=' ')
    print(str(round(sol['of'], 2)) + "\t|", end=' ')
    print(str(round(end, 2)) + "  \t|", end=' ')
    print(str(iterTS) + "\t\t|")

    start = time.time()
    sol = tabusearch.execute(inst, iterTS, 40, "random")
    end = time.time() - start
    print("TS, tenure=40 \t|", end=' ')
    print(str(round(sol['of'], 2)) + "\t|", end=' ')
    print(str(round(end, 2)) + "  \t|", end=' ')
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
