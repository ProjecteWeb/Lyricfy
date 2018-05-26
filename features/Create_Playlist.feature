Feature: Create playlist
  In order to add here my favourite songs
  As a user
  I want to manage my playlists

  Background: There is a registered user
    Given Exists a user "user2" with password "password"


  Scenario: Registered user wants to add first playlist
    Given I login as user "user2" with password "password"
    Then I go to Playlists section
    And I create a playlist "MyPlaylist" for "user2"
    And I go to MyPlaylists and there are 1 playlists


  Scenario: Registered user add a second playlist
    Given I login as user "user2" with password "password"
    Given Exists a playlist "MyPlaylist" for "user2"
    Then I go to Playlists section
    When I create a playlist "MyPlalylist1" for "user2"
    Then I go to MyPlaylists and there are 2 playlists

  Scenario: Registered user add a playlist with the same name
    Given I login as user "user2" with password "password"
    Given Exists a playlist "MyPlaylist" for "user2"
    Then I go to Playlists section
    When I create another playlist "MyPlaylist" for "user2"
    Then I get an error message





