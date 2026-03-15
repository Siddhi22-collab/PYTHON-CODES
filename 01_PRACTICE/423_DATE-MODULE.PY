from datetime import date
ex = date.today()
print(f"Today date:{ex}")
print(f"Year:{ex.year},Month:{ex.month},Day:{ex.day}")
print(f"Today ISO weekday (1=Mon):{ex.isoweekday()}")
print(f"Today weekday (0=Mon):{ex.weekday()}")