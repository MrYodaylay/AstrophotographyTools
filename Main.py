from argparse import ArgumentParser
from datetime import timezone, timedelta

from Utils import Dates


# Globals
g_tz: timezone
g_td: timedelta


# Helper functions
def timezones(p):
    global g_td
    g_td = timedelta(hours=int(p[0]))
    global g_tz
    g_tz = timezone(g_td)


# Views
def equinox_view(p):
    from Modules import Equinoxes
    day = Equinoxes.calculate_equinox(int(p[0]), int(p[1]))
    date = Dates.julian_day_to_datetime(day)

    global g_td
    global g_tz
    if g_tz is not None:
        date = date.astimezone(g_tz)
        print(f"Equinox occurs on: {date}")
    else:
        print(f"Equinox occurs on: {date} UTC")


def solstice_view(p):
    from Modules import Equinoxes
    day = Equinoxes.calculate_solstice(int(p[0]), int(p[1]))
    date = Dates.julian_day_to_datetime(day)

    global g_td
    global g_tz
    if g_tz is not None:
        date = date.astimezone(g_tz)
        print(f"Solstice occurs on: {date}")
    else:
        print(f"Solstice occurs on: {date} UTC")


# Main method
def main():
    parser = ArgumentParser()
    parser.add_argument("--timezone", action="store", nargs=1)
    parser.add_argument("--equinox", action="extend", nargs=2)
    parser.add_argument("--solstice", action="extend", nargs=2)
    args = vars(parser.parse_args())

    run = []

    for arg in args:
        match arg:
            case "timezone" if args["timezone"] is not None: timezones(args["timezone"])
            case "equinox" if args["equinox"] is not None: run.append((equinox_view, args["equinox"]))
            case "solstice" if args["solstice"] is not None: run.append((solstice_view, args["solstice"]))

    for runnable in run:
        runnable[0](runnable[1])


if __name__ == "__main__":
    main()

    from Objects.Database.DeepSkyObjects import Andromeda
    from Utils.Formats import decimal_to_hms
    print(f"In decimal: {Andromeda.right_ascension}")
    print(f"In hours: {decimal_to_hms(Andromeda.right_ascension)}")

