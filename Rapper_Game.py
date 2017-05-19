# Creating a dictionary with all key-pair values for the lyrics and rapper
#Try to make a game that you would personally like to play

#THINGS TO DO
    # Print random rap lyric
    # print random.sample(rap_pair, 1) and return random.sample(rap_pair())     
    #Don't allow duplicates in the random /shuffle option - make a list 
    #to keep track of which lyric they've already seen

    #Store high scores   

    # API from Rap Genius

    # After 10 guesses,
    # - If 0-5 out of 10 guesses right, print message
    # - If 6-7 out of 10 guesses right, print message
    # - If 8-10 out of 10 guesses right, print message

    # Prompt user if they want to play again - have a function to bring 
    #them back to the top or put the whole thing in a loop

    #add ASCII Art for when people exit the game

    # Making code easier to read, simple and utilizing what we learned during class


rap_pair = {
    "I remember syrup sandwiches and crime allowances": "kendrick lamar",
    "Percocets, molly, Percocets": "future",
    "Let the suicide doors up, I threw suicies on the tour bus": "kanye west",
    "The lonely stoner seems to free his mind at night": "kid cudi",
    "Shake it like a Polaroid picture": "outkast",
    "Pretty woman, wassup? Is you here right now? You a stand-up or is you in your chair right now?": "nicki minaj",
    # "I got hustle, though ambition flow inside my DNA": "kendrick lamar",
    # "Man, I promise I'm so self-conscious, that's why you always see me with at least one of my watched": "kanye west",
    # "I'm so heartless, thoughtless, lawless and flawless, smallest, regardless": "nicki minaj",
    # "Tell the promoter we need more seats, we just sold out all the floor seats": "nicki minaj"
        }          


def explain_game():
#add menu to start game again 

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

# Prompt user if they're ready
#     If ready, we'll start the game
#     Else, if not ready, message letting them know they can try later (break)

def execute_game():
    while True:
        ready_to_play = menu_choice()

        #Need a break statement to exit
        if ready_to_play == "exit":
            print "No problem, I hope you'll decide to come back! :)"
            break
        
        elif ready_to_play == "no":
            print "\nOkay, I understand. No pressure, just come back when you're ready\n"
            break

    # - Prompt for user inpur
    #     If correct, print message, count as 1
    #     If incorrect, print other message, count as 0
    #     Add to total score
    #     Return
    # - Repeat 5 more times

        elif ready_to_play == "yes":
            score = 0
            #Function for keeping a score: starts at zero and then increases

            for key in rap_pair:
                print key
                guess = raw_input(">>> ")

                if guess.lower() == rap_pair[key]:
                    print "\nThat's a win!"
                    score = score + 1
                    print #morespace

                elif guess = "exit"
                    break

                else:
                    print "\nI'm afraid that's the wrong guess...\n"

        else:
            print "\nSorry, I don't know what that means. Are you ready to play?\n"
            menu_choice()

#Call Function
explain_game()
execute_game()

