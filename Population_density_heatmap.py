import numpy as np
import matplotlib.pyplot as plt

# Generate sample population density data
np.random.seed(0)
population_density = np.random.poisson(lam=10, size=(10, 10))


plt.figure(figsize=(8, 6))
plt.imshow(population_density, cmap='hot', interpolation='nearest')
plt.colorbar(label='Population Density')
plt.title('Population Density Heatmap')
plt.show()
