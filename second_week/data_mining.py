import unicodecsv
from datetime import datetime


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


enrollments = read_csv('dataset/enrollments.csv')
daily_engagement = read_csv('dataset/daily_engagement.csv')
project_submissions = read_csv('dataset/project_submissions.csv')

keys_enrollment = []
for enrollment in enrollments:
    enrollment['cancel_date'] = parse_date(enrollment['cancel_date'])
    enrollment['days_to_cancel'] = parse_maybe_int(enrollment['days_to_cancel'])
    enrollment['is_canceled'] = enrollment['is_canceled'] == 'True'
    enrollment['is_udacity'] = enrollment['is_udacity'] == 'True'
    enrollment['join_date'] = parse_date(enrollment['join_date'])
    if enrollment['account_key'] not in keys_enrollment:
        keys_enrollment.append(enrollment['account_key'])


keys_daily_engagement = []
for engagement_record in daily_engagement:
    engagement_record['lessons_completed'] = int(float(engagement_record['lessons_completed']))
    engagement_record['num_courses_visited'] = int(float(engagement_record['num_courses_visited']))
    engagement_record['projects_completed'] = int(float(engagement_record['projects_completed']))
    engagement_record['total_minutes_visited'] = float(engagement_record['total_minutes_visited'])
    engagement_record['utc_date'] = parse_date(engagement_record['utc_date'])
    if engagement_record['acct'] not in keys_daily_engagement:
        keys_daily_engagement.append(engagement_record['acct'])

keys_project_submissions = []
for submission in project_submissions:
    submission['completion_date'] = parse_date(submission['completion_date'])
    submission['creation_date'] = parse_date(submission['creation_date'])
    if (submission['account_key'], submission['lesson_key']) not in keys_project_submissions:
        keys_project_submissions.append((submission['account_key'], submission['lesson_key']))

enrollment_num_rows = len(enrollments)
engagement_num_rows = len(daily_engagement)
submission_num_rows = len(project_submissions)

enrollment_num_unique_students = len(keys_enrollment)
engagement_num_unique_students = len(keys_daily_engagement)
submission_num_unique_students = len(keys_project_submissions)

print('For table enrollments, exists', enrollment_num_rows,
      'and', enrollment_num_unique_students, 'primary key.')

print('For table daily_engagement, exists', engagement_num_rows,
      'and', engagement_num_unique_students, 'primary key.')

print('For table project_submissions, exists', submission_num_rows,
      'and', submission_num_unique_students, 'primary key.')