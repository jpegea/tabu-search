from matplotlib import pyplot as plt
import numpy as np

time = [i for i in range(0, 60, 5)]

ts1 = [6543.76, 8024.33, 8033.03, 8034.58, 8036.43, 8039.24, 8039.24, 8039.24, 8039.24, 8039.24, 8039.24, 8039.24]
ts2 = [6639.28, 8176.65, 8204.19, 8205.79, 8205.79, 8213.98, 8213.98, 8213.98, 8213.98, 8213.98, 8213.98, 8213.98]
ts3 = [6330.34, 7742.04, 7745.83, 7799.15, 7816.61, 7816.61, 7817.29, 7817.29, 7817.29, 7817.29, 7817.29, 7817.29]
ts4 = [6358.79, 7894.24, 7899.44, 7900.5, 7917.17, 7917.17, 7919.61, 7919.61, 7919.61, 7922.45, 7922.45, 7922.45]

plt.figure(figsize=(8, 3), dpi=200) 

plt.plot(time, ts1, marker='d', color='blue', label='TS 1', linestyle='--', linewidth=1)
plt.plot(time, ts2, marker='D', color='red', label='TS 2', linestyle='--', linewidth=1)
plt.plot(time, ts3, marker='P', color='magenta', label='TS 3', linestyle='--', linewidth=1)
plt.plot(time, ts4, marker='X', color='green', label='TS 4', linestyle='--', linewidth=1)

plt.xlabel("Time (in seconds)")
plt.ylabel("Objective Function value")
plt.title("Evolution of the best solution found over time")
plt.legend(fontsize=10, loc='lower right', ncol=2)

plt.tight_layout()
plt.show()