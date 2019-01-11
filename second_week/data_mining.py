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
    result = []
    for row in list(archive):
        row_dict = dict(row)
        row_dict.update({'account_key': row_dict['acct']})
        del[row_dict['acct']]
        result.append(row_dict)
    return result


def remove_trial_students(data, paid_students):
    new_data = []
    for data_element in data:
        if data_element['account_key'] in paid_students:
            new_data.append(data_element)

    return  new_data


enrollments = read_csv('dataset/enrollments.csv')
daily_engagement = read_csv('dataset/daily_engagement.csv')
project_submissions = read_csv('dataset/project_submissions.csv')
daily_engagement = change_column_acct(daily_engagement)

enrollments_unique_keys = set()
enrollments_aux = []
enrollments_remove = []
for enrollment in enrollments:
    if enrollment['is_udacity'] != 'True':
        enrollment['cancel_date'] = parse_date(enrollment['cancel_date'])
        enrollment['days_to_cancel'] = parse_maybe_int(enrollment['days_to_cancel'])
        enrollment['is_canceled'] = enrollment['is_canceled'] == 'True'
        enrollment['join_date'] = parse_date(enrollment['join_date'])
        enrollments_unique_keys.add(enrollment['account_key'])
        enrollments_aux.append(enrollment)
    else:
        enrollments_remove.append(enrollment['account_key'])

enrollments = enrollments_aux

engagement_unique_key = set()
daily_engagement_aux = []
for engagement in daily_engagement:
    if engagement['account_key'] not in enrollments_remove:
        engagement['lessons_completed'] = int(float(engagement['lessons_completed']))
        engagement['num_courses_visited'] = int(float(engagement['num_courses_visited']))
        engagement['projects_completed'] = int(float(engagement['projects_completed']))
        engagement['total_minutes_visited'] = float(engagement['total_minutes_visited'])
        engagement['utc_date'] = parse_date(engagement['utc_date'])
        engagement_unique_key.add(engagement['account_key'])
        daily_engagement_aux.append(engagement)

daily_engagement = daily_engagement_aux

submissions_unique_key = set()
project_submissions_aux = []
for submission in project_submissions:
    if submission['account_key'] not in enrollments_remove:
        submission['completion_date'] = parse_date(submission['completion_date'])
        submission['creation_date'] = parse_date(submission['creation_date'])
        submissions_unique_key.add(submission['account_key'])
        project_submissions_aux.append(submission)

project_submissions = project_submissions_aux

print('For table enrollments, exists', len(enrollments),
      'and', len(enrollments_unique_keys), 'primary key.')

print('For table daily_engagement, exists', len(daily_engagement),
      'and', len(engagement_unique_key), 'primary key.')

print('For table project_submissions, exists', len(project_submissions),
      'and', len(submissions_unique_key), 'primary key.')

paid_students = {}
for enrollment in enrollments:
    if not enrollment['is_canceled'] or enrollment['days_to_cancel'] > 7:
        account_key = enrollment['account_key']
        enrollment_date = enrollment['join_date']
        paid_students[account_key] = enrollment_date

        if account_key not in paid_students or \
                enrollment_date > paid_students[account_key]:
            paid_students[account_key] = enrollment_date

paid_enrollments = remove_trial_students(enrollments, paid_students)
paid_project_submissions = remove_trial_students(project_submissions, paid_students)
paid_daily_engagement = remove_trial_students(daily_engagement, paid_students)

print('Exists', len(paid_students), 'paid students.')
print('For table enrollments, exists', len(paid_enrollments), 'for paid students.')
print('For table daily_engagement, exists', len(paid_project_submissions), 'for paid students.')
print('For table project_submissions, exists', len(paid_daily_engagement), 'for paid students.')

paid_students_first_week = []
for engagement in paid_daily_engagement:
    account_key = engagement['account_key']
    join_date = paid_students[account_key]
    engagement_record_date = engagement['utc_date']
    days_current_project = engagement_record_date - join_date

    if 0 <= days_current_project.days < 7:
        paid_students_first_week.append(engagement)

print('Exists', len(paid_students_first_week), 'student finally project in one week.')

engagement_by_account = defaultdict(list)
for engagement_record in paid_students_first_week:
    account_key = engagement_record['account_key']
    engagement_by_account[account_key].append(engagement_record)

total_minutes_by_account = {}
for account_key, engagement_for_student in engagement_by_account.items():
    total_minutes = 0
    for engagement_record in engagement_for_student:
        total_minutes += engagement_record['total_minutes_visited']
    total_minutes_by_account[account_key] = total_minutes

total_minutes = total_minutes_by_account.values()
print(total_minutes)

print('Mean:', np.mean(total_minutes))
'''
print('Standard deviation:', np.mean(total_minutes))
print('Minimum:', np.mean(total_minutes))
print('Maximum:', np.mean(total_minutes))
'''