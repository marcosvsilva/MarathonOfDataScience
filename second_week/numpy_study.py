import numpy as np

# First 20 countries with school completion data
countries_completion = np.array([
    'Algeria', 'Argentina', 'Armenia', 'Aruba', 'Austria', 'Azerbaijan',
    'Bahamas', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Bolivia',
    'Botswana', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi',
    'Cambodia', 'Cameroon', 'Cape Verde'
])

# First 20 countries with employment data
countries_employment = np.array([
    'Afghanistan', 'Albania', 'Algeria', 'Angola', 'Argentina',
    'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas',
    'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium',
    'Belize', 'Benin', 'Bhutan', 'Bolivia',
    'Bosnia and Herzegovina'
])

# Female school completion rate in 2007 for those 20 countries
female_completion = np.array([
    97.35583, 104.62379, 103.02998, 95.14321, 103.69019,
    98.49185, 100.88828, 95.43974, 92.11484, 91.54804,
    95.98029, 98.22902, 96.12179, 119.28105, 97.84627,
    29.07386, 38.41644, 90.70509, 51.7478, 95.45072
])

# Male school completion rate in 2007 for those 20 countries
male_completion = np.array([
    95.47622, 100.66476, 99.7926, 91.48936, 103.22096,
    97.80458, 103.81398, 88.11736, 93.55611, 87.76347,
    102.45714, 98.73953, 92.22388, 115.3892, 98.70502,
    37.00692, 45.39401, 91.22084, 62.42028, 90.66958
])

employment = np.array([
    55.70000076,  51.40000153,  50.5       ,  75.69999695,
    58.40000153,  40.09999847,  61.5       ,  57.09999847,
    60.90000153,  66.59999847,  60.40000153,  68.09999847,
    66.90000153,  53.40000153,  48.59999847,  56.79999924,
    71.59999847,  58.40000153,  70.40000153,  41.20000076
])


def overall_completion_rate(female, male):
    return (female + male) / 2

def standardize_data(values):
    standardize_values = (values - values.mean()) / values.std()
    return standardize_values


sum_completion = overall_completion_rate(female_completion, male_completion)
for i in range(len(countries_completion)):
    print('Country {} sum_completion {}'.format(countries_completion[i], sum_completion[i]))

print('\n')
standardize = standardize_data(employment)
for i in range(len(countries_employment)):
    print('Country {} sum_completion {}'.format(countries_employment[i], standardize[i]))