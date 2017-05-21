# Creating a dictionary with all key-pair values for the lyrics and rapper
#Try to make a game that you would personally like to play
# Make sure code is easy to read, simple and utilizing what we learned during class

#THINGS TO DO
    # Print random rap lyric
    #Don't allow duplicates in the random /shuffle option - make a list 
    #to keep track of which lyric they've already seen

    # API from Rap Genius
import random

def explain_game():
    # - Greet user
    print "\nHi there!"
    print "\nWelcome to a game of Guess the Rapper ~~~ where you will be... \n"
    print "You guessed right! Guessing who sang what!\n"

    # - Prompt user for name
    print "First off, let's get to know each other. What's your name?\n"
    user_name = raw_input(">>> " )

    # - Welcome message to user (include name)
    print "\nHi ",user_name,"! Glad that you could join us.\n"

    # - Instructions for user about the game
    #     - 6 rap lyrics will be given out
    #     - User has to guess who the rapper is
    #     - The game will count right guesses and let you know how close 
    # you are to becoming a rapper

    print "In this game, I'll ask you to guess the rapper behind the lyrics"
    print
    print "\t* I'll let you know when you've guessed right or wrong after each guess"
    print "\t* At the end, I'll let you know how close you are to becoming a rapper"

#Function for menu
def menu_choice():
    print "\nAre you ready to start playing? \n"
    print "YES to start playing"
    print "NO if you wouldn't like to play"
    print "EXIT to quit\n"

    ready_to_play = raw_input(">>> ")
    return ready_to_play.lower()
            
# After 6 guesses, depending on score, print message
def message_after_game(score):

    if score <= 4:
        print "Your score is ",score, "out of 10"
        print "Oooh, it looks like you've got a long way to go to be a rapper"

    elif 4 < score < 9:
        print "Your score is ",score, "out of 10"
        print "You're so close to becoming a rapper, you just need a little more practice"

    elif score >= 9:
        print "Your score is ",score, "out of 10"
        print "You're a certified rapper, go out there and make some magic"

    else:
        print "\ncomputing error, I'm too old for this\n"

#add ASCII Art for when people exit the game
def ascii_art_exit():
    print "\nNo problem, I hope you'll decide to come back! \n"
    print "      ,o8o, ,o8o,"
    print "    ,888888,888888,"
    print "    888888888888888"
    print "    888888888888888"
    print "    `8888888888888'"
    print "      `888888888'"
    print "        `88888'"
    print "          `8' \n"

# Prompt user if they're ready
#     If ready, we'll start the game
#     Else, if not ready, message letting them know they can try later (break)

def execute_game():
    while True:
        ready_to_play = menu_choice()

        #Need a break statement to exit
        if ready_to_play == "exit":
            ascii_art_exit()
            break
        
        elif ready_to_play == "no":
            ascii_art_exit()
            break

    # Prompt for user inpur
    #     If correct, print message, count as 1
    #     If incorrect, print other message, count as 0
    #     Add to total score
    #     Return
    # Repeat 5 more times

        elif ready_to_play == "yes":
            score = 0
            #Function for keeping a score: starts at zero and then increases
            
            # Print random rap lyric
            seen_lyrics = set()
            for lyric in range(10):
                lyric = random.choice(rap_pair.keys())

                while lyric in seen_lyrics:
                    lyric = random.choice(rap_pair.keys())
                else:
                    seen_lyrics.add(lyric)
                
                print lyric
                guess = raw_input("\n>>> ")
                if guess.lower() == rap_pair[lyric]:
                    print "\nThat's a win!"
                    score = score + 1
                    print #morespace

                elif guess == "exit":
                    break

                else:
                    print "\nI'm afraid that's the wrong guess...\n"
            message_after_game(score)


        else:
            print "\nSorry, I don't know what that means. Are you ready to play?\n"
            menu_choice()


rap_pair = {
    "I remember syrup sandwiches and crime allowances": "kendrick lamar",
    "Percocets, molly, Percocets": "future",
    "Let the suicide doors up, I threw suicies on the tour bus": "kanye west",
    "The lonely stoner seems to free his mind at night": "kid cudi",
    "Shake it like a Polaroid picture": "outkast",
    "Pretty woman, wassup? Is you here right now? You a stand-up or is you in your chair right now?": "nicki minaj",
    "I got hustle, though ambition flow inside my DNA": "kendrick lamar",
    "Man, I promise I'm so self-conscious, that's why you always see me with at least one of my watched": "kanye west",
    "I'm so heartless, thoughtless, lawless and flawless, smallest, regardless": "nicki minaj",
    "Tell the promoter we need more seats, we just sold out all the floor seats": "nicki minaj"
        }          


#Call Function
explain_game()
execute_game()

