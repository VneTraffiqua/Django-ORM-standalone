import datetime


def format_duration(visit_time):
    visit_time_in_sec = int(datetime.timedelta.total_seconds(visit_time))
    return f'{visit_time_in_sec // 3600}:{(visit_time_in_sec // 60) % 60}'
