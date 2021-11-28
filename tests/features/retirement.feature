Feature: retirement calc
    calculator that returns the full retirement age and month to the user

Scenario Outline: calculate retirement age and month
    Given the user has opened the app
    When the <"birthYear>" is entered by the user
    When the <"monthOfBirth>" is entered by the user
    Then the age of retirement is "<retireAge>" and the month of retirement is "<retireMonthNum>"

    Examples: birth year ranges
    | birthYear | monthOfBirth | retireAge | retireMonthNum |
    | 1931      | 1            | 65        | 0              |
    | 1938      | 1            | 65        | 2              |
    | 1939      | 1            | 65        | 4              |
    | 1940      | 1            | 65        | 6              |
    | 1941      | 1            | 65        | 8              |
    | 1942      | 1            | 65        | 10             |
    | 1945      | 1            | 66        | 0              |
    | 1955      | 1            | 66        | 2              |
    | 1956      | 1            | 66        | 4              |
    | 1957      | 1            | 66        | 6              |
    | 1958      | 1            | 66        | 8              |
    | 1959      | 1            | 66        | 10             |
    | 1960      | 1            | 67        | 0              |
    | 1989      | 1            | 67        | 0              |


