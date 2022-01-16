from datetime import datetime, timezone, timedelta
from math import floor


def datetime_to_julian_day(dt: datetime) -> int:
    y = dt.year
    m = dt.month
    d = dt.day \
        + (((((dt.second / 60) + dt.minute) / 60) + dt.hour) / 24)

    if m < 3:
        y -= 1
        m += 12

    a = int(y / 100)
    b = 2 - a + int(a / 4)

    jd = int(365.25 * (y + 4716)) \
         + int(30.6001 * (m + 1)) \
         + d + b - 1524.5

    return jd


def julian_day_to_datetime(day: float) -> datetime:
    jd = day + 0.5
    z = floor(jd)
    f = jd - z

    if z < 2299161:
        a = z
    else:
        al = int((z - 1867216.25) / 36524.25)
        a = z + 1 + al - int(al / 4)

    b = a + 1524
    c = int((b - 122.1) / 365.25)
    d = int(365.25 * c)
    e = int((b - d) / 30.6001)

    day_of_month = int(b - d - int(30.6001 * e) + f)
    month = e - 1 if e < 14 else e - 13
    year = c - 4716 if month > 2 else c - 4715
    hour = f * 24
    minute = (hour - int(hour)) * 60
    second = (minute - int(minute)) * 60

    return datetime(year, month, day_of_month, int(hour), int(minute), int(second), tzinfo=timezone(timedelta(hours=0)))
