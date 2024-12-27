from algorithms import grasp
from structure import instance
import random, time

def test(inst, testTime):
    print("Grasp " + str(testTime) + " seconds")
    iter_list = []
    for j in range(2, 9):
        alpha = 0.1 * j;
        sol, iters = grasp.executeduring(inst, testTime, alpha)
        print(str(round(sol['of'], 2)))
        iter_list.append(iters)
    for iters in iter_list:
        print(iters)


def testProblems(testTime):
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

    path = "instances/MDG-a_9_n500_m50.txt"
    inst = instance.readInstance(path)
    print("\nInstance 9,", path)
    test(inst, testTime)

    path = "instances/MDG-a_13_n500_m50.txt"
    inst = instance.readInstance(path)
    print("\nInstance 13,", path)
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


random.seed(1)

start = time.time()
# for t in range(10, 60, 10):
#     testProblems(t)
testProblems(10)
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
