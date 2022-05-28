import random;
ALLOWED_FAILURES = 6;
words = ["buffalo", "parrot", "squirrel", "hedgehog"];
word = random.choice(words);

correct_letters = ['_'] * len(word);
incorrect_letters = [];

letters_remaining = len(word);
while letters_remaining > 0 and len(incorrect_letters) < ALLOWED_FAILURES:
    guess = input("Guess a letter: ").lower();
    if guess in correct_letters or guess in incorrect_letters:
        print("That letter has already been used.");
        continue;
    elif not guess.isalpha():
        print("That is not a letter.");
        continue;

    i = 0;
    is_in_word = False;
    for letter in word:
        if guess == letter:
            is_in_word = True;
            correct_letters[i] = letter;
            letters_remaining -= 1;
        i += 1;
    
    if not is_in_word:
        incorrect_letters.append(guess);

    print(f"The word so far: {correct_letters}");
    print(f"Incorrect guesses: {incorrect_letters}");

print("Game Over");
if len(incorrect_letters) < ALLOWED_FAILURES:
    print("Player wins!");
else:
    print("Player loses :(");
