from matplotlib import pyplot as plt
import numpy as np

time = [i+1 for i in range(10)]
# SEED 1
ts1 = [7446.67, 7572.36, 7702.41, 7764.47, 7764.47, 7797.77, 7847.39, 7847.39, 7872.35, 7872.35]
# SEED 2
ts2 = [7419.38, 7618.84, 7779.45, 7906.07, 7924.04, 7945.99, 7945.99, 7945.99, 7946.62, 7955.27]
# SEED 1
grasp1 = [7719.83, 7719.83, 7719.83, 7719.83, 7719.83, 7719.83, 7719.83, 7719.83, 7719.83, 7719.83]
# SEED 2
grasp2 = [7670.39, 7670.39, 7682.76, 7682.76, 7682.76, 7682.76, 7682.76, 7682.76, 7709.65, 7709.65]

plt.figure(figsize=(9.5, 3.5), dpi=200) 
plt.grid(True, axis='y', linestyle='--', linewidth=0.5)
plt.plot(time, ts1, marker='d', color='black', label='TS 1', linestyle='--', linewidth=1)
plt.plot(time, ts2, marker='D', color='black', label='TS 2', linestyle='--', linewidth=1)
plt.plot(time, grasp1, marker='+', color='black', label='GRASP 1', linestyle='--', linewidth=1)
plt.plot(time, grasp2, marker='x', color='black', label='GRASP 2', linestyle='--', linewidth=1)
plt.xlabel("Time (in seconds)")
plt.ylabel("Objective Function value")
plt.title("Evolution of the algorithms at short executions")
plt.legend(fontsize=10, loc='upper left', ncol=2)

plt.tight_layout()
plt.show()

