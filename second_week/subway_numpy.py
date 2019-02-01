import numpy as np


def mean_riders_for_max_station(ridership):
    overall_mean = None  # Replace this with your code
    mean_for_max = None  # Replace this with your code

    return (overall_mean, mean_for_max)


# Subway ridership for 5 stations on 10 different days
ridership = np.array([
    [0, 0, 2, 5, 0],
    [1478, 3877, 3674, 2328, 2539],
    [1613, 4088, 3991, 6461, 2691],
    [1560, 3392, 3826, 4787, 2613],
    [1608, 4802, 3932, 4477, 2705],
    [1576, 3933, 3909, 4979, 2685],
    [95, 229, 255, 496, 201],
    [2, 0, 1, 27, 0],
    [1438, 3785, 3589, 4174, 2215],
    [1342, 4043, 4009, 4665, 3033]
])

print(ridership[1, 3])
print(ridership[1:3, 3:5])
print(ridership[1, :])
print(ridership[0, :] + ridership[1, :])
print(ridership[:, 0] + ridership[:, 1])

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = np.array([[1, 1, 1], [2, 2, 2], [3, 3, 3]])

print(a + b)
