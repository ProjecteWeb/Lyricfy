Feature: Edit playlist
  In order to change it's name or manage my songs list
  As a user
  I want to edit my playlists

  Background: There is a registered user
    Given Exists a user "user3" with password "password"
    Given I login as user "user3" with password "password"
    Given Exists a playlist "MyPlaylist" for "user3"
    Given Exists song "FirstSong"
    Given Exists a relation Song "FirstSong" and "MyPlaylist"


  Scenario: Change the name of MyPlaylist
    Then I go to Playlists section
    When I go to MyPlaylist page
    Then I can edit MyPlaylist name to "MyPlaylist1"
    And I can see the Correct Edition message and go back to see "MyPlaylist1" name

  Scenario: Delete playlist MyPlaylist
    Then I go to Playlists section
    When I go to MyPlaylist page
    Then I can delete MyPlaylist
    And comprove that "MyPlaylist" doesn't exists in Plyalists list


  Scenario: Delete song from MyPlaylist
    Then I go to Playlists section
    When I go to MyPlaylist page
    Then I delete song "FirstSong" from "MyPlaylist" and save the changes
    Then I see the delete confirmation of song "FirstSong"






