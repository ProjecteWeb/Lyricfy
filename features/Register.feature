Feature: Register
  In order to can make login and access to my personal workspace
  As a user
  I want to can login in the system


  Scenario: There is a user that want to create an account
    Given I sign up completing the fields as user "user1" with password "qwer1234"
    Given I login as user "user1" with password "qwer1234"
    Then I'm viewing user "user1" home page


  Scenario: There is a registered user that want to create an account
    Given I sign up completing the fields as user "user1" with password "qwer1234"
    When I sign up completing the fields as user "user1" with password "qwer12345"
    Then There is an error because the user allready exists


  Scenario: User wants to create account with two different passwords
    When I try to sign up with "user2" using password "qwer1234" with password confirmation "qwer12345"
    Then There is as error because I use two different passwords









