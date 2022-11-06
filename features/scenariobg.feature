Feature: Events

  Background: User should able to book a events
    Given user should able to launch chrome browser
    Then user should select the location
    When user should click on the location
    Then user should able to click on events page
    And user should click on browse by venue
    And  user should click on art beat:bengaluru
    And user should click on texture painting on canvas
    Then user should click on book
    And user should click on add
    Then user should click on proceed

  Scenario Outline:
    When user enter "<name>" into name textfield
    Then user enter mobile_no "<mobile_no>" into mobile number textfield
    Then user enter the email "<email>" into email textfield
    When user should able to click on checkbox
    Then user should able to click on submit button
    And user should able to click on proceed to pay

    Examples:
      | name        | mobile_no  | email               |
      | sachin      | 9657063172 | sgore9240@gmail.com |
      | shankar     | 9359233886 | kadamshankar668@gmail.com|
      | atul        | 9975827653 | atul11@gmail.com         |
      | sohel       | 997582     | sohel22@gmail.com        |
      | akash       |997582765343 | akash@gmail.com           |





