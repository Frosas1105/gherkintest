import pytest
from pytest_bdd import scenarios, given, when, then
from SScalcRosas import *
from ssModule2 import *

EXTRA_TYPES = {
    'Number': int
}

CONVERTERS = {
    'birthYear' : int,
    'retireAge' : int,
    'retireMonthNum': int,
}
    
scenarios('../features/retirement.feature', example_converters=CONVERTERS)

@given('the user has opened the app')
def start():
    pass

@when('the <"birthYear>" is entered by the user')
def birthYear(birthYear):
    return birthYear

@when('the <"birthMonth>" is entered by the user')
def birthMonth(birthMonth):
    return birthMonth

@then('the age of retirement is "<retireAge>" and the month of retirement is "<retireMonthNum>"')
def step_function(birthYear, birthMonth, retireAge, retireMonthNum):
   year, month, age, monthNum = myFunc2(birthYear, birthMonth, retireAge, retireMonthNum)
   assert year == birthYear and month == birthMonth and age == retireAge and monthNum == retireMonthNum
