#Pseudo code for the Guess the Rapper terminal-based game

# Creating a dictionary with all key-pair values for the lyrics and rapper
rap_pair = {
    "I remember syrup sandwiches and crime allowances": "kendrick lamar",
    "Percocets, molly, Percocets": "future",
    "I got hustle, though ambition flow inside my DNA": "kendrick lamar",
    "Let the suicide doors up, I threw suicies on the tour bus": "kanye west",
    "Man, I promise I'm so self-conscious, that's why you always see me with at least one of my watched": "kanye west",
    "The lonely stoner seems to free his mind at night": "kid cudi",
    "Shake it like a Polaroid picture": "outkast",
    "Pretty woman, wassup? Is you here right now? You a stand-up or is you in your chair right now?": "nicki minaj",
    "I'm so heartless, thoughtless, lawless and flawless, smallest, regardless": "nicki minaj",
    "Tell the promoter we need more seats, we just sold out all the floor seats": "nicki minaj"
        }          


# - Greet user
print #space
print "Hi there! Welcome to a game of Guess the Rapper ~~~ where you will be... "
print "You guessed right! Guessing who sang what!"

# - Prompt user for name
print
print "First off, let's get to know each other. What's your name?"

user_name = raw_input(">>> " )

print

# - Welcome message to user (include name)
print "Hi ",user_name,"! Glad that you could join us."
print

# - Instructions for user about the game
#     - 15 rap lyrics will be given out
#     - User has to guess who the rapper is
#     - The game will count right guesses and let you know how close 
# you are to becoming a rapper

#FUNCTION FOR MENU
#FUNCTON FOR INCREASING THE SCORE
#FUNCTION FOR PLAYING THE GAME == starts at zero and then increases
# Making code easier to read, simple and utilizing what we learned during class

print "In this game, I'll ask you to guess the rapper behind the lyrics"
print
print "\t* I'll let you know when you've guessed right or wrong after each guess"
print
print "\t* At the end, I'll let you know how close you are to becoming a rapper"

print 
print "Are you ready to start playing? "
print "(type exit at any point if you would like to end the game)"
print

ready_to_play = raw_input(">>> ")
print

# Prompt user if they're ready
#     If ready, we'll start the game
#     Else, if not ready, message letting them know they can try later (break)

#MIGHT NEED TO ADD A WHILE LOOP
#NEED A BREAK STATEMENT TO EXIT
#ADD MENU TO START GAME AGAIN 

while True:
    
    if ready_to_play.lower() == "exit":
        break
    
    elif ready_to_play.lower() == "no":
        print "Okay, I understand. No pressure, just come back when you're ready"
        break
    #INFINITE LOOP

# - Print random rap lyric
# - Prompt for user inpur
#     If correct, print message, count as 1
#     If incorrect, print other message, count as 0
#     Add to total score
#     Return
# - Repeat 9 more times

    score = 0

    elif ready_to_play.lower() == "yes":
           
           # print random.sample(rap_pair, 1) and return random.sample(rap_pair())        

            for key in rap_pair:
                print key
                guess = raw_input(">>> ")

                if guess.lower() == rap_pair[key]:
                    print "That's a win!"
                    print #morespace

                else:
                    print "I'm afraid that's the wrong guess..."

    else:
        print "Sorry, I don't know what that means. Are you ready to play?"
        ready_to_play = raw_input(">>> ")

#Don't allow duplicates in the random /shuffle option - make a list 
#to keep track of which lyric they've already seen


#Try to make a game that you would personally like to play

# Game starts
# - ~100 rap lyrics saved in the database, different random rap lyric
# pulled up each time
# API from Rap Genius


# After 10 guesses,
# - If 0-5 out of 10 guesses right, print message
# - If 6-7 out of 10 guesses right, print message
# - If 8-10 out of 10 guesses right, print message

#(Store high scores)

# Prompt user if they want to play again - have a function to bring 
#them back to the top or put the whole thing in a loop

