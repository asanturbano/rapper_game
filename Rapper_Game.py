#Pseudo code for the Guess the Rapper terminal-based game


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

print "In this game, I'll ask you to guess the rapper behind the lyrics"
print
print "\t* I'll let you know when you've guessed right or wrong after each guess"
print
print "\t* At the end, I'll let you know how close you are to becoming a rapper"

print 
print "Are you ready to start playing? (type exit if you would like to end the game"
print

ready_to_play = raw_input(">>> ")
print

# Prompt user if they're ready
#     If ready, we'll start the game
#     Else, if not ready, message letting them know they can try later (break)

#MIGHT NEED TO ADD A WHILE LOOP
#NEED A BREAK STATEMENT TO EXIT
#ADD MENU TO START GAME AGAIN 

if ready_to_play.isdigit():
    print "Sorry, I don't know what that means"

else:
    if ready_to_play.lower() == "yes":
        print "Go"
    elif ready_to_play.lower() == "no":
        print "Okay, I understand. No pressure, just come back when you're ready"
    else:
        print "Okay let me know"

# Game starts
# - ~100 rap lyrics saved in the database, different random rap lyric
# pulled up each time

# - Print random rap lyric
# - Prompt for user inpur
#     If correct, print message, count as 1
#     If incorrect, print other message, count as 0
#     Add to total score
#     Return
# - Repeat 14 more times

# After 15 guesses,
# - If 0-5 out of 15 guesses right, print message
# - If 6-10 out of 15 guesses right, print message
# - If 11-15 out of 15 guesses right, print message

# Prompt user if they want to play again