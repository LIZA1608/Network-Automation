import matplotlib.pyplot as plt
# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Create a new figure
plt.figure()
# Plot the data as a stem plot
plt.stem(x, y, linefmt='-k', markerfmt='ko', basefmt=' ')

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Stem Plot')

# Add grid
plt.grid(True)

# Show the plot
plt.show()
