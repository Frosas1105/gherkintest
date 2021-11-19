Feature: retirement calc
    Checking If assertion are raised

Scenario: Birth year is under 1900
    Given birth year entered is under 1900
    Then assertion statement is raised

Scenario: Birth year is over 3000
    Given birth year entered is over 3000
    Then assertion statement is raised
