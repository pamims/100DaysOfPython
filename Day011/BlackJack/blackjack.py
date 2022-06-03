import random

# Constant
CARD_VALUES = {
    "A" : 11,
    "2" : 2,
    "3" : 3,
    "4" : 4,
    "5" : 5,
    "6" : 6,
    "7" : 7,
    "8" : 8,
    "9" : 9,
    "10" : 10,
    "J" : 10,
    "Q" : 10,
    "K" : 10
};
MIN_CARDS_LEFT = 52;

# Game Variables
DECK = [];
HAND = [[]];


# Helper functions
def set_deck(num_decks = 6):
    """Creates a fresh dealer deck made of num_decks of playing cards"""
    DECK.clear();
    num_each_card = 4 * num_decks;
    for key in CARD_VALUES:
        for i in range(0, num_each_card):
            DECK.append(key);
    random.shuffle(DECK);
    return;

def get_hand_value(hand_index = 0):
    """Returns the current value of the hand"""
    hand = HAND[hand_index];
    value = 0;
    for card in hand:
        value += CARD_VALUES[card];
    if value <= 21:
        return value;
    num_aces = hand.count("A");
    while value > 21 and num_aces > 0:
        value -= 10;
        num_aces -= 1;
    return value;

def split(hand_index = 0):
    """Splits a hand into two smaller hands"""
    HAND.append([HAND[hand_index].pop()]);
    return;

def can_split(hand_index = 0):
    """Returns True if a split is allowed"""
    value1 = CARD_VALUES[HAND[hand_index][0]];
    value2 = CARD_VALUES[HAND[hand_index][1]];
    # You can split non identical 10 value cards.
    if value1 != value2:
        return False;
    # Allowed to split twice (up to three hands).
    if len(HAND) >= 3:
        return False;
    # Splits Aces cannot be re-split.
    if value1 == 11 and len(HAND) == 2:
        return False;
    return True;

def hit(hand_index = 0):
    """Add a card to a hand"""
    HAND[hand_index].append(DECK.pop());
    return;

def is_split():
    """Returns True if the deck is split"""
    return len(HAND) > 1;

def can_hit(hand_index = 0):
    """Returns true if hit is allowed"""
    # Split Aces receive only one card.
    if is_split() and HAND[hand_index][0] == "A":
        return False;
    if get_hand_value(HAND[hand_index]) >= 21:
        return False;
    return True;

def clear_hand():
    """Clears the HAND list"""
    HAND.clear();
    HAND.append([]);
    return;

def show_cards():
    """Displayes the cards in the player's hand"""
    num_hands = len(HAND);
    for i in range(0, num_hands):
        hand_string = "";
        if num_hands > 1:
            hand_string += f"Hand{i + 1} :";
        else:
            hand_string += "Hand :";
        for card in HAND[i]:
            hand_string += f" {card}";
        hand_string += f" : {get_hand_value(i)}"
        print(hand_string);
    return;

def will_split(hand_index):
    """Returns player's decision on splitting a hand"""
    hand_string = "";
    if len(HAND) > 1:
        hand_string = f" Hand{hand_index + 1}";
    will_split = "";
    while will_split != "y" and will_split != "n":
        will_split = input(f"Would you like to split{hand_string} (Y/n)? ").lower();
    if will_split == "y":
        return True;
    return False;

def deal_cards():
    """Deals initial cards to the player"""
    hand_range = range(0, len(HAND));
    for i in hand_range:
        while len(HAND[i]) < 2:
            hit(i);
    show_cards();
    for i in hand_range:
        if can_split(i) and will_split(i):
            split(i);
            deal_cards();
    return;


# Game phases
def begin_round():
    print("Beginning new round.");
    clear_hand();
    print(str(len(DECK)));
    if len(DECK) < MIN_CARDS_LEFT:
        set_deck();
        print(str(len(DECK)));
        print("The deck has been shuffled");
    deal_cards();
    return;

def get_player_decision():
    print("Player, make a decision.");
    print("Not yet implemented...");
    return;

def dealer_plays():
    print("Dealer plays...");
    print("Not yet implemented...");
    return;

def end_round():
    print("End round.");
    print("Not yet implemented...");
    return;

    
# You can hit and double down split hands.