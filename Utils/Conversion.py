
def convert_length(amount, from_unit: str, to_unit: str):
    """

    m - Metre
    hm - Hectometre
    dm - Decimetre
    km - Kilometre
    mm - Megametre
    gm - Gigametre
    tm - Terametre
    pm - Petaetre
    em - Exametre
    zm - Zettametre
    ym - Yottametre

    pc - Parsec
    kpc - Kiloparsec
    mpc - Megaparsec
    gpc - Gigaparsec

    ly = Light year
    kly = Kilo light year
    mly = Mega light year
    gly = Giga light year

    au - Astronomical unit
    kau - Kilo astronomical unit
    mau - Mega astronomical unit
    gau - Giga astronomical unit

    :param amount:
    :param from_unit:
    :param to_unit:
    :return:
    """
    from_factor: float
    match from_unit:
        case "m": from_factor = 1
        case "hm": from_factor = 1 * 10 ** 1
        case "dm": from_factor = 1 * 10 ** 2
        case "km": from_factor = 1 * 10 ** 3
        case "mm": from_factor = 1 * 10 ** 6
        case "gm": from_factor = 1 * 10 ** 9
        case "tm": from_factor = 1 * 10 ** 12
        case "pm": from_factor = 1 * 10 ** 15
        case "em": from_factor = 1 * 10 ** 18
        case "zm": from_factor = 1 * 10 ** 21
        case "ym": from_factor = 1 * 10 ** 24
        case "pc": from_factor = 3.0856775814913673 * 10 ** 16
        case "kpc": from_factor = 3.0856775814913673 * 10 ** 19
        case "mpc": from_factor = 3.0856775814913673 * 10 ** 22
        case "gpc": from_factor = 3.0856775814913673 * 10 ** 25
        case "ly": from_factor = 9.4607304725808 * 10 ** 15
        case "kly": from_factor = 9.4607304725808 * 10 ** 18
        case "mly": from_factor = 9.4607304725808 * 10 ** 21
        case "gly": from_factor = 9.4607304725808 * 10 ** 24
        case "au": from_factor = 1.495978707 * 10 ** 11
        case "kau": from_factor = 1.495978707 * 10 ** 14
        case "mau": from_factor = 1.495978707 * 10 ** 17
        case "gau": from_factor = 1.495978707 * 10 ** 20

    to_factor: float
    match to_unit:
        case "m": to_factor = 1
        case "hm": to_factor = 1 / (1 * 10 ** 1)
        case "dm": to_factor = 1 / (1 * 10 ** 2)
        case "km": to_factor = 1 / (1 * 10 ** 3)
        case "mm": to_factor = 1 / (1 * 10 ** 6)
        case "gm": to_factor = 1 / (1 * 10 ** 9)
        case "tm": to_factor = 1 / (1 * 10 ** 12)
        case "pm": to_factor = 1 / (1 * 10 ** 15)
        case "em": to_factor = 1 / (1 * 10 ** 18)
        case "zm": to_factor = 1 / (1 * 10 ** 21)
        case "ym": to_factor = 1 / (1 * 10 ** 24)
        case "pc": to_factor = 1 / (3.0856775814913673 * 10 ** 16)
        case "kpc": to_factor = 1 / (3.0856775814913673 * 10 ** 19)
        case "mpc": to_factor = 1 / (3.0856775814913673 * 10 ** 22)
        case "gpc": to_factor = 1 / (3.0856775814913673 * 10 ** 25)
        case "ly": to_factor = 1 / (9.4607304725808 * 10 ** 15)
        case "kly": to_factor = 1 / (9.4607304725808 * 10 ** 18)
        case "mly": to_factor = 1 / (9.4607304725808 * 10 ** 21)
        case "gly": to_factor = 1 / (9.4607304725808 * 10 ** 24)
        case "au": to_factor = 1 / (1.495978707 * 10 ** 11)
        case "kau": to_factor = 1 / (1.495978707 * 10 ** 14)
        case "mau": to_factor = 1 / (1.495978707 * 10 ** 17)
        case "gau": to_factor = 1 / (1.495978707 * 10 ** 20)

    try:
        result = amount * from_factor * to_factor
    except NameError:
        raise ValueError(f"Unrecognised units: {from_unit}, {to_unit}")

    return result
