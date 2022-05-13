import time
import random


enemy = ''
enemyLists = ['pirate', 'troll', 'lion', 'leopard']
weapon = 'dagger'


# Combining print and pause time
def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


# geting user input
def get_input(prompt, values):
    while True:
        selection = input(prompt).lower()
        if selection in values:
            return selection


# User wants to play again
def play_again():
    selection = get_input("Would you like to play again? (y/n)\n", ['y', 'n'])
    if selection == 'y':
        global weapon
        print_pause("Excellent! Restarting the game...")
        weapon = 'dagger'
        start_game()
    else:
        finish_game()


# User selecting choice
def my_choice():
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    house_weapon()


# User to enter house or select weapon
def house_weapon():
    selection = get_input("Please enter 1 or 2.\n", ['1', '2'])
    if selection == '1':
        house()
    else:
        change_weapon()


# User choosing house
def house():
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens and out steps a "
                + enemy + ".")
    print_pause("Eep! This is the " + enemy + "'s house!")
    print_pause("The " + enemy + " attacks you!")
    fight_or_run()


# User decides to fight or run
def fight_or_run():
    selection = get_input("Would you like to (1) fight or (2) run away?\n",
                          ['1', '2'])
    if selection == '1':
        fight()
    else:
        run_away()


# User decides to fight
def fight():
    if weapon == 'sword':
        print_pause("As the " + enemy + " moves to attack, you unsheath" +
                    " your new " + weapon + ".")
        print_pause("The " + weapon + " of Ogoroth shines brightly in your" +
                    " hand as you brace yourself for the attack.")
        print_pause("But the " + enemy + " takes one look at your shiny" +
                    " new toy and runs away!")
        print_pause("You have rid the town of the " + enemy +
                    ". You are victorious!")
    else:
        print_pause("You do your best...")
        print_pause("But your " + weapon + " is no match for the "
                    + enemy + ".")
        print_pause("You have been defeated!")
    play_again()


# User decides to run
def run():
    print_pause("You run back into the field. Luckily, you don't seem to" +
                " have been followed.")
    my_choice()


# User decides to change weapon
def change_weapon():
    global weapon
    print_pause("You peer cautiously into the cave.")
    if weapon == 'sword':
        print_pause("You've been here before, and gotten all the" +
                    " good stuff. It's just an empty cave now.")
    else:
        print_pause("It turns out to be only a small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You discard your silly old " + weapon +
                    " and take the sword with you.")
        weapon = 'sword'
    print_pause("You walk back out to the field.")
    my_choice()


# Game finishes
def finish_game():
    print("Thanks for playing! See you next time.")


# Introduction to the game
def start_game():
    global enemy
    enemy = random.choice(enemyLists)
    print_pause("You find yourself standing in an open field, filled" +
                " with grass and yellow widlflowers.")
    print_pause("Rumor has it that a " + enemy + " is somewhere around" +
                " here, and has been terrifying the nerby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very effective)"
                + " " + weapon + ".")
    my_choice()


start_game()
