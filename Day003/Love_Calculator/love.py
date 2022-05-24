# Leap Year
# Author: Powell A. Mims
# This program calculates a love score based on two names

print("\nWelcome to the Love Calculator!\n");

name_1 = input("What is the first person's name? ").lower();
name_2 = input("What is the other person's name? ").lower();
name_combo = name_1 + name_2;

t_count = name_combo.count("t");
r_count = name_combo.count("r");
u_count = name_combo.count("u");
l_count = name_combo.count("l");
o_count = name_combo.count("o");
v_count = name_combo.count("v");
e_count = name_combo.count("e");

score_left = t_count + r_count + u_count + e_count;
score_left = str(score_left);
score_right = l_count + o_count + v_count + e_count;
score_right = str(score_right);
score = score_left + score_right;
score = int(score);

message = f"Your score is {score}."
if score < 10 or score > 90:
    message += " You go together like coke and mentos!";
elif score >= 40 and score <= 50:
    message += " You are alright together.";

print(f"{message}\n");
