from ssModule2 import *
print("Created: 8/21/2021 By: Fabian Rosas")


def main():
    print("Social Security Full Retirement Age Calculator")
    birthYear = input("Enter the year of birth or 0 to exit: ")
    if birthYear == 0:
        exit()
    elif int(birthYear) < 1900:
        print("Invalid input: Birth year must be after 1900")
        exit()
    elif int(birthYear) > 3000:
        print("Invalid input: Birth year must be before 3000")
        exit()
    monthOfBirth = int(input("Enter the month of birth: "))
    if 1 > monthOfBirth > 12:
        print("Invalid input: Months must be between 1 and 12")
        exit()

    retireAge, retireMonthNum = myFunc(birthYear)  # Assigning variable names to values returned from myFunc

    retireMonthName, retireYear = myFunc2(birthYear, monthOfBirth, retireAge, retireMonthNum)  # Assigning variable names to values returned from myFunc2

    print(f"Your full retirement age is {retireAge} and {retireMonthNum} months")
    print(f"This will be in {retireMonthName} of {retireYear}")


main()
