from datetime import date, datetime, timedelta

FILE_NAME = "C:\dylan_time_spent\dylan_time_spent.json"
TIME_FRAMES = {"day": 1, "week": 7, "month": 30, "year": 365}
WEEK_DAYS = 7


def convert_min_to_dec(time):
    if ":" in time:
        hours_min = time.split(":")
        min_in_dec = int(hours_min[1]) / 60
        time = int(hours_min[0]) + min_in_dec
    
    try:
        return float(time)
    except:
        print("Not a valid time")
        return None

def convert_dec_to_min(time):
    time = str(time)
    if "." in time:
        hours_min = time.split(".")
        min_in_time = int(hours_min[1]) * 60 / 100
        while min_in_time > 60:
            min_in_time /= 10
        min_in_time = round(min_in_time)
        if min_in_time % 10 > 0:
            min_in_time *= 10
        
        time = f"{hours_min[0]}:{min_in_time}"
    return time

def get_week():
    day = date.today()
    day_of_week = day.isoweekday()
    start = day_of_week - 1
    day -= timedelta(days=start)

    dates_of_week = list()
    
    for _ in range(WEEK_DAYS):
        dates_of_week.append(day.isoformat())
        day += timedelta(days=1)

    return dates_of_week

current_week = get_week()
today = str(date.today())
current_year = str(date.today().year)
current_month = str(date.today().month)