import requests, json

# 1 and 2. Navigate to https://deckofcardsapi.com/ and check if the site is up
def is_site_up():
    response = requests.get("https://deckofcardsapi.com/")
    return response.status_code == 200

if not is_site_up():
    print("The site is NOT up!")
else:
    # 3. Get a new deck
    response = requests.get("https://deckofcardsapi.com/api/deck/new/")
    new_deck_content = response.json()
    print('New Deck: ', json.dumps(new_deck_content, indent=4))
    deck_id = new_deck_content["deck_id"]
    print(f'New Deck ID: {deck_id}')

    # 4. Shuffle the deck
    response = requests.get(f"https://deckofcardsapi.com/api/deck/{deck_id}/shuffle/")
    shuffled_deck_content = response.json()
    print('Shuffled New Deck: ', json.dumps(shuffled_deck_content, indent=4))

    # 5. Draw 6 cards from shuffled deck and deal three cards alternatively to each of two players
    # Note: each player should get 2 cards first
    # to determine whether either has blackjack (an Ace + 10/Jack/Queen/King)

    response = requests.get(f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=6")
    draw_cards_content = response.json()
    player1_cards = []
    player2_cards = []
    for i in range(0,6):
        if i % 2:
            player1_cards.append(draw_cards_content["cards"][i])
        else:
            player2_cards.append(draw_cards_content["cards"][i])

    # Define a function to calculate a hand's value
    # that is used to check whether either player has blackjack (total hand value of 21)
    def hand_value(hand):
        value = 0
        for card in hand:
            if card["value"] in ["JACK", "QUEEN", "KING"]:
                value += 10
            elif card["value"] == "ACE":
                value += 11      # can use as value += 1 in certain card combinations if the player getting more cards
            else:
                value += int(card["value"])
        return value

    # 6 and 7. Check whether either player has blackjack and write out if either has
    if hand_value(player1_cards) == 21:
        print('Player1 has BlackJack!')
    print('Player1 cards: ', [card["code"] for card in player1_cards], "Hand value: ", hand_value(player1_cards))
    if hand_value(player2_cards) == 21:
        print('Player2 has BlackJack!')
    print('Player2 cards: ', [card["code"] for card in player2_cards], "Hand value: ", hand_value(player2_cards))

