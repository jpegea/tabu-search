from matplotlib import pyplot as plt
import numpy as np

time = [5 * (i + 1) for i in range(20)]
# SEED 1
ts_random_f = [7757.43, 7784.8, 7787.84, 7787.84, 7787.84, 7789.15, 7807.6, 7824.68, 7825.51, 7842.71, 7862.93, 7884.33, 7884.33, 7889.29, 7889.29, 7897.46, 7897.46, 7901.44, 7901.44, 7901.44]
# SEED 1
ts_random_b = [7737.33, 7752.3, 7752.3, 7762.49, 7865.84, 7865.84, 7867.07, 7867.07, 7867.07, 7867.07, 7867.07, 7867.07, 7867.07, 7867.07, 7867.07, 7867.07, 7867.07, 7867.07, 7867.07, 7867.07]
# SEED 1
ts_greedy_f = [7702.92, 7702.92, 7708.13, 7715.1, 7747.33, 7747.52, 7764.41, 7770.51, 7770.51, 7770.51, 7770.51, 7770.51, 7770.51, 7770.51, 7770.51, 7770.51, 7770.51, 7770.51, 7770.51, 7770.51]
# SEED 1
ts_greedy_b = [7667.92, 7668.15, 7668.15, 7672.97, 7676.82, 7679.86, 7692.12, 7692.12, 7692.12, 7719.45, 7721.9, 7724.17, 7724.17, 7724.17, 7724.17, 7724.17, 7724.17, 7724.17, 7724.17, 7724.17]

plt.figure(figsize=(9.5, 4.5), dpi=200) 
plt.grid(True, axis='y', linestyle='--', linewidth=0.5)
plt.plot(time, ts_random_f, marker='d', color='blue', label='TS random + tsfirstimp', linestyle='--', linewidth=1)
plt.plot(time, ts_random_b, marker='+', color='magenta', label='TS random + tsbestimp', linestyle='--', linewidth=1)
plt.plot(time, ts_greedy_f, marker='P', color='green', label='TS greedy + tsfirstimp', linestyle='--', linewidth=1)
plt.plot(time, ts_greedy_b, marker='x', color='red', label='TS greedy + tsbestimp', linestyle='--', linewidth=1)
plt.xlabel("Time (in seconds)")
plt.ylabel("Objective Function value")
plt.title("Evolution of the best solution found over time")
plt.legend(fontsize=10, loc='upper left', ncol=2)

plt.tight_layout()
plt.show()

