from Objects import Galaxy
from Utils import hms_to_decimal, dms_to_decimal


class Andromeda(Galaxy):
    name = "Andromeda"
    alt_names = ["Andromeda", "Andromeda Galaxy", "Messier 31", "M31", "NGC 224", "Andromeda Nebula"]
    designation = "M31"
    alt_designations = ["M31", "NGC 224"]
    type = "Barred Spiral"
    constellation = "Andromeda"
    right_ascension = hms_to_decimal(0, 42, 44.3)
    declination = dms_to_decimal(41, 16, 9)
    apparent_magnitude: 3.44


class M31(Andromeda):
    pass


class NGC224(Andromeda):
    pass
