from math import floor


def normalise_hours(hours: float) -> float:
    if hours > 24:
        hours -= 24
    elif hours < 0:
        hours += 24
    return hours


def hms_to_decimal(hour: int, minute: int, second: float) -> float:
    return hour + minute / 60 + second / 3600


def decimal_to_hms(hours: float) -> tuple[int, int, float]:
    mins = (hours - floor(hours)) * 60
    secs = (mins - floor(mins)) * 60
    return floor(hours), floor(mins), secs


def normalise_degrees360(degrees: float) -> float:
    if degrees > 360:
        degrees -= 360
    elif degrees < 0:
        degrees += 360
    return degrees


def normalise_degrees90(degrees: float) -> float:
    if degrees > 90:
        degrees -= 90
    elif degrees < 0:
        degrees += 90
    return degrees


def dms_to_decimal(degree: int, minute: int, second: float) -> float:
    return degree + minute / 60 + second / 3600


def decimal_to_dms(degress: float) -> tuple[int, int, float]:
    mins = (degress - floor(degress)) * 60
    secs = (mins - floor(mins)) * 60
    return floor(degress), floor(mins), secs
