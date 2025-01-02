from algorithms import tabusearch
from structure import instance

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


inst = allInstances()
for i in inst:
    sol, iters = tabusearch.executeduring(i, 40, 30)
    print(iters)