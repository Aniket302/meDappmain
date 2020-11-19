import matplotlib.pyplot as plt
import numpy as np
import random

meandarr = []
normaldarr = []
poissondarr = []
meand = np.random.exponential(5, size = 2000)

normald = np.random.normal(5, size = 2000)

poissond = np.random.poisson(5, size = 2000)

for i in range (1000):
  meandarr.append(np.mean(random.choices(meand, k = 20)))

  normaldarr.append(np.mean(random.choices(normald, k = 20)))

  poissondarr.append(np.mean(random.choices(poissond, k = 20)))

plt.title("Exponential")
plt.hist(meandarr)
plt.show()
plt.title("Normal")
plt.hist(normaldarr)
plt.show()
plt.title("Poisson")
plt.hist(poissondarr)
plt.show()

