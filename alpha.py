from algorithms import grasp
from structure import instance
import random, time

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


alpha = [round(0.1*i, 1) for i in range(2, 10)]
instances = allInstances()

start = time.time()
random.seed(1)

for inst in instances:
    for a in alpha:
        sol, _ = grasp.executeduring(inst, 40, a)
        print(str(round(sol['of'], 2)), end=', ')
    print()

end = time.time() - start
print("time:", end)