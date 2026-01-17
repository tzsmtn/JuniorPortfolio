############################################################
#  FUNCTIONS ARCADE â€” COLLABORATIVE PROJECT (2025)
#  Instructions:
#  1. DO NOT DELETE anyone else's code.
#  2. Write your game inside your own section only.
#  3. Each student MUST add a comment block like this:
#
#  ########################################################
#  # Name: (Your Name)
#  # Game Title: (Name of your game)
#  # Description: (1â€“2 sentences)
#  ########################################################
#
#  4. Comment your code clearly.
#  5. At the bottom, add your button to the menu.
############################################################

import random
import time
import simplegui

# ---------------------------------------------------------
#                 WELCOME SCREEN
# ---------------------------------------------------------

def draw(canvas):
    canvas.draw_text("Welcome to the Functions Arcade!", [20,70], 22, "Red")
    canvas.draw_text("Select a game to play", [40,110], 20, "Red")

# ---------------------------------------------------------
#  STUDENT GAME SECTION 1
#  (Student edits ONLY this section)
# ---------------------------------------------------------


########################################################
# Name: Tenzin Samten
# Game Title: choice game
# Description: player has to choose between two different things to progress
########################################################

def coin_game():
    print("Welcome to the coin flip game")
    print("=" * 50)
    
    score = 0
    round_s = 5
    
    # game rules
    print("You have " + str(round_s) + " rounds to get as many points as possible!")
    print("Each correct guess: 10 pts\nEach wrong guess: -5 pts\n")
    
    # round number
    for round_num in range(1, round_s + 1):
        print("---- Round " + str(round_num)+ " ----")
        # Player guess
        guess_ = input("Enter h for heads or t for tails")
        # Coin flip
        random_ = random.randint(0,1)
    
        if random_ == 0 :
            result = "Heads"
        else:
            result = "Tails"
         
        # Check if guess is correct
        if guess_ == "h" and random_ == 0:
            score= score + 10
            print("Result: " + result+ " - Correct! + 10 points")
        elif guess_ == "t" and random_ == 1:
            score= score + 10
            print("Result: " + result+ " - Correct! + 10 points")
        else:
            score = score - 5
            print("Result: " + result + " x Wrong! -5 points")
    print("=" *50)       
    print("Game over!")
    print("Final score: " + str(score) + " points")

    
# ---------------------------------------------------------
#      ðŸŽ¯ START YOUR GAMES BELOW â€” ONE PER STUDENT
# ---------------------------------------------------------

# ---------------------------------------------------------
#  STUDENT GAME SECTION 2
#  (Student edits ONLY this section)
# ---------------------------------------------------------


########################################################
# Name: Akash Khelawan 
# Game Title: Guess The Number-Mini game 
# Description:Guess The number secret number with hints and 3 tries 
########################################################


# Write your game function here:
'''
def number_game():
    # guessing the number between 1 to 100
    secret = random.randint(1, 100)
    
    print("welcome to my guessing game")
    print("I am thinking of a number between 1 and 100")
    print("you may ask 3 yes/no questions then you get 3 guesses.")
    
    # ask the yes/no questions
    for i in range(3):
        question = input("ask a yes/no question:!! ")
        
        # yes/no answer 
        answer = random.randint(0, 1)
        if answer == 1:
            print("yes.")
        else:
            print("no.")
    print("--------------------------------")
    print("Now you get 3 guesses!!")
    
    # 3 guesses to find the secret number
    for i in range(3):
        guess = int(input("your guess: "))
        
        if guess == secret:
            print("you got it! hoorayyðŸ¥³ðŸ¥³ðŸ¥³ðŸ¥³ðŸ¥³ðŸ¥³")
        elif guess < secret:
            print("Too low!")
        else:
            print("Too high!!")
    
    print("out of guesses, well the number was " + str(secret))
'''
                              
                    
                    

# ---------------------------------------------------------
#  STUDENT GAME SECTION 3
# ---------------------------------------------------------


########################################################
# Name:Sadiya Hosein 
# Game Title: Choose Your Own Path! - Mini Story
# Description: The user will be able to go through scenarios of their choice and make their own decisions through the given options. 
########################################################


# Write your game function here:
def mini_game():
    print("Welcome to your own story!")
    print("Together we will go through scenarios to create a story of your own")
    print("\n")

    #Beginner Page
    print("Welcome to the Island Story!")
    print("\n")
 
    #Island Story
    l1 = "Your plane just crashed on a deserted island. \nYou're the only survivor"
    l2 = "What is your first step?"
    print(l1 + "\n"+ l2)
    steps = ["Gather resources" , "Gather food" , "Find shelter" , "Secure fresh water" , "Create a fire" , "Signal for rescue"]
    l3 = input("What is your first step? Gather resources or gather food?")
    if l3 == "Gather resources" or l3 == "gather food" or l3 == "gather resources" or l3 == "Gather food":
        print("Good choice! Here should be your next steps.")
    for x in range(6):
        print(steps[x])
    print("\n")
    
    #Snake conflict
    print("OH MY GOD!!! Theres a venemous snake within 10 feet of you! \n What are you going to do! Kill it or avoid it?")
    l4 = input("Hurry!! Kill it or avoid it!")
    if l4 != "Avoid it" or l4 != "avoid it": 
        print("Okay quick!! \n Try not to touch it but smash it with anything heavy you can find!")
    elif l4 != "Kill it" or l4 != "kill it":
        print("Okok, good choice as well. Move as far away from it as your possibly can without getting yourself into further danger.")
    else: 
        print("You have to do something!")
    print("\n")
    
    #Food situation
    l5 = input("Have you gathered food? Yes or No")
    if l5 == "Yes" or l5 == "yes":
        print("Good job! Make a comfortable shelter out of resources you gathered earlier")
    elif l5 != "Yes" or l5 != "yes":
        print("You have to do it right now!!! The sun is setting!")
 
    #Rescue prep 
    print("\n")
    print("It's far after sunset...")
    print("It's pitch black.\nWe need to start a fire in case a plane or ship comes by!")
    l6 = input("Is there enough wood to make a fire? Yes or No")
    if l6 == "Yes" or l6 == "yes":
        print("Good job! \nRub two sticks together until it sparks and place it ontop the pile of wood")
    if l6 != "Yes" or l6 != "yes":
        print("Search in a nearby area for wood. \nThen, rub two of sticks together until it sparks and place it on top of the pile of the other woods")
        print("Now there's more hope for a ship or plane to notice you.")
    print("\n")

    #Getting rescued 
    print("Its 3:08 am...A ship passes by and notices your fire while you are asleep")
    print("The ship is too big to come close to the island without hurting you, so the captain calls the Coast Guard")
    print("The Coast Guard shows up to rescue you at 4:23 am.")
    print("They bring you into their plane and cover you in a blanket and feed you bread and vegetables")
    print("At 10:46 am, you board a last minute plane home after talking answering so many questions")
    print("You enter your house at 2:51 pm and you finally feel safe.")
    
 # ---------------------------------------------------------
#  STUDENT GAME SECTION 4
# ---------------------------------------------------------


########################################################
# Name:Marquice Broderick
# Game Title: Nations Hangman
# Description: You will be given a nation adn you will have to spell the nations name .
########################################################


# Write your game function here:   
def hang_man():
    import random
    words = ["Barbados", "Brazil", "Samoa", "Seychelles", "Thailand"]
    word = random.choice(words)
    wrd_guesses = []
    added = ["_"] * len(word)
    count_turn = 1
    max_turns = 10
    wrong_try = 0

    while count_turn <= max_turns:  # Change here: count_turn should go up to max_turns
        print("Turn " + str(count_turn))  # Fixed this line to properly display the current turn number

        for letter in added:
            print(letter, end=" ")
        print()
        
        print("Guessed letters so far:", end=" ")
        for letter in wrd_guesses:
            print(letter, end=" ")
        print()

        guess = input("Guess a letter: ")  
        
        if len(guess) != 1:
            print("Please enter only one letter.")
            continue  # Add continue to skip the rest of the loop and go to the next turn

        if guess in wrd_guesses:
            print("You've already guessed " + str(guess) + ". Try again.")
            continue  # Skip the rest of the loop if the guess was already made

        wrd_guesses.append(guess)
        found = False
        for i in range(len(word)):
            if word[i] == guess:
                added[i] = guess  
                found = True

        if found:
            print("Good guess! " + str(guess) + " is in the word.")
        else:
            print("Oops! " + str(guess) + " is not in the word.")
            wrong_try += 1

        if "_" not in added:
            print("Congratulations! You've guessed the word: " + str(word))
            # End the game if the word is guessed right or wrong 

        if wrong_try == max_turns:
            print("Game over! The word was: " + word)
           

        count_turn += 1  # Increment turn count after each round

# Start the game
# ---------------------------------------------------------
#  STUDENT GAME SECTION 5
# ---------------------------------------------------------


########################################################
# Name: Kashfia Nayim
# Game Title: Rock - Paper - Scissors 
# Description: Play either rock, paper, or scissors and see if you win!
########################################################


# Write your game function here:

import random

def rps_game():
# Allows player to choose how many rounds
    rounds = int(input("How many rounds do you want to play?"))
# Ensures player selects a playable amount of rounds
    if rounds != 0:
# Repeats rounds for the number player selected
        for x in range(rounds):
# Computer randomly selects an integer from 1-3 (Inclusive) which each number correlating to a game choice
            decide = random.randint(1,3)
# Code block for computer choosing 1 (rock)
            if decide == 1:
                choice = input("rock paper scissors say shoot!")
                if choice == "rock" or choice == "Rock" or choice == "ROCK":
                    print("I play: rock")
                    print("You play: rock")
                    print("It's a tie!")
                elif choice == "paper" or choice == "Paper" or choice == "PAPER":
                    print("I play: rock")
                    print("You play: paper")
                    print("You win!")
                elif choice == "scissors" or choice == "scissor" or choice == "Scissors" or choice == "Scissor" or "SCISSORS" or "SCISSOR":
                    print("I play: rock")
                    print("You play: scissors")
                    print("You lose!")
                else:
                    print("Not valid input!")
# Code block for computer choosing 2 (paper)
            elif decide == 2:
                choice = input("rock paper scissors say shoot!")
                if choice == "rock" or choice == "Rock" or choice == "ROCK":
                    print("I play: paper")
                    print("You play: rock")
                    print("You lose!")
                elif choice == "paper" or choice == "Paper" or choice == "PAPER":
                    print("I play: paper")
                    print("You play: paper")
                    print("It's a tie!")
                elif choice == "scissors" or choice == "scissor" or choice == "Scissors" or choice == "Scissor" or choice == "SCISSORS" or choice == "SCISSOR":
                    print("I play: paper")
                    print("You play: scissors")
                    print("You win!")
                else:
                    print("Not valid input!")
# Code block for computer choosing 3 (scissors)
            else:
                choice = input("rock paper scissors say shoot!")
                if choice == "rock" or choice == "Rock" or choice == "ROCK":
                    print("I play: scissors")
                    print("You play: rock")
                    print("You win!")
                elif choice == "paper" or choice == "Paper" or choice == "PAPER":
                    print("I play: scissors")
                    print("You play: paper")
                    print("You lose!")
                elif choice == "scissors" or "scissor" or "Scissors" or "Scissor" or "SCISSORS" or "SCISSOR":
                    print("I play: scissors")
                    print("You play: scissors")
                    print("It's a tie!")
                else:
                    print("Not valid input!")
    else:
        print("Not valid input!")
# ---------------------------------------------------------
#        MENU (ADD YOUR GAME BUTTON HERE)
# ---------------------------------------------------------

frame = simplegui.create_frame("Functions Arcade", 300, 200)
frame.set_draw_handler(draw)

# â¬‡ï¸ Students must add one line in this section only â¬‡ï¸
# Example:
# frame.add_button("Example Game", example_game)
                              
frame.add_button("Rock Paper Scissors", rps_game)
frame.add_button("Island Story Minigame", mini_game)
frame.add_button("Coin flip", coin_game)
frame.add_button("Nations Hangman", hang_man)
frame.start()