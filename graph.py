import matplotlib.pyplot as plt

# Sample data (replace this with your actual data)
years = [2004, 2006, 2008, 2010, 2012, 2014, 2016, 2018, 2020, 2022, 2024]
collisions = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]

# Plotting the data
plt.figure(figsize=(10, 6))
plt.plot(years, collisions, marker='o', linestyle='-')

# Adding labels and title
plt.title('Kessler Syndrome: Space Collisions Over Two Decades (2004-2024)')
plt.xlabel('Year')
plt.ylabel('Number of Collisions')

# Displaying the grid
plt.grid(True)

# Show plot
plt.show()
