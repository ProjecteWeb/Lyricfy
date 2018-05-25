Feature: Edit playlist
  In order to change it's name or manage my songs list
  As a user
  I want to edit my playlists

  Background: There is a registered user
    Given Exists a user "user3" with password "password"
    Given I login as user "user3" with password "password"

  Scenario: Change the name of MyPlaylist
    Given Exists a playlist "MyPlaylist" for "user3"
    Then I go to Playlists section
    When I go to MyPlaylist page
    Then I can edit MyPlaylist name to MyPlaylist1
    And I can see the Correct Edition message and go back to see MyPlaylist1 name
