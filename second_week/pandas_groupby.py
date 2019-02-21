import pandas as pd
import matplotlib
matplotlib.use("wxAgg")
import matplotlib.pyplot as plt

filename = 'dataset/nyc_subway_weather.csv'
subway_df = pd.read_csv(filename)

rideship_by_day = subway_df.groupby('day_week').mean()['ENTRIESn_hourly']

print(rideship_by_day)
plt.plot(rideship_by_day)
plt.show()