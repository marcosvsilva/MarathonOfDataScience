import pandas as pd


def standardize(df):
    df_diffs = df.sub(df.mean(axis='columns'), axis='index')
    return df_diffs.div(df.std(axis='columns'), axis='index')

serie = pd.Series([1, 2, 3, 4])

data_frame = pd.DataFrame({
    0: [10, 20, 30, 40],
    1: [50, 60, 70, 80],
    2: [90, 100, 110, 120],
    3: [130, 140, 150, 160]
})

print(data_frame)
print(standardize(data_frame))