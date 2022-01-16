from Utils.Formats import decimal_to_hms, decimal_to_dms


def format_hms(hours: int, minutes: int = None, seconds: float = None, rounding: int = 2) -> str:
    if minutes is None:
        hours, minutes, seconds = decimal_to_hms(hours)
    return f"{hours}h {minutes}m {round(seconds, rounding)}s"


def format_dms(hours: int, minutes: int = None, seconds: float = None, rounding: int = 2, unicode: bool = True) -> str:
    if minutes is None:
        hours, minutes, seconds = decimal_to_dms(hours)
    if unicode:
        return f"{hours}° {minutes}′ {round(seconds, rounding)}″"
    else:
        return f"{hours}d {minutes}m {round(seconds, rounding)}s"
