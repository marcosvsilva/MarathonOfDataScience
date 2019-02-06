import numpy as np


def mean_riders_for_max_station(ridership):
    max_station = ridership[0, :].argmax()
    mean_for_max = ridership[:, max_station].mean()
    overall_mean = ridership.mean()
    return overall_mean, mean_for_max


def min_and_max_riders_per_day(ridership):
    station_riders = ridership.mean(axis=0)
    max_daily_ridership = station_riders.max()
    min_daily_ridership = station_riders.min()
    return max_daily_ridership, min_daily_ridership

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

overall_mean, mean_for_max = mean_riders_for_max_station(ridership)
print('The subway station in New York receives average of {} people'
      'from a total of {} people in five stations.'.format(int(overall_mean), int(mean_for_max)))

max_daily_ridership, min_daily_ridership = min_and_max_riders_per_day(ridership)
print('The average number of people at the metro station was between {} and '
      '{}'.format(int(max_daily_ridership), int(min_daily_ridership)))

