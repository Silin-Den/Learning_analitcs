import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

sns.set(rc={'figure.figsize': (14, 8)}, style='whitegrid')

sample_size = 10000
sigma = 10
mu = 100

population = np.random.normal(mu, sigma, sample_size)
sns.displot(population, kde=False)
plt.show()
