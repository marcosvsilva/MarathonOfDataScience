import pandas as pd


def correlation(x, y):
    std_x = (x - x.mean()) / x.std(ddof=0)
    std_y = (y - y.mean()) / y.std(ddof=0)
    return (std_x * std_y).mean()


def get_hourly_entries_and_exists(entries_and_exists):
    return entries_and_exists - entries_and_exists.shift(1)

entries_and_exists = pd.DataFrame({
    'ENTRIESn': [3144312, 3144335, 3144353, 3144424, 3144594,
                 3144808, 3144895, 3144905, 3144941, 3145094],
    'EXITSn': [1088151, 1088159, 1088177, 1088231, 1088275,
               1088317, 1088328, 1088331, 1088420, 1088753]
})

csv_directory = '../dataset/nyc_subway_weather.csv'
subway_weather = pd.read_csv(csv_directory)

correlation_entries_anpressurei = correlation(subway_weather['ENTRIESn_hourly'], subway_weather['meanpressurei'])
print(correlation_entries_anpressurei)
print('\n')

correlation_entries_entries = correlation(subway_weather['ENTRIESn_hourly'], subway_weather['ENTRIESn'])
print(correlation_entries_entries)
print('\n')

entries_and_exists = get_hourly_entries_and_exists(entries_and_exists)
print(entries_and_exists)