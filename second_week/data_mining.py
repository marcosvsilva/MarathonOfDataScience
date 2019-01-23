import unicodecsv
import numpy as np
from datetime import datetime
from collections import defaultdict


def read_csv(archive):
    with open(archive, 'rb') as arq:
        reader = unicodecsv.DictReader(arq)
        result = []
        for line in reader:
            result.append(line)

        return result


def parse_date(date):
    result = None
    try:
        if date != '':
            result = datetime.strptime(date, '%Y-%m-%d')
    except:
        result = None
    return result


def parse_maybe_int(number):
    result = None
    try:
        if number != '':
            result = int(number)
    except:
        result = None

    return result


def change_column_acct(data):
    for data_element in data:
        data_element['account_key'] = data_element['acct']
        del[data_element['acct']]
    return data


def remove_udacity_accounts(data, udacity_accounts):
    new_data = []
    for data_element in data:
        if data_element['account_key'] not in udacity_accounts:
            new_data.append(data_element)
    return new_data


def remove_trial_accounts(data, paid_accounts):
    new_data = []
    for data_element in data:
        if data_element['account_key'] in paid_accounts:
            new_data.append(data_element)
    return new_data


''' 
Read CSV
Normalize keys
'''

enrollments = read_csv('dataset/enrollments.csv')
daily_engagement = read_csv('dataset/daily_engagement.csv')
project_submissions = read_csv('dataset/project_submissions.csv')
daily_engagement = change_column_acct(daily_engagement)

''' 
Convert types
'''

for enrollment in enrollments:
    enrollment['cancel_date'] = parse_date(enrollment['cancel_date'])
    enrollment['days_to_cancel'] = parse_maybe_int(enrollment['days_to_cancel'])
    enrollment['is_canceled'] = enrollment['is_canceled'] == 'True'
    enrollment['join_date'] = parse_date(enrollment['join_date'])

for engagement in daily_engagement:
    engagement['lessons_completed'] = int(float(engagement['lessons_completed']))
    engagement['num_courses_visited'] = int(float(engagement['num_courses_visited']))
    engagement['projects_completed'] = int(float(engagement['projects_completed']))
    engagement['total_minutes_visited'] = float(engagement['total_minutes_visited'])
    engagement['utc_date'] = parse_date(engagement['utc_date'])

for submission in project_submissions:
    submission['completion_date'] = parse_date(submission['completion_date'])
    submission['creation_date'] = parse_date(submission['creation_date'])

'''
Extract unique enrollment
'''

unique_enrollments = set()
for enrollment in enrollments:
    unique_enrollments.add(enrollment['account_key'])

unique_engagements = set()
for engagement in daily_engagement:
    unique_engagements.add(engagement['account_key'])

unique_submission = set()
for submission in project_submissions:
    unique_submission.add(submission['account_key'])

'''
1. How many students are enrolled but do not have any work days?
'''

numbers_of_records = 0
for unique_enrollment in unique_enrollments:
    if unique_enrollment not in unique_engagements:
        numbers_of_records += 1

print('\n')
print("1. How many students are enrolled but do not have any work days?")
print(numbers_of_records, "enrollments.")

'''
2. How many students are enrolled at least a day, but do not have any work days?
'''

numbers_of_records = 0
for enrollment in enrollments:
    if enrollment['cancel_date'] != enrollment['join_date']:
        if enrollment['account_key'] not in unique_engagements:
            numbers_of_records += 1

print('\n')
print("2. How many students are enrolled at least a day, but do not have any work days?")
print(numbers_of_records, 'enrollments.')

'''
3. Remove udacity test accounts from datasets
'''

enrollments_udacity = set()
for enrollment in enrollments:
    if enrollment['is_udacity'] == 'True':
        enrollments_udacity.add(enrollment['account_key'])

enrollments = remove_udacity_accounts(enrollments, enrollments_udacity)
daily_engagement = remove_udacity_accounts(daily_engagement, enrollments_udacity)
project_submissions = remove_udacity_accounts(project_submissions, enrollments_udacity)

print('\n')
print('3. How many registrations are left after removing all udacity test accounts?')
print('Enrollments: ', len(enrollments))
print('Daily engagement: ', len(daily_engagement))
print('Project submissions: ', len(project_submissions))

'''
4. How many students have passed the free test and are still working?
'''

paid_students = {}
for enrollment in enrollments:
    join_data = enrollment['join_date']
    account_key = enrollment['account_key']
    days_to_cancel = enrollment['days_to_cancel']
    canceled = enrollment['is_canceled']

    if (not canceled) or ((days_to_cancel is not None) and (days_to_cancel > 7)):
        if (account_key not in paid_students) or (paid_students[account_key] < join_data):
            paid_students[account_key] = join_data

print('\n')
print('4. How many students have passed the free test and are still working?')
print(len(paid_students), 'students.')

'''
5. How many students worked for one week after enrollment
'''

enrollments_paid = remove_trial_accounts(enrollments, paid_students)
daily_engagement_paid = remove_trial_accounts(daily_engagement, paid_students)
project_submissions_paid = remove_trial_accounts(project_submissions, paid_students)

paid_engagement_in_first_week = []
for engagement in daily_engagement_paid:
    account_key = engagement['account_key']
    utc_date = engagement['utc_date']

    if account_key in paid_students:
        if utc_date is not None:
            if (utc_date - paid_students[account_key]).days < 7:
                paid_engagement_in_first_week.append(engagement)

print('\n')
print('5. How many students worked for one week after enrollment?')
print(len(paid_engagement_in_first_week), 'students.')

'''
7. Calculate the average time spent for each student in the first week.
'''

engagement_by_account = defaultdict(list)
for engagement in paid_engagement_in_first_week:
    account_key = engagement['account_key']
    engagement_by_account[account_key].append(engagement)

total_minutes_by_account = {}
for account_key, engagement_list in engagement_by_account.items():
    total_minutes = 0
    for engagement in engagement_list:
        total_minutes += engagement['total_minutes_visited']
    total_minutes_by_account[account_key] = total_minutes

total_minutes = list(total_minutes_by_account.values())

print('\n')
print('7. Average time spent in one week of studies')
print('Mean:', np.mean(total_minutes))
print('Standard deviation:', np.std(total_minutes, axis=0))
print('Maximum:', np.max(total_minutes))
print('Minimum:', np.min(total_minutes))