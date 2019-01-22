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


def change_column_acct(archive):
    for row in archive:
        row['account_key'] = row['acct']
        del[row['acct']]
    return archive


def remove_trial_students(data, paid_students):
    new_data = []
    for data_element in data:
        if data_element['account_key'] in paid_students:
            new_data.append(data_element)

    return  new_data


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