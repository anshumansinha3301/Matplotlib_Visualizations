import numpy as np
import matplotlib.pyplot as plt

 
years = np.arange(1900, 2024)
temperatures = np.random.normal(loc=15, scale=5, size=len(years))

# Plot temperature changes over time
plt.figure(figsize=(10, 6))
plt.plot(years, temperatures, label='Global Temperature')
plt.xlabel('Year')
plt.ylabel('Temperature (°C)')
plt.title('Global Temperature Changes (1900-2023)')
plt.legend()
plt.show()
