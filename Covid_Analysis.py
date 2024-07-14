import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load COVID-19 data
url = 'https://raw.githubusercontent.com/datasets/covid-19/main/data/countries-aggregated.csv'
data = pd.read_csv(url)
data['Date'] = pd.to_datetime(data['Date'])
country_data = data[data['Country'] == 'India']

# Plot daily cases, recoveries, and deaths
plt.figure(figsize=(10, 6))
plt.plot(country_data['Date'], country_data['Confirmed'], label='Confirmed')
plt.plot(country_data['Date'], country_data['Recovered'], label='Recovered')
plt.plot(country_data['Date'], country_data['Deaths'], label='Deaths')
plt.xlabel('Date')
plt.ylabel('Number of Cases')
plt.title('COVID-19 Data for India')
plt.legend()
plt.show()
