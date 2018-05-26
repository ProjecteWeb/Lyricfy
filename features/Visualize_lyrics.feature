Feature: Visualize lyrics
  I want to see the lyrics of a song
  As a user
  In order to undersand my favourites songs

  Scenario:See the lyrics of one song
    Given I see the songs list that contained "Perfect"
    When I press one song from the list
    Then I can see the lyrics of the song


  Scenario: Search song without lyrics
    Given I see the songs list that contained "Aaa"
    When I press a song from the list
    Then I get a message that the song have no lyrics
