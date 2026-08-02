from datetime import datetime
import calendar
import time


# ---------- Current Time ---------- #

def current_time():

    return datetime.now().strftime(
        "Current time is %I:%M:%S %p"
    )


# ---------- Current Date ---------- #

def current_date():

    return datetime.now().strftime(
        "Today is %d %B %Y"
    )


# ---------- Current Day ---------- #

def current_day():

    return datetime.now().strftime(
        "Today is %A"
    )


# ---------- Current Month ---------- #

def current_month():

    month = datetime.now().month

    return f"Current month is {calendar.month_name[month]}."


# ---------- Current Year ---------- #

def current_year():

    return f"Current year is {datetime.now().year}."


# ---------- Day Number ---------- #

def day_number():

    return f"Today is day {datetime.now().day} of the month."


# ---------- Week Number ---------- #

def week_number():

    week = datetime.now().isocalendar().week

    return f"This is week {week} of the year."


# ---------- Greeting ---------- #

def greeting():

    hour = datetime.now().hour

    if 5 <= hour < 12:
        return "Good Morning."

    elif 12 <= hour < 17:
        return "Good Afternoon."

    elif 17 <= hour < 21:
        return "Good Evening."

    return "Good Night."


# ---------- Time Zone ---------- #

def timezone():

    return f"Current timezone is {time.tzname[0]}."


# ---------- Date & Time ---------- #

def current_datetime():

    return datetime.now().strftime(
        "%A, %d %B %Y, %I:%M:%S %p"
    )


# ---------- Unix Timestamp ---------- #

def unix_timestamp():

    return f"Unix timestamp is {int(time.time())}."


# ---------- 24-Hour Time ---------- #

def military_time():

    return datetime.now().strftime(
        "Current 24-hour time is %H:%M:%S"
    )


# ---------- AM / PM ---------- #

def am_pm():

    return datetime.now().strftime(
        "It is currently %p."
    )


# ---------- Day Of Year ---------- #

def day_of_year():

    return f"Today is day {datetime.now().timetuple().tm_yday} of the year."