import numpy as np

# Define the slice thickness (cm)
delta_x = 0.15

# Number of slices
N = int(9 / delta_x)

# Generate midpoints for each slice
x_values = np.array([(i + 0.5) * delta_x for i in range(N)])

# Calculate the side lengths at each x
side_lengths = -1/9 * x_values**2 + 9

# Calculate the area of each square cross section
areas = side_lengths**2

# Approximate the total volume by summing the volumes of all slices
V_approx = np.sum(areas * delta_x)
print("Approximate volume (cm^3):", V_approx)