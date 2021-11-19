from pytest_bdd import scenarios, given, when, then, parsers
from pytest_bdd.scenario import scenario
from retirement import *

CONVERTERS = {
    'dates': int,
}

scenarios('../features/retirement.feature')


def test_birthyear():
    pass

@given('birth year entered is under 1900')
def test_input():
   pass
    
@then('assertion statement is raised')
def test_input1899():
    with pytest.raises(ValueError):
        calculate_retirement_age(1899)
    
@given('birth year entered is over 3000')
def test_input2():
    pass

@then('assertion statement is raised')
def test_input3001():
    with pytest.raises(ValueError):
        calculate_retirement_age(3001)


    