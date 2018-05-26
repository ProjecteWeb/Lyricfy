Feature: Search field
  In order to find the song or author that I want
  As a user
  I want to search the information into the search field

  Background: I want to use the search bar to find song or artists
    Given I'm on the initial page of the application

  Scenario: Search a song in the search bar
    When I search the song "Boom"
    Then I obtain a list with all the relationed names with song name "Boom"

  Scenario: Search a song that doesn't exists
    When I search the song "z1x2c"
    Then I get a message that there is no song with this name