Feature: retirement calc
    calculator that returns the full retirement age and month to the user

Scenario Outline: calculate retirement age and month
    Given the user has opened the app
    When the <"birthYear>" is entered by the user
    When the <"birthMonth>" is entered by the user
    Then the age of retirement is "<retireAge>" and the month of retirement is "<retireMonthNum>"

    Examples: birth year ranges
    | birthYear | birthMonth | retireAge | retireMonthNum |
    | 1931      | 0          | 65        | 0              |
    | 1938      | 0          | 65        | 2              |
    | 1939      | 0          | 65        | 4              |
    | 1940      | 0          | 65        | 6              |
    | 1941      | 0          | 65        | 8              |
    | 1942      | 0          | 65        | 10             |
    | 1945      | 0          | 66        | 0              |
    | 1955      | 0          | 66        | 2              |
    | 1956      | 0          | 66        | 4              |
    | 1957      | 0          | 66        | 6              |
    | 1958      | 0          | 66        | 8              |
    | 1959      | 0          | 66        | 10             |
    | 1960      | 0          | 67        | 0              |
    | 1989      | 0          | 67        | 0              |


