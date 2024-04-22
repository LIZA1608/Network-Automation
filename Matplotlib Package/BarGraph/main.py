import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Create a new figure
plt.figure()

# Plot the data as a bar chart
plt.bar(x, y)

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Bar Chart')

# Show the plot
plt.show()
