import pandas as pd

'''
1. Countrys above and below the correlation
'''


def variable_correlation(variable1, variable2):
    above = (variable1 > variable1.mean()) & (variable2 > variable2.mean())
    below = (variable1 < variable1.mean()) & (variable2 < variable2.mean())
    num_same_direction = (above | below).sum()
    return num_same_direction, len(variable1) - num_same_direction


countries = pd.Series([
    'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda',
    'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan',
    'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus',
    'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia'
])

life_expectancy_values = pd.Series([
    74.7,  75.,  83.4,  57.6,  74.6,  75.4,  72.3,  81.5,  80.2,
    70.3,  72.1,  76.4,  68.1,  75.2,  69.8,  79.4,  70.8,  62.7,
    67.3,  70.6
])

gdp_values = pd.Series([
    1681.61390973,   2155.48523109,  21495.80508273,    562.98768478,
    13495.1274663,   9388.68852258,   1424.19056199,  24765.54890176,
    27036.48733192,   1945.63754911,  21721.61840978,  13373.21993972,
    483.97086804,   9783.98417323,   2253.46411147,  25034.66692293,
    3680.91642923,    366.04496652,   1175.92638695,   1132.21387981
])

above_mean, below_mean = variable_correlation(life_expectancy_values, gdp_values)
print("Exists {} values correlations above or below mean and {} values not correlations".format(above_mean, below_mean))
print('\n')


'''
2. Max employment for countries
'''


def max_employment(employment):
    max_country = employment.idxmax()
    max_value = employment.max()
    return max_country, max_value


countries = ([
    'Afghanistan', 'Albania', 'Algeria', 'Angola',
    'Argentina', 'Armenia', 'Australia', 'Austria',
    'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh',
    'Barbados', 'Belarus', 'Belgium', 'Belize',
    'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina'
])

employment_values = ([
    55.70000076, 51.40000153, 50.5, 75.69999695,
    58.40000153, 40.09999847, 61.5, 57.09999847,
    60.90000153, 66.59999847, 60.40000153, 68.09999847,
    66.90000153, 53.40000153, 48.59999847, 56.79999924,
    71.59999847, 58.40000153, 70.40000153, 41.20000076
])

employment = pd.Series(employment_values, index=countries)
country, value = max_employment(employment)
print('The country with the highest salary and {} with a salary of {}'.format(country, value))
print('\n')


'''
3. Teste seires index pandas
'''

serie1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
serie2 = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
print(serie1 + serie2)
print('\n')

serie1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
serie2 = pd.Series([10, 20, 30, 40], index=['d', 'c', 'b', 'a'])
print(serie1 + serie2)
print('\n')

serie1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
serie2 = pd.Series([10, 20, 30, 40], index=['c', 'd', 'e', 'f'])
print(serie1 + serie2)
print('\n')
print((serie1 + serie2).dropna())
print('\n')

serie1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
serie2 = pd.Series([10, 20, 30, 40], index=['e', 'f', 'g', 'h'])
print(serie1 + serie2)
print('\n')

serie1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
serie2 = pd.Series([10, 20, 30, 40], index=['c', 'd', 'e', 'f'])
print(serie1.add(serie2, fill_value=0))
print('\n')

'''
3. converting a list of full names to last name, first name
'''


def reverse_names(name):
    name = str(name)
    name_reverse = None
    full_name = name.split()
    if len(full_name) == 2:
        name_reverse = '{}, {}'.format(full_name[1], full_name[0])
    return name_reverse


names = pd.Series([
    'Andre Agassi', 'Barry Bonds', 'Christopher Columbus', 'Daniel Defoe',
    'Emilio Estevez', 'Fred Flintstone', 'Greta Garbo', 'Humbert Humbert',
    'Ivan Ilych', 'James Joyce', 'Keira Knightley', 'Lois Lane', 'Mike Myers',
    'Nick Nolte', 'Ozzy Osbourne', 'Pablo Picasso', 'Quirinus Quirrell', 'Rachael Ray',
    'Susan Sarandon', 'Tina Turner', 'Ugueth Urbina', 'Vince Vaughn', 'Woodrow Wilson',
    'Yoji Yamada', 'Zinedine Zidane'
])

names_reverse = names.apply(reverse_names)
print(names_reverse)