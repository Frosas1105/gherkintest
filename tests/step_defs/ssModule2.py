import datetime

def myFunc(birthYear):
        birthYear = int(birthYear)
        retireAge = 0
        retireMonthNum = 0
        if 1900 <= birthYear <= 1937:
            retireAge = 65
        elif birthYear == 1938:
            retireAge = 65
            retireMonthNum = 2
        elif birthYear == 1939:
            retireAge = 65
            retireMonthNum = 4
        elif birthYear == 1940:
            retireAge = 65
            retireMonthNum = 6
        elif birthYear == 1941:
            retireAge = 65
            retireMonthNum = 8
        elif birthYear == 1942:
            retireAge = 65
            retireMonthNum = 10
        elif 1943 <= birthYear <= 1954:
            retireAge = 66
        elif birthYear == 1955:
            retireAge = 66
            retireMonthNum = 2
        elif birthYear == 1956:
            retireAge = 66
            retireMonthNum = 4
        elif birthYear == 1957:
            retireAge = 66
            retireMonthNum = 6
        elif birthYear == 1958:
            retireAge = 66
            retireMonthNum = 8
        elif birthYear == 1959:
            retireAge = 66
            retireMonthNum = 10
        elif birthYear >= 1960:
            retireAge = 67
        else:
            print("Invalid input")
        return retireAge, retireMonthNum

    # this function recieves input from the user and returned values from myfunc1.
def myFunc2(birthYear, monthOfBirth, retireAge, retireMonthNum):
        birthYear = int(birthYear)
        sumOfMonths = monthOfBirth + retireMonthNum
        retireYear = birthYear + retireAge
        # here is a check to add 1 year if the total of months exceeds 12 months
        if sumOfMonths > 12:
            sumOfMonths = sumOfMonths - 12
            retireYear += 1
        # these 2 line take the datetime module and converts the months number into the actual month.
        month = datetime.date(retireYear, sumOfMonths, 1).strftime("%B")
        retireMonthName = month

        return retireMonthName, retireYear
