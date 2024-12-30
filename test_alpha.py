from algorithms import grasp
from structure import instance
import random, time
import numpy as np

def test(instances, testTime):
    alpha = [round(0.1 * k, 1) for k in range(2, 10)]
    rel = np.zeros(8)
    for i in list(instances):
        inst = instances[i]
        maxOf = 0
        of = np.empty((8, 2))
        for j in range(8):
            sol1, _ = grasp.executeduring(inst, testTime, alpha[j])
            sol2, _ = grasp.executeduring(inst, testTime, alpha[j])
            maxOf = np.max([maxOf, sol1['of'], sol2['of']])
            of[j] = sol1['of'], sol2['of']
        relOf = (maxOf - of) / maxOf
        for j in range(8):
            rel[j] += np.sum(relOf[j])
    for k in range(8):
        print("alpha = " + str(alpha[k]), end=', ')
        print(rel[k])
            

        
def allInstances():
    instances = {}

    path = "instances/MDG-a_2_n500_m50.txt"
    instances[2] = instance.readInstance(path)

    path = "instances/MDG-a_5_n500_m50.txt"
    instances[5] = instance.readInstance(path)

    path = "instances/MDG-a_6_n500_m50.txt"
    instances[6] = instance.readInstance(path)

    path = "instances/MDG-a_9_n500_m50.txt"
    instances[9] = instance.readInstance(path)

    path = "instances/MDG-a_13_n500_m50.txt"
    instances[13] = instance.readInstance(path)

    path = "instances/MDG-a_16_n500_m50.txt"
    instances[16] = instance.readInstance(path)

    path = "instances/MDG-a_17_n500_m50.txt"
    instances[17] = instance.readInstance(path)

    path = "instances/MDG-a_19_n500_m50.txt"
    instances[19] = instance.readInstance(path)

    path = "instances/MDG-a_20_n500_m50.txt"
    instances[20] = instance.readInstance(path)

    path = "instances/MDG-a_1_100_m10.txt"
    instances[1] = instance.readInstance(path)

    path = "instances/MDG-a_4_100_m10.txt"
    instances[4] = instance.readInstance(path)

    path = "instances/MDG-a_10_100_m10.txt"
    instances[10] = instance.readInstance(path)

    path = "instances/MDG-a_12_100_m10.txt"
    instances[12] = instance.readInstance(path)

    path = "instances/MDG-a_14_100_m10.txt"
    instances[14] = instance.readInstance(path)

    return instances


random.seed(1)

start = time.time()
test(allInstances(), 10)
end = time.time() - start

hours = int(end / 60**2)
end -= hours * 60**2
minutes = int(end / 60)
end -= minutes * 60
seconds = int(end)
print("\nTime elapsed during the test:", end=' ')
print(str(hours) + "h, " +
      str(minutes) + " m, " +
      str(seconds) + " s")
