from datetime import date, time


def today():
    return date.today()


def date_format(day, month, year):
    return date(year, month, day)


def current_day():
    return date.today.day


def current_month():
    return date.today.month


def current_year():
    return date.today.year
