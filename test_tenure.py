from algorithms import tabusearch
from structure import instance
import random, time


def test(inst):
    for tabutenure in range(20, 60, 10):
        print(tabutenure, end=', ')
        for t in range(20, 60, 10):
            sol, iters = tabusearch.executeduring(inst, t, tabutenure, "random")
            print(round(sol['of'], 2), end=', ')
            print(t, end=', ')
            print(iters, end=', ')
        print()


def testAllInstances():
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


random.seed(1)

start = time.time()
testAllInstances()
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
