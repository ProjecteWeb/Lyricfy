Feature: Visualize playlists
  In order to visualize my playlists
  As a user
  I want to can access to my playlists list

  Background: There is a registered user
    Given Exists a user "user2" with password "password"
    Given Exists a playlist "MyPlaylist" for "user2"


  Scenario: Registered user wants visualize their playlists
    Given I login as user "user2" with password "password"
    Then I'm viewing playlist "MyPlaylist" in playlists page
