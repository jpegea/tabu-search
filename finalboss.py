from algorithms import grasp, tabusearch
from structure import instance
import random

def allInstances():
    instances = []

    path = "instances/MDG-a_1_100_m10.txt"
    instances.append(instance.readInstance(path))

    path = "instances/MDG-a_4_100_m10.txt"
    instances.append(instance.readInstance(path))

    path = "instances/MDG-a_10_100_m10.txt"
    instances.append(instance.readInstance(path))

    path = "instances/MDG-a_12_100_m10.txt"
    instances.append(instance.readInstance(path))

    path = "instances/MDG-a_14_100_m10.txt"
    instances.append(instance.readInstance(path))

    path = "instances/MDG-a_20_100_m10.txt"
    instances.append(instance.readInstance(path))

    path = "instances/MDG-a_2_n500_m50.txt"
    instances.append(instance.readInstance(path))

    path = "instances/MDG-a_5_n500_m50.txt"
    instances.append(instance.readInstance(path))

    path = "instances/MDG-a_6_n500_m50.txt"
    instances.append(instance.readInstance(path))

    path = "instances/MDG-a_9_n500_m50.txt"
    instances.append(instance.readInstance(path))

    path = "instances/MDG-a_13_n500_m50.txt"
    instances.append(instance.readInstance(path))

    path = "instances/MDG-a_16_n500_m50.txt"
    instances.append(instance.readInstance(path))

    path = "instances/MDG-a_17_n500_m50.txt"
    instances.append(instance.readInstance(path))

    path = "instances/MDG-a_19_n500_m50.txt"
    instances.append(instance.readInstance(path))

    path = "instances/MDG-a_20_n500_m50.txt"
    instances.append(instance.readInstance(path))

    return instances


instances = allInstances()

"""
f = open("test10s.csv", 'w')
# 10 seconds
random.seed(1)
for inst in instances:
    if inst['n'] == 100:
        sol = grasp.execute(inst, 11000, 0.2, True)
        f.write(str(round(sol['of'], 2)) + ', ')
        sol = grasp.execute(inst, 8100, 0.5, True)
        f.write(str(round(sol['of'], 2)) + ', ')
        sol = tabusearch.execute(inst, 13000, 20, "random", 0, True)
        f.write(str(round(sol['of'], 2)) + ', ')
        sol = tabusearch.execute(inst, 14000, 30, "random", 0, True)
        f.write(str(round(sol['of'], 2)) + ', ')
    else:
        sol = grasp.execute(inst, 200, 0.2, True)
        f.write(str(round(sol['of'], 2)) + ', ')
        sol = grasp.execute(inst, 100, 0.5, True)
        f.write(str(round(sol['of'], 2)) + ', ')
        sol = tabusearch.execute(inst, 380, 20, "random", 0, True)
        f.write(str(round(sol['of'], 2)) + ', ')
        sol = tabusearch.execute(inst, 400, 30, "random", 0, True)
        f.write(str(round(sol['of'], 2)) + ', ')
    f.write('\n')
f.close()
"""

# 40 seconds
f = open("test40s.csv", 'w')
random.seed(1)
for inst in instances:
    if inst['n'] == 100:
        sol = grasp.execute(inst, 44000, 0.2, True)
        f.write(str(round(sol['of'], 2)) + ', ')
        sol = grasp.execute(inst, 30000, 0.5, True)
        f.write(str(round(sol['of'], 2)) + ', ')
        sol = tabusearch.execute(inst, 51000, 20, "random", 0, True)
        f.write(str(round(sol['of'], 2)) + ', ')
        sol = tabusearch.execute(inst, 55000, 30, "random", 0, True)
        f.write(str(round(sol['of'], 2)) + ', ')
    else:
        sol = grasp.execute(inst, 790, 0.2, True)
        f.write(str(round(sol['of'], 2)) + ', ')
        sol = grasp.execute(inst, 390, 0.5, True)
        f.write(str(round(sol['of'], 2)) + ', ')
        sol = tabusearch.execute(inst, 800, 20, "random", 0, True)
        f.write(str(round(sol['of'], 2)) + ', ')
        sol = tabusearch.execute(inst, 820, 30, "random", 0, True)
        f.write(str(round(sol['of'], 2)) + ', ')
    f.write('\n')
f.close()