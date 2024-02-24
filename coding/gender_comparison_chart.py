# filename: gender_comparison_chart.py
import matplotlib.pyplot as plt

# Estimated population data (source: World Bank)
population_data = {
    'Males': 3500000000,
    'Females': 3500000000,
}

# Create the chart
fig, ax = plt.subplots()
ax.bar(population_data.keys(), population_data.values())

# Add labels and title
ax.set_xlabel('Gender')
ax.set_ylabel('Number of Individuals')
ax.set_title('Comparison of Male and Female Population on Earth')

# Display the chart
plt.show()