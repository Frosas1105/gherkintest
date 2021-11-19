import pytest
from pytest_bdd import scenarios, given, when, then
from SScalcRosas import *

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
def step_function():
    pass

@when('the <"birthYear>" is entered by the user')
def step_function(birthYear):
    return birthYear

@when('the <"birthMonth>" is entered by the user')
def step_function(birthMonth):
    # Add Your Code Here
    pass

@then(Parser('the age of retirement is "<retireAge>" and the month of retirement is "<retireMonthNum>"'))
def step_function(session: Session):
    # Add Your Code Here
    pass