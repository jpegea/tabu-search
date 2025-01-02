from matplotlib import pyplot as plt
import numpy as np

time = [5 * (i + 1) for i in range(20)]
# SEED 1
ts1 = [7813.82, 7914.81, 7915.88, 7922.96, 7952.73, 7971.83, 7987.26, 8013.36, 8036.31, 8036.31, 8036.31, 8036.31, 8036.31, 8036.31, 8036.31, 8036.31, 8036.31, 8036.31, 8036.31, 8036.31]
# SEED 2
ts2 = [7924.04, 7955.27, 7967.46, 7967.46, 7967.46, 7969.94, 7969.94, 7971.27, 7971.27, 7971.98, 7971.98, 7971.98, 7972.36, 7972.36, 7972.36, 7972.36, 7972.36, 7972.36, 7972.36, 7972.36]
# SEED 1
grasp1 = [7719.83, 7719.83, 7726.23, 7726.23, 7726.23, 7726.23, 7732.15, 7732.15, 7762.62, 7762.62, 7762.62, 7762.62, 7762.62, 7762.62, 7762.62, 7762.62, 7762.62, 7762.62, 7762.62, 7762.62]
# SEED 2
grasp2 = [7682.76, 7713.99, 7713.99, 7713.99, 7713.99, 7713.99, 7730.55, 7730.55, 7730.55, 7730.55, 7730.55, 7730.55, 7730.55, 7730.55, 7730.55, 7730.55, 7730.55, 7730.55, 7730.55, 7730.55]

plt.figure(figsize=(9.5, 3.7), dpi=200) 
plt.grid(True, axis='y', linestyle='--', linewidth=0.5)
plt.plot(time, ts1, marker='d', color='blue', label='TS 1', linestyle='--', linewidth=1)
plt.plot(time, ts2, marker='D', color='magenta', label='TS 2', linestyle='--', linewidth=1)
plt.plot(time, grasp1, marker='+', color='green', label='GRASP 1', linestyle='--', linewidth=1)
plt.plot(time, grasp2, marker='x', color='red', label='GRASP 2', linestyle='--', linewidth=1)
plt.xlabel("Time (in seconds)")
plt.ylabel("Objective Function value")
plt.title("Evolution of the algorithms at long executions")
plt.legend(fontsize=10, loc='upper left', ncol=2)

plt.tight_layout()
plt.show()

