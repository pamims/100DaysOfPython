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
DEALER_HAND = [];
COINS = {"stack" : 200, "bet" : [0]};


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

def get_hand_value(hand):
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

def get_player_hand_value(hand_index = 0):
    """Returns the current value of the hand"""
    hand = HAND[hand_index];
    return get_hand_value(hand);
    
def split(hand_index = 0):
    """Splits a hand into two smaller hands"""
    show_coins();
    HAND.append([HAND[hand_index].pop()]);
    COINS["bet"].append(0);
    place_bet(-1);
    print("");
    show_coins();
    return;

def can_split(hand_index = 0):
    """Returns True if a split is allowed"""
    if COINS["stack"] <= 0:
        return False;
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
        print("\nSplit aces are only allowed one card.");
        return False;
    if get_player_hand_value(hand_index) >= 21:
        print("\nYour hand is already worth 21.")
        return False;
    return True;

def clear_hands():
    """Clears the HAND list"""
    HAND.clear();
    HAND.append([]);
    DEALER_HAND.clear();
    return;

def show_cards(show_dealer_hand = False):
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
        hand_string += f" : {get_player_hand_value(i)}";
        print(hand_string);
    if not show_dealer_hand:
        print(f"Dealer card: {DEALER_HAND[0]}");
    else:
        hand_string = "Dealer Hand :";
        for card in DEALER_HAND:
            hand_string += f" {card}";
        hand_string += f" : {get_hand_value(DEALER_HAND)}";
        print(hand_string);
    return;

def will_split(hand_index):
    """Returns player's decision on splitting a hand"""
    hand_string = "";
    if len(HAND) > 1:
        hand_string = f" Hand{hand_index + 1}";
    will_split = "";
    while will_split != "y" and will_split != "n":
        will_split = input(f"\nWould you like to split{hand_string} (Y/n)? ").lower();
    if will_split == "y":
        return True;
    return False;

def deal_cards():
    """Deals initial cards to the player and dealer"""
    if len(DEALER_HAND) < 2:
        # Nobody has to know...
        DEALER_HAND.append(DECK.pop());
        DEALER_HAND.append(DECK.pop());
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

def is_valid_bet(value):
    if not value.isnumeric():
        print("Number must be a positive integer.");
        return False;
    value = int(value);
    if value <= 0 or value > COINS["stack"]:
        print("Cannot bet more than you have or less than 1.");
        return False;
    return True;

def place_bet(hand_index = 0):
    bet = "";
    valid = False;
    while not valid:
        bet = input(f"How much to bet? ");
        valid = is_valid_bet(bet);
    bet = int(bet);
    COINS["stack"] -= bet;
    COINS["bet"][hand_index] = bet;

def show_coins():
    print(f"Coins: {COINS['stack']}");
    if COINS["bet"][0] != 0:
        num_bets = len(COINS["bet"]);
        for i in range(0, num_bets):
            if num_bets > 1:
                hand_string = f"Hand{i + 1} ";
            else:
                hand_string = "";
            print(f"{hand_string}Bet: {COINS['bet'][i]}");
    return;

def can_double(hand_index = 0):
    if not can_hit(hand_index):
        return False;
    if COINS["bet"][hand_index] > COINS["stack"]:
        print("Not enough coins left.");
        return False;
    return True;

# Player decisions
def player_hit(hand_index = 0):
    yes_no = {"y" : True, "n" : False}
    hit_again = True;
    while hit_again:
        hit(hand_index);
        show_cards();
        if get_player_hand_value(hand_index) < 21:
            decision = "";
            while decision not in yes_no:
                decision = input("Would you like to hit again (Y/n)? ").lower();
            hit_again = yes_no[decision];
        else:
            hit_again = False;
    return;

def player_double(hand_index = 0):
    COINS["stack"] -= COINS["bet"][hand_index];
    COINS["bet"][hand_index] *= 2;
    hit(hand_index);
    show_coins();
    show_cards();
    return;

def player_stand(hand_index = 0):
    return;

def player_surrender(hand_index = 0):
    coins = round(COINS["bet"][hand_index] / 2);
    COINS["stack"] += coins;
    COINS["bet"][hand_index] = 0;
    show_coins();
    show_cards();
    return;

PLAYER_DECISIONS = {
    "hit" : player_hit,
    "double" : player_double,
    "stand" : player_stand,
    "surrender" : player_surrender
}

def player_win(i = 0, hand_number = ""):
    print(f"Hand{hand_number} wins!");
    COINS["stack"] += COINS["bet"][i] * 2;
    COINS["bet"][i] = 0;
    return;

def player_lose(i = 0, hand_number = ""):
    print(f"Hand{hand_number} loses.");
    COINS["bet"][i] = 0;
    return
 
# Main game functions
def begin_round():
    print("Beginning new round.");
    if len(DECK) < MIN_CARDS_LEFT:
        set_deck();
        print("The deck has been shuffled.");
    show_coins();
    place_bet();
    print("");
    show_coins();
    deal_cards();
    return;

def get_player_decision():
    num_hands = len(HAND);
    for i in range(0, num_hands):
        if num_hands > 1:
            hand_string = f" for Hand{i + 1}";
        else:
            hand_string = "";
        print(f"\nPlayer, make a decision{hand_string}.");
        decision = "";
        while decision not in PLAYER_DECISIONS:
            decision = input("hit, double, stand, surrender: ")
            if decision == "hit" and not can_hit(i):
                print(f"Not allowed to hit.");
                decision = "";
            elif decision == "double" and not can_double(i):
                print("Not allowed to double down.");
                decision = "";

        func = PLAYER_DECISIONS[decision];
        func(i);
    return;

def dealer_plays():
    print("\nDealer plays...");
    while get_hand_value(DEALER_HAND) < 17:
        DEALER_HAND.append(DECK.pop());
    show_cards(True);
    return;

def end_round():
    print("\nEnd round.");
    dealer_score = get_hand_value(DEALER_HAND);
    num_hands = len(HAND);
    hand_number = "";
    for i in range(0, num_hands):
        if num_hands > 1:
            hand_number = f"{i + 1}";
        value = get_player_hand_value(i);
        if value > 21:
            player_lose(i, hand_number);
        elif value > dealer_score:
            player_win(i, hand_number);
        elif value == dealer_score:
            if len(HAND[i]) == 2 and len(DEALER_HAND) > 2:
                player_win(i, hand_number);
            else:
                player_lose(i, hand_number);
        elif dealer_score > 21:
            player_win(i, hand_number);
        else:
            player_lose(i, hand_number);
    COINS["bet"] = [0];
    show_coins();
    clear_hands();
    return;
    
# You can hit and double down split hands.