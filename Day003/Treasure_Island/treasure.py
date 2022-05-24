# Treasure Island
# Author: Powell A. Mims
# This program lets you play an awesome adventure game.


bad_input_message = '''A dragon flies out of the sky and lands in front of you. You try to speak to it.
It looks at you like you're stupid, then it burns you to a crisp.
You are dead.
Game Over'''

print('''
  ____________________________________________________________________
 / \\-----     ---------  -----------     -------------- ------    ----\\
 \\_/__________________________________________________________________/
 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
 |  ~ \__ (( _( (  ))  ) _)    ((     \\\\//    " |   "    \_____,' | ~|
 |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\\\ " __,---._  "  "   "  /~~~|
 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
 | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
 |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
 |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
 | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
 |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
 | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
 |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
 | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
 |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
 | ~~ ~|__,-'~~~~~\    \\"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
 |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
 |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
 / \----- ----- ------------  ------- ----- -------  --------  -------\\
 \_/__________________________________________________________________/
''');

print("\nWelcome to Treasure Island!");
print("Your mission is to find the treasure.");
print("You are at the bottom of the map.");
decision = input("Should you go left or right? (left, right) ");

if decision == "left":
    print("You walk left through a grassy area when all of a sudden the ground starts shaking.");
    print("You look around just in time to realize you are being chased by the Southern Island Troll.");
    print("You run away, but he is way to fast for you. He catches you and eats you.");
    print("You are dead.");
    print("Game Over");
    exit();
elif decision != "right":
    print(bad_input_message);
    exit();

print("You travel eastward until you end up on a beach.");
print("To the north, the terrain is too rocky to travers.");
print("To the south is empty ocean. But far off in the east, you can make out a small patch of land.");
decision = input("Should you swim or wait? (swim, wait) ");

if decision == "swim":
    print("You jump in the water and start swimming to the far off patch of land.");
    print("The water is cold, but you press on. Until you see a triangular fin zipping through the water.");
    print("Before you know it, there are three of them circling you.");
    print("The sharks eat you alive.");
    print("You are dead.");
    print("Game Over");
    exit();

elif decision != "wait":
    print(bad_input_message);
    exit();

print("You decide to wait, and before long, the eagles fly down to carry you across the mountains.");
print("They drop you off in a large grassy field, and they go off on their way to wherever they go.");
print("To the west you see a forest. To the east you see a lake.");
print("To the south, you see a path into the mountains.");
decision = input("Which way should you go? (west, east, south) ");

if decision == "west":
    print("You go west into the forest. Before long, you stumble across a cottage made of candy.");
    print("You decide to knock on the door, and when you do, you find that an old lady is already there");
    print("waiting just for you.");
    print("You go inside, and when you do, the door shuts and locks behind you.");
    print("The old lady is a witch, and she boils you alive to eat you, after stuffing you with candy first, of course.");
    print("You are dead.");
    print("Game Over");
    exit();
elif decision == "south":
    print("You climb all the way to the top of the mountain, and when you reach the summit,");
    print("you realize that you're at the top of a volcano.");
    print("As you go to turn around, you trip and fall inside.");
    print("You are dead.");
    print("Game Over");
    exit();
elif decision != "east":
    print(bad_input_message);
    exit();

print("You travel east toward the lake until you find a giant 'X' carved in the ground.");
print("You reach into your pack and pull out your shovel and start digging.");
print("You pull a large wooden box out of the ground, and inside is a key and a note.")
print("The note says, \"Here is the key to my house on the lake. The tree nearby has a fancy tire swing. Kudos.\"");
print("Congratulations, you found the treasure!");
print("You Win!");
