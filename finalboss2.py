from algorithms import tabusearch
from structure import instance
import numpy as np
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

# 10 seconds
f = open("test10s2.csv", 'w')
random.seed(1)
for inst in instances:
    if inst['n'] == 100:
        s1 = tabusearch.execute(inst, 14000, 30, "random", 0, True)
        s2 = tabusearch.execute(inst, 14000, 30, "random", 0, True)
        s3 = tabusearch.execute(inst, 14000, 30, "random", 0, True)
        s4 = tabusearch.execute(inst, 14000, 30, "random", 0, True)
        sol = np.max([s1['of'], s2['of'], s3['of'], s4['of']])
        f.write(str(round(sol, 2)) + ', ')
    else:
        s1 = tabusearch.execute(inst, 400, 30, "random", 0, True)
        s2 = tabusearch.execute(inst, 400, 30, "random", 0, True)
        s3 = tabusearch.execute(inst, 400, 30, "random", 0, True)
        s4 = tabusearch.execute(inst, 400, 30, "random", 0, True)
        sol = np.max([s1['of'], s2['of'], s3['of'], s4['of']])
        f.write(str(round(sol, 2)) + ', ')
    f.write('\n')
f.close()