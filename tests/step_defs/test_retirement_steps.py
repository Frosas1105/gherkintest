from pytest_bdd import scenario, given, when, then

from retirement import *

@scenario('../features/retirement.feature', 'Birth year is under 1900')

def test_birthyear():
    pass

@given('birth year entered is under 1900')
def input():
    pass


@then('assertion statement is raised')
def input3000():
    with pytest.raises(ValueError):
        calculate_retirement_age(3000)
