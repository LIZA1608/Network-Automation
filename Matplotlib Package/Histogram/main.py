import matplotlib.pyplot as plt

# Sample data
data = [1, 1, 2, 3, 3, 3, 4, 4, 5, 5, 5, 5, 6, 6, 6]

# Create a new figure
plt.figure()

# Plot the data as a histogram
plt.hist(data, bins=5, edgecolor='black')

# Add labels and title
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Histogram')

# Show the plot
plt.show()
