from datetime import datetime
from math import cos, radians


def calculate_solstice(year: int, number: int) -> float:
    """Calculates the date and time of solstices.

    :param year The year for which the calculation will be done. Most accurate for years between 1000 and 3000.
    :param number A number corresponding to which equinox or solstice to calculate. March corresponds to 1 and
                  September to 2

    :returns The Julian day number of the event. Use Util.Date.julian_day_to_datetime to convert to a datetime object.
    """
    return calculate_equinox_or_solstice(year, number * 2)


def calculate_equinox(year: int, number: int) -> float:
    """Calculates the date and time of equinoxes.

    :param year The year for which the calculation will be done. Most accurate for years between 1000 and 3000.
    :param number A number corresponding to which equinox or solstice to calculate. March corresponds to 1 and
                  September to 2

    :returns The Julian day number of the event. Use Util.Date.julian_day_to_datetime to convert to a datetime object.
    """
    return calculate_equinox_or_solstice(year, number * 2 - 1)


def calculate_equinox_or_solstice(year: int, number: int) -> float:
    """Calculates the date and time of equinoxes and solstices.
    Algorithm from Astronomical Algorithms, 2009, by Jean Meeus.

    :param year The year for which the calculation will be done. Most accurate for years between 1000 and 3000.
    :param number A number corresponding to which equinox or solstice to calculate. March corresponds to 1, June to 2,
                  September to 3 and December to 4

    :returns The Julian day number of the event. Use Util.Date.julian_day_to_datetime to convert to a datetime object.
    """

    # Calculate the date of the September equinox for the given year
    # Algorithm from Astronomical Algorithms, 2009, Jean Meeus
    y = (year - 2000) / 1000

    if number == 1:
        jde_0 = 2451623.80984 + 365242.37404 * y + 0.05169 * y ** 2 - 0.00411 * y ** 3 - 0.00057 * y ** 4
    elif number == 2:
        jde_0 = 2451716.56767 + 365241.62603 * y + 0.00325 * y ** 2 + 0.00888 * y ** 3 - 0.00030 * y ** 4
    elif number == 3:
        jde_0 = 2451810.21715 + 365242.01767 * y - 0.06223 * y ** 2 + 0.00823 * y ** 3 + 0.00078 * y ** 4
    elif number == 4:
        jde_0 = 2451900.05952 + 365242.74049 * y - 0.06223 * y ** 2 - 0.00823 * y ** 3 + 0.00032 * y ** 4
    else:
        raise ValueError("Only values 1 through 4 are valid for parameter number")

    t = (jde_0 - 2451545.0) / 36525
    w = 35999.373 * t - 2.47
    d_l = 1 + 0.0334 * cos(radians(w)) + 0.0007 * cos(radians(2 * w))
    s = 485 * cos(radians(324.96 + 1934.136 * t)) \
        + 203 * cos(radians(337.23 + 32964.467 * t)) \
        + 199 * cos(radians(342.08 + 20.186 * t)) \
        + 182 * cos(radians(27.85 + 445267.112 * t)) \
        + 156 * cos(radians(73.14 + 45036.886 * t)) \
        + 136 * cos(radians(171.52 + 22518.443 * t)) \
        + 77 * cos(radians(222.54 + 65928.934 * t)) \
        + 74 * cos(radians(296.72 + 3034.906 * t)) \
        + 70 * cos(radians(243.58 + 9037.513 * t)) \
        + 58 * cos(radians(119.81 + 33718.147 * t)) \
        + 52 * cos(radians(297.17 + 150.678 * t)) \
        + 50 * cos(radians(21.02 + 2281.226 * t)) \
        + 45 * cos(radians(247.54 + 29929.562 * t)) \
        + 44 * cos(radians(325.15 + 3155.956 * t)) \
        + 29 * cos(radians(60.93 + 4443.417 * t)) \
        + 18 * cos(radians(155.12 + 67555.328 * t)) \
        + 17 * cos(radians(288.79 + 4562.452 * t)) \
        + 16 * cos(radians(198.04 + 62894.029 * t)) \
        + 14 * cos(radians(199.76 + 31436.921 * t)) \
        + 12 * cos(radians(95.39 + 14577.848 * t)) \
        + 12 * cos(radians(287.11 + 31931.756 * t)) \
        + 12 * cos(radians(320.81 + 34777.259 * t)) \
        + 9 * cos(radians(227.73 + 1222.114 * t)) \
        + 8 * cos(radians(15.45 + 16859.074 * t))

    jde = jde_0 + (0.00001 * s) / d_l
    return jde
