Feature: Add song to playlist
  In order to save my favourite song
  As a user
  I want to add this at my playlist

  Background: I want to add a song to MyPlaylist
    Given Exists a user "user5" with password "qwer1234"
    Given I login as user "user5" with password "qwer1234"


  Scenario: Registered user add a song to playlist
    Given Exists a playlist "MySongsPlaylist" for "user5"
    When I search the song "Perfect"
    Then I see the songs list that contained "Perfect"
    And I press one song from the list
    And I can add this song to MyPlaylist
