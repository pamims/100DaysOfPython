# Hangman
# Author: Powell A. Mims
# Play a game of hangman


import random;

# 'Constant' values
WORDS = ["buffalo", "parrot", "squirrel", "hedgehog"];
STAGES = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
ALLOWED_FAILURES = len(STAGES) - 1;

# Helper functions
def draw_output(correct_letters, incorrect_letters):
    stage = ALLOWED_FAILURES - len(incorrect_letters);
    print(f"The word so far: {correct_letters}");
    print(STAGES[stage]);
    print(f"Incorrect guesses: {incorrect_letters}");
    return;

# Program start
word = random.choice(WORDS);
correct_letters = ['_'] * len(word);
incorrect_letters = [];
game_is_over = False;

# Game loop
while not game_is_over:
    # Show game status and collect input
    draw_output(correct_letters, incorrect_letters);
    guess = input("Guess a letter: ").lower();
    print("\n\n");

    # Filter for bad input
    if guess in correct_letters or guess in incorrect_letters:
        print("That letter has already been used.");
        continue;
    elif not guess.isalpha():
        print("That is not a letter.");
        continue;

    # Update game state
    i = 0;
    if guess in word:
        for letter in word:
            if guess == letter:
                correct_letters[i] = letter;
            i += 1;
    else:
        incorrect_letters.append(guess);
    
    # Check for game over
    if '_' not in correct_letters or len(incorrect_letters) >= ALLOWED_FAILURES:
        game_is_over = True;

# Results
draw_output(correct_letters, incorrect_letters);
print("Game Over");
if len(incorrect_letters) < ALLOWED_FAILURES:
    print("Player wins!");
else:
    print("Player loses :(");
