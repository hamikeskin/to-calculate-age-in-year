from datetime import date


def calculateAge(birthDate):
    days_in_year = 365.2425
    age = int((date.today() - birthDate).days / days_in_year)
    return age


print(calculateAge(date(1999, 6, 15)), "years")
