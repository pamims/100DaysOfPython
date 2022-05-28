import random;
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

def draw_output(correct_letters, incorrect_letters):
    stage = ALLOWED_FAILURES - len(incorrect_letters);
    print(f"The word so far: {correct_letters}");
    print(STAGES[stage]);
    print(f"Incorrect guesses: {incorrect_letters}");
    return;


word = random.choice(WORDS);

correct_letters = ['_'] * len(word);
incorrect_letters = [];
while '_' in correct_letters and len(incorrect_letters) < ALLOWED_FAILURES:
    draw_output(correct_letters, incorrect_letters);
    guess = input("Guess a letter: ").lower();
    print("\n\n");
    if guess in correct_letters or guess in incorrect_letters:
        print("That letter has already been used.");
        continue;
    elif not guess.isalpha():
        print("That is not a letter.");
        continue;

    i = 0;
    if guess in word:
        for letter in word:
            if guess == letter:
                correct_letters[i] = letter;
            i += 1;
    else:
        incorrect_letters.append(guess);

draw_output(correct_letters, incorrect_letters);
print("Game Over");
if len(incorrect_letters) < ALLOWED_FAILURES:
    print("Player wins!");
else:
    print("Player loses :(");
