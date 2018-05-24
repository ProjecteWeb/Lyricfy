Feature: Register
  In order to can make login and access to my personal workspace
  As a user
  I want to can login in the system


  Scenario: There is a user that want to create an account
    Given I sign up completing the fields as user "user1" with password "password"
    And I repetat the password completing the field with password "password"
    When I save the changes for user "user1" with password "password"
    Then I go to loggin page
    And I login as user "user1" with password "password"
    Then I'm viewing user "user1" home page




