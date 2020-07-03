# Python3 code to calculate age in years

from datetime import date

print("")

def calculateAge(born):
    today = date.today()
    try:
        birthday = born.replace( year=today.year )

    # raised when birth date is February 29
    # and the current year is not a leap year
    except ValueError:
        birthday = born.replace( year=today.year,
                                 month=born.month + 1, day=1 )

    if birthday > today:
        return today.year - born.year - 1
    else:
        return today.year - born.year

    # Driver code

year= int(input('Enter a year  '))
month = int(input('Enter a month  '))
day = int(input('Enter a day  '))

print( calculateAge( date( year, month, day ) ), "years" )0


