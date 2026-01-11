import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])

m, c = np.polyfit(x, y, 1)
print(f"Equation of best-fit line: y = {m:.2f}x + {c:.2f}")
