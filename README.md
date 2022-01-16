# AstrophotographyTools
### Introduction
Astrophotography Tools started as a small script to calculate the best time of year to view objects in the night
sky. I am hoping to expand it, and introduce new features over time. I recommend looking at the [Astropy](https://www.astropy.org) 
project if you need to do any serious astronomical calculations.

### Usage
Astrophotography tools can be used from the terminal or as a library. 

The CLI supports 3 arguments:

* `--timezone 10` sets the timezone to the given offset from UTC.
* `--equinox 2022 1` returns the date and time of the first equinox in 2022
* `--soltice 2022 1` returns the date and time of the first solstice in 2022

```bash
python3 Main.py --timezone 11 --equinox 2022 1
```
```
Equinox occurs on: 2022-03-21 02:35:19+11:00
```

Alternatively, you can use Astrophotography Tools as a library.

```python
from AstrophotographyTools.Modules import Equinoxes
e = Equinoxes.calculate_equinox(2022, 1)
d = Dates.julian_day_to_datetime(day)
print(d)
```
```
2022-03-21 02:35:19+11:00
```

Astrophotography tools also includes information on deep space objects (as of version 0.1, only Andromeda), which can
be imported with either their designation or name

```python
from AstrophotographyTools.Objects.Database.DeepSkyObjects import M31
# also works: 
# from AstrophotographyTools.Objects.Database.DeepSkyObjects import Andromeda
from AstrophotographyTools.Utils.Formats import decimal_to_hms

print(f"In decimal: {Andromeda.right_ascension}")
print(f"In hours: {decimal_to_hms(Andromeda.right_ascension)}")
```
```
In decimal: 0.7123055555555555
In hours: (0, 42, 44.299999999999784)
```