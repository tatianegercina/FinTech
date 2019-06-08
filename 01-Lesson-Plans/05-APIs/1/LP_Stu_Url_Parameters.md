### 16. Students Do: URL Parameters (15 mins)

This activity is dedicated to giving the students an opportunity to use a fun API. Students play a game of BlackJack using the `Deck of Cards` API. The key skills reinforced in this activity include the execution of `GET` requests using the Python `requests library`, extraction of JSON elements, and parameterization of API `request URLs`.

Students can play the game against a classmate or imaginary dealer. Students are encouraged to work as partners so they can pair-program and play against one another.

**Files:**

* [url_parameters.ipynb](Activities/16-Stu_URL_Parameters/Unsolved/url_parameters.ipynb)

**Instructions:**

* [README.md](Activities/16-Stu_URL_Parameters/README.md)

### 17. Instructor Do: Review URL Parameters (5 mins)

**Files:**

* [url_parameters.ipynb](Activities/16-Stu_URL_Parameters/Solved/url_parameters.ipynb)

Facilitate a dry walk through of the solution utilizing the following discussion points:

* Passing `parameters` to APIs through `request URLs` gives users the ability to configure and control API actions. By passing `parameters` to the `request URLs` for the `Deck of Cards` API, users can create a deck of cards can be created and shuffled. Parameters also allow users to draw `n` number of cards from the deck.

  ```python
  create_deck_url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=6"
  draw_cards_url = "https://deckofcardsapi.com/api/deck/<<deck_id>>/draw/?count=2"
  shuffle_deck_url = "https://deckofcardsapi.com/api/deck/<<deck_id>>/shuffle/"
  ```

  ![parameters.png](Images/parameters.png)

* The Deck of Cards API has some parameters that need to be specified using a forward slash `/`. There are other parameters that need to be passed using the `?` symbol.

  ![parameter_formats.png](Images/parameter_formats.png)

* Interpolation is a common way to pass `parameters` to `request URLs`. This allows for parameters to be assigned to variables and those variables to be interpolated into the `request URLs`. This also enables dynamic configuration of parameters and removes instances of hard-coded parameter values.

  ```python
  draw_cards_url = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=2"
  shuffle_deck_url = f"https://deckofcardsapi.com/api/deck/{deck_id}/shuffle/"
  print(draw_cards_url)
  print(shuffle_deck_url)
  ```

  ```
  https://deckofcardsapi.com/api/deck/epigy7ynp5yi/draw/?count=2
  https://deckofcardsapi.com/api/deck/epigy7ynp5yi/shuffle/
  ```

* `Parameterized request URLs` are submitted like any other URL: using the `GET` request. `Parameters` help simplify the amount of data being returned from the output. This makes parsing JSON objects/rows easy, especially since JSON data often times has to be iterated. The more parameters used, the less data returned.

  ```python
  # Draw two cards
  drawn_cards = requests.get(draw_cards_url).json()
  ```

* In order to parse JSON data, the structure of the JSON data needs to be understood. JSON data includes parent objects, one or many JSON objects, and elements/attributes for each JSON object. Each of these has to be specified when extracting values from JSON output.

  ```python
  # Select returned card's value and suit (i.e. 3 of clubs)
  player_1_card_1 = drawn_cards['cards'][0]['value'] + " of " + drawn_cards['cards'][0]['suit']
  player_1_card_2 = drawn_cards['cards'][1]['value'] + " of " + drawn_cards['cards'][1]['suit']

  # Print player cards
  print(player_1_card_1)
  print(player_1_card_2)
  ```

  ```
  3 of HEARTS
  QUEEN of CLUBS
  ```

  ![parse_json.png](Images/parse_json.png)

Ask the following questions:

* In addition to `deck_id`, what other parameter values should be interpolated for the `draw_cards_url`?

  > "count"

* If you were to contribute to the `Deck of Cards` API, what type of features or functionality would you want to enhance or add?

  > "Game Options (i.e. Poker, Go Fish, War, etc.)

  > "Automated dealing based off of game type (i.e. Poker, Texas Hold'em, etc.)"

  > "Game specific interactions (i.e. playing war compares player cards turn by turn)"

  > "Turn based gaming"

  > "Scoring"

* Has url `parameters` made APIs more challenging or easier to use?

Ask if there are any remaining questions or comments before continuing.
