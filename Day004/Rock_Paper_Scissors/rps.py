# Rock, Paper, Scissors
# Author: Powell A. Mims
# Plays rock, paper, scissors :)
import random;

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''';

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''';

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''';

print("\nI challenge you to Rock, Paper, Scissors!\n");
player_choice = int(input("Enter 0 for Rock, 1 for Paper, 2 for Scissors: "));
computer_choice = random.randint(0, 2);

choices = [rock, paper, scissors];
print("\nPlayer played:\n");
print(choices[player_choice]);
print("\nComputer played:\n");
print(choices[computer_choice]);

# Row represents computer, Column represents player,
# 1/0 represent player win/loss, 2 is tie
win_table = [
    [2, 1, 0],
    [0, 2, 1],
    [1, 0, 2]
];
condition = win_table[computer_choice][player_choice];

outcomes = [
    "Player loses :(",
    "Player wins!",
    "It was a tie!"
];
print(f"\n{outcomes[condition]}\n");
