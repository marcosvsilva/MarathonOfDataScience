import pandas as pd


def convert_grades(grade):
    if grade >= 90:
        return 'A'
    elif 80 <= grade < 90:
        return 'B'
    elif 70 <= grade < 80:
        return 'C'
    elif 60 <= grade < 70:
        return 'D'
    elif grade < 60:
        return 'F'


def standardize_column(column):
    return (column - column.mean()) / column.std()


def standardize(df):
    return df.apply(standardize_column)


def second_max_value(column):
    second_column = column.sort_values(by=column.keys()[0], ascending=False)
    return second_column.iloc[1]


def second_largest(df):
    return df.apply(second_max_value)


grades_df = pd.DataFrame(
    data={'exam1': [43, 81, 78, 75, 89, 70, 91, 65, 98, 87],
          'exam2': [24, 63, 56, 56, 67, 51, 79, 46, 72, 60]},
    index=['Andre', 'Barry', 'Chris', 'Dan', 'Emilio',
           'Fred', 'Greta', 'Humbert', 'Ivan', 'James']
)

grades_convert = grades_df.applymap(convert_grades)
print(grades_convert)
print('\n')

grades_df_normatize = standardize(grades_df)
print(grades_df_normatize)
print('\n')

grades_df_second_max = second_max_value(grades_df)
print(grades_df_second_max)