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

def change_column_acct(archive):
    result = []
    for row in list(archive):
        row_dict = dict(row)
        row_dict.update(dict(account_key=row_dict['acct']))
        del[row_dict['acct']]
        result.append(row_dict)
    return result

def remove_trial(data):
    new_data = []
    for element_data in data:
        if (not element_data['is_canceled']) or (element_data['days_to_cancel'] > 7):
            account_key = element_data['account_key']
            join_date = element_data['join_date']
            dict = {account_key: join_date}

            if (dict not in new_data) or (join_date > new_data[account_key]):
                new_data[account_key] = join_date

        return new_data


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


paid_students = remove_trial(enrollments)
paid_engament = remove_trial(engagement)
paid_submissions = remove_trial(project_submissions)

print(len(paid_students))
print(len(paid_engament))
print(len(paid_submissions))