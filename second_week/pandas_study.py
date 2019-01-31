import pandas as pd
import numpy as np

'''
1. Countrys above and below the avarage
'''

countries = ['Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda',
             'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan',
             'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus',
             'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia']

life_expectancy_values = [74.7,  75. ,  83.4,  57.6,  74.6,  75.4,  72.3,  81.5,  80.2,
                          70.3,  72.1,  76.4,  68.1,  75.2,  69.8,  79.4,  70.8,  62.7,
                          67.3,  70.6]

gdp_values = [ 1681.61390973,   2155.48523109,  21495.80508273,    562.98768478,
               13495.1274663,   9388.68852258,   1424.19056199,  24765.54890176,
              27036.48733192,   1945.63754911,  21721.61840978,  13373.21993972,
                483.97086804,   9783.98417323,   2253.46411147,  25034.66692293,
               3680.91642923,    366.04496652,   1175.92638695,   1132.21387981]


def variable_correlation(variable1, variable2):
    variable1 = pd.Series(variable1)
    variable2 = pd.Series(variable2)

    above = (variable1 > variable1.mean()) & (variable2 > variable2.mean())
    below = (variable1 < variable1.mean()) & (variable2 < variable2.mean())
    some_directions = above | below
    num_same_direction = some_directions.sum()
    num_different_direction = len(variable1) - num_same_direction

    return num_same_direction, num_different_direction


above_mean, below_mean = variable_correlation(life_expectancy_values, gdp_values)
print("Exists {} values correlations above or below mean and {} values not correlations".format(above_mean, below_mean))
print('\n')