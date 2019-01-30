import numpy as np

'''
1- study countrys and genere completition
'''


def overall_completion_rate(female, male):
    return (female + male) / 2


countries_completion = np.array([
    'Algeria', 'Argentina', 'Armenia', 'Aruba', 'Austria', 'Azerbaijan',
    'Bahamas', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Bolivia',
    'Botswana', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi',
    'Cambodia', 'Cameroon', 'Cape Verde'
])

female_completion = np.array([
    97.35583, 104.62379, 103.02998, 95.14321, 103.69019,
    98.49185, 100.88828, 95.43974, 92.11484, 91.54804,
    95.98029, 98.22902, 96.12179, 119.28105, 97.84627,
    29.07386, 38.41644, 90.70509, 51.7478, 95.45072
])

male_completion = np.array([
    95.47622, 100.66476, 99.7926, 91.48936, 103.22096,
    97.80458, 103.81398, 88.11736, 93.55611, 87.76347,
    102.45714, 98.73953, 92.22388, 115.3892, 98.70502,
    37.00692, 45.39401, 91.22084, 62.42028, 90.66958
])


sum_completion = overall_completion_rate(female_completion, male_completion)
for i in range(len(countries_completion)):
    print('Country {} sum_completion {}'.format(countries_completion[i], sum_completion[i]))
print('\n')


'''
2- study normalization
'''


def standardize_data(values):
    standardize_values = (values - values.mean()) / values.std()
    return standardize_values


countries_employment = np.array([
    'Afghanistan', 'Albania', 'Algeria', 'Angola', 'Argentina',
    'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas',
    'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium',
    'Belize', 'Benin', 'Bhutan', 'Bolivia',
    'Bosnia and Herzegovina'
])

employment = np.array([
    55.70000076,  51.40000153,  50.5       ,  75.69999695,
    58.40000153,  40.09999847,  61.5       ,  57.09999847,
    60.90000153,  66.59999847,  60.40000153,  68.09999847,
    66.90000153,  53.40000153,  48.59999847,  56.79999924,
    71.59999847,  58.40000153,  70.40000153,  41.20000076
])

standardize = standardize_data(employment)
for i in range(len(countries_employment)):
    print('Country {} standardize {}'.format(countries_employment[i], standardize[i]))
print('\n')


'''
3- study index array 
'''


def mean_time_for_paid_students(time_spent, days_to_cancel):
    index = (days_to_cancel >= 7)
    print(index)
    print(time_spent[index])
    return np.mean(time_spent[index])


time_spent = np.array([
       12.89697233,    0.        ,   64.55043217,    0.        ,
       24.2315615 ,   39.991625  ,    0.        ,    0.        ,
      147.20683783,    0.        ,    0.        ,    0.        ,
       45.18261617,  157.60454283,  133.2434615 ,   52.85000767,
        0.        ,   54.9204785 ,   26.78142417,    0.
])

days_to_cancel = np.array([
      4,   5,  37,   3,  12,   4,  35,  38,   5,  37,   3,   3,  68,
     38,  98,   2, 249,   2, 127,  35
])

standardize = standardize_data(employment)
print('Mean {}'.format(mean_time_for_paid_students(time_spent, days_to_cancel)))