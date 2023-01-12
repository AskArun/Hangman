################################################
# A basic game that uses the turtle module to  #
# animate an ambulance for the wrong guesses   #
# made by the user trying to guess the other   #
# players word. A game known as Guess The      #
# Word.                                        #
# Additional Features:                         # 
#   - 1 Player Mode.                           # 
#   - More Attempts.                           # 
#   - Score System.                            # 
#   - Player Names.                            # 
#   - Prevention Of Repeating Characters.      # 
#   - Prevention Of The Input Length Being     #
#     Greater Than The Word To Be Guessed.     #
#   - Prevention Of Empty Strings.             #
#   - Prevention Of Inputs Other Than Letters  # 
#                                              #   
# Developer: 18016995                          #
# Date of creation: 30/03/2020                 #
# Date of last modification: 18/04/2020        #
#                                              #
################################################

################################################
# Declaration/Importing the turtle module and  #
# random module which will be used later on.   #
# Turtle is for the animation created.         # 
# Random used to select a random word from a   # 
# predefined list.                             #
################################################
import turtle
import random

################################################
# Creating the 7 turtles to be used            #
# throughout the program                       #
################################################
Ambulance = turtle.Turtle() # Turtle that controls the animation sequences of the ambulance.
Attempt = turtle.Turtle() # Turtle that controls the animation of the guesses that player 2 has left.
CorrectChar = turtle.Turtle() # Turtle that controls the animation of printing the masked and letters guessed correctly to the turtle screen.
PlayerScore = turtle.Turtle() # Turtle that controls the display/animation of the players score.
Title = turtle.Turtle() # Turtle that will control the display/animation of the Guess the word title in the turtle window.
WinLose = turtle.Turtle() # Turtle that controls the display/animation of the Win/Lose messages.
WrongGuesses = turtle.Turtle() # Turtle that controls the display of the wrong guesses made.

ScoreP1 = 0 # Player 1's Score counter.
ScoreP2 = 0 # Player 2's Score counter.

################################################
# Module/Function that sets up the turtle      #
# screen with the default messages.            #
################################################
def main():
    
    # The code below hides the turtles in the turtle window.
    WrongGuesses.hideturtle()
    WinLose.hideturtle()
    PlayerScore.hideturtle()

    # The code below changes the turtles color and pensize to make the turtle window more appealing.
    Ambulance.color("blue") # Changes the color of the turtle to blue
    Ambulance.pensize(3) # Sets the line size of the turtle to 3
    WrongGuesses.color("green") # Changes the color of the turtle to green.
    Title.color("blue") # Changes the color of the turtle to blue

    turtle.title("18016995's Guess The Word Game!") # Changes the the name of the titlebar to "18016995's Guess The Word Game!"
    turtle.setup(width=500, height=600, startx=-10, starty=-40) # Setup of the turtle window. Size of the window is 500 by 600 and starting position is (-10,-40)
    turtle.bgcolor("yellow") # Sets the background colour of the turtle shell to yellow
    turtle.hideturtle()
    
    Title.hideturtle() # Hides the turtle icon from the screen.
    Title.up() # Lifts the turtle/pen up so no drawing happens when movement occurs. 
    Title.goto(-70,250) # Moves the turtle to the coordinates (-70,250).
    Title.write("Guess The Word: ", align = "right", font = ("Arial", 15, "italic")) # Displays in the turtle window "Guess The Word: " in Arial font of size 15 in italics where the text is aligned to meet the left hand side of the screen. 
    Title.down() # Places the turtle/pen down so drawing can occur.
    
    Attempt.hideturtle()
    Attempt.up()
    Attempt.goto(0,-210) # Moves the turtle to the coordinates (0,-210).
    Attempt.write("You have 15 Attempts Remaining",align = "center", font = ("Arial", 15, "bold")) # Displays "You have 14 Attempts Remaining" in the turtle window centered in arial fnt of size 15 and bold.
    Attempt.down()
    
    Choice() # Calls the Choice function/module to be run so the user can select which game mode to play in.

################################################
# Module/Function that prompts the user to     #
# enter the 1 player or 2 player game mode.    #
################################################
def Choice():
    
    for line in range(50): # for loop that prints blank lines so that console is more pleasing to look at.
        print("\n") # Prints a blank line.

    print("------------------------ Game Mode ------------------------\n") # Improves aesthetics of the console screen.
    
    Choose = str(input("\n1 Player Mode \n\n     OR \n\n2 Player Mode \n\n[Type '1' For 1 Player OR '2' For 2 Player]: ")) # Prompts the user to enter whether they want to enter 1 player mode or 2 player mode.String conversion used so that the cannot enter letters and be thrown an error.
    
    loop = True # Variable that controls the while loops iterations.
    while (loop == True): # While that keeps repeating until the user enters the correct response.
        if (Choose == "1"): # If the player/user enters 1 the program executes the code below. The player selects 1 player mode.
            OnePlayer() # Calls the 1Player function/module to be run.
            loop = False # Ends the loop by setting the value to false.
        elif (Choose == "2"): # If the player/user enters 2 the program executes the code below. The player selects 2 player mode.
            TwoPlayer() # Calls the 2Player module/function to run.
            loop = False
        else: # If the requred input is not entered the following code is executed.
            Choose = str(input("\nType '1' For 1 Player OR '2' For 2 Player: ")) # Asks the user to enter '1' or '2'.

################################################
# Module/Function for the 2 Player Version of  #
# the Guess The Word game.                     #
# Also controls the animation of the           #
# ambulance.                                   #
################################################
def TwoPlayer():
    
    PlayerScore.clear() # Clears the turtle that displays the players score in two player mode.

    AlphaLetter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] # Variable that stores the alphabet which will be used to check that the user enters a letter and not numbers or symbols.
    
    Guess = 15 # Variable that controls the while loop for how many guesses the player/user gets.
    J = 240 # Variable that sets the x coordinate so that the animation of displaying incorrect guesses can be placed in line with the title.
    Incorrect = 0 # Variable that counts the number of incorrect inputs made by the player/user.
    x = 0 # Variable that is incremented to go through a list which retrieves the incorrect inputs to be displayed to the screen.
    
    GuessList = [] # List that contains the word that player 1 has entered.
    IncorrectList = [] # List that stores all the incorrect inputs made by the user.
    GameControl = [] # List that stores all the correct user inputs made.
    
    global ScoreP1 # Allows the variable to be used in this module as is global which is used to display the score of player 1 and also be used to make calculations.
    global ScoreP2 # Allows the variable to be used in this module to display the score of player 2 and also do calculations.
    global PointP1 # Globalizes the declared variable to be used thrughout the module/function to display the points that Player 1 has.
    global PointP2 # Globalizes the declared variable to be used thrughout the module/function to display the points that Player 12 has.

    for line in range(50): # for loop that prints 50 blank lines to clear the console screen.
        print("\n") # Prints blank lines.

    print("------------------------ Player Name ------------------------\n") # heading to make the console more appealing.

    Player1 = str((input("\nPlayer 1 Enter Your Name: ").lower()).capitalize()) # input that requires player 1 to enter the name for the game ,which is put into lowercase and capitalized, stored in the variable named "Player1".
    Player2 = str((input("\nPlayer 2 Enter Your Name: ").lower()).capitalize()) # input that requires player 2 to enter the name for the game ,which is put into lowercase and capitalied, stored in the variable named "Player2".

    PlayerScore.up()
    PlayerScore.goto(0,-260) # Sends the turtle to the coodinates (0,-260).
    PlayerScore.write(Player1 + ": " + str(ScoreP1) + "\n" + Player2 + ": " + str(ScoreP2), align = "center", font = ("Arial", 15, "bold")) # Displays the players score and points if two player mode is selected.
    PlayerScore.down()

    for line in range(50):
        print("\n")
        
    print("------------------------ Player 1: " + Player1 + " ------------------------\n") # Improve the look of the console screen.
    print("[Make Sure Player 2 is not peaking!!!]") 
    
    Word = list(input("\n" + Player1 + " Enter Your Word [If Your Word Has A Space, Use '-' , e.g. bus-stop]: ").lower()) # Asks player 1 to input a word which is put into lowercase if the user puts capitals and stored as a list in the variable named "word".

    for line in range(50):
        print("\n")

    print("------------------------ Player 2: " + Player2 + " ------------------------\n") # Improve the look of the console screen.

    while (Guess > 0): # while loop for the guesses made by the user.
        
        Fail = 0 # Variable that tells the program that the user/player has won
        L = 225 # Variable that sets the x coordinate of the masked/correct character so that it is in line with the Heading
        
        CorrectChar.clear() # Clears the CorrectChar turtle which shows the masked/correct character on the screen 
        
        for Character in Word: # For loop that goes through the characters in the word the user/player inputs.
            
            if (Character in GuessList): # If a character of the word is in the list "GuessList" then execute the code below.
                
                CorrectChar.hideturtle()
                CorrectChar.up()
                CorrectChar.goto(-L,200) # Sends the turtle to the coordinates (-L,200) where L is changing to prevent overlap.
                CorrectChar.write(str(Character), align = "center", font = ("Arial", 20, "bold")) # Replaces the masked character with the correct character guessed. 
                CorrectChar.down()
                
            else: # If the guess is not in the word then the code below is executed.
                
                CorrectChar.hideturtle()
                CorrectChar.up()
                CorrectChar.goto(-L,200) # Sends the turtle to the coordinates (-L,200) where L is changing so that the characters are in a row and not overlapping.
                CorrectChar.write("*", align = "center", font = ("Arial", 20, "bold")) # If the character is not guessed then the program displays "*".
                CorrectChar.down()
                
                Fail += 1 # Variable that is incremented if the user does not get it right so that the program knows when the user has won/lost.
            L -= 20 # Translates the next characters so they are in a row next to each other. Also preventing overlapping of characters.
                
        if (Fail == 0): # If the user correctly guesses the word then Fail variable is not incremented so the code below is executed.
            ScoreP2 += 1 # Increments Variable if player 2 guesses the word
            Win() # Calls and executes the "Win" module/function.
            
        GuessLetter = str(input("\n" + Player2 + " Guess A Letter: ").lower()) # User/Player is prompted to guess a letter.
        
        LenOfGuess = len(GuessLetter) # Determines the length of the user input
        LenOfWord = len(Word) # Length of the word Player 1 has inputed.
        OED = True # Variable that controls the loop. Named OED as abbreivates to Oversized,Empty and Duplicate.
        while (OED == True): # While loop iterates if the user enters a word too long, already guessed a word/letter or nothing entered 
            if (LenOfGuess > LenOfWord): # If the guess is longer than the word the code below is executed.
                GuessLetter = str(input("\n[The word is "+LenOfWord+" characters]\nGuess a Letter: ").lower()) # Asks user to enter a word/letter that is less than the word size and displays the characters in the word in the console.
                LenOfGuess = len(GuessLetter) # Reevaluates the length of the guess so can it can be rechecked
            elif ((GuessLetter in GuessList) and (GuessLetter in IncorrectList)): # If the letter/word has already been guessed the code below is executed.
                GuessLetter = str(input("\n[Letter Already Guessed Try Again]\n Guess A Letter: ").lower()) # Asks user to enter a word/letter that hasnt been guessed.
                GuessList += GuessLetter # Adds the new guess into the guess list
            elif (GuessLetter == ""): # If the User enters an empty string then the code below is executed. 
                GuessLetter = str(input("\n[You Have Not Entered A Letter]\nGuess A Letter: ").lower()) # asks for user to input a letter/word.
            elif ((GuessLetter not in AlphaLetter) and (LenOfGuess == 1) and (GuessLetter not in Word)): # If the user enters a number or symbol the code below is executed.
                GuessLetter = str(input("\n[You Have Not Entered A Valid Letter]\nGuess A Lettter: ").lower()) # Asks user to enter a letter.
            else: # If all the parameters are met the code below is executed.
                GuessList += GuessLetter # Adds the guess made to the guess list
                OED = False # Breaks the loop.

        GameControl.clear() # Clears the list for the next input.
        for WordLetters in Word: # For Loop that goes through the word.
            if WordLetters in GuessList: # If the letter is in the list of guesses the code below is executed.
                GameControl += WordLetters # If the letter is found then the letter is put into the GameControl list. 
        
        if ((GuessLetter not in Word) and (GameControl != Word)): # If the letter guessed is not in the word and the word is not completed yet that Player 1 entered the code below is executed.
            
            Guess -= 1 # As this is a failed attempt the guess counter is decremented.
            WrongGuesses.up()
            WrongGuesses.goto(-80,-120) # Translates the turtle to the coordinates (-80,-120).
            WrongGuesses.write("Wrong Guesses:\n ", align = "right", font = ("Arial", 15)) # Displays the heading wrong guesses onto the turtle screen.
            WrongGuesses.down()
            
            if (len(GuessLetter) == 1): # If the lenghth of the user input is 1 the code below is executed
                
                
                IncorrectList += GuessLetter # The incorrect letter/guess is stored in the IncorrectList List.
                J -= 30 # Changes the value of J so that the incorrect guesses can be placed in a row.
                
                WrongGuesses.hideturtle()
                WrongGuesses.up()
                WrongGuesses.goto(-J,-120) # Translates the turtle to the coodinates (-J,-150) where J is changing to prevent overlap of the letters
                WrongGuesses.write(str((IncorrectList[x])), align = "center", font = ("Arial", 15)) # Displays the incorrect guesses under the heading wrong guesses.
                WrongGuesses.down()

                x += 1 # Increments x every inorrect guess to retrieve the correct incorrect guess the user enters.
                Incorrect += 1 # Controls the animation of the ambulance as each incorrect guess increments the counter displaying a different part of the ambulance ech incorrect guess.
                

            else: # If the length is greater than 1 the code below is enteredx.
                
                J -= len(GuessLetter)*10 # Changes the value of J so that the incorrect guesses can be placed in a row
                IncorrectList += GuessLetter.split() # The incorrect letter/guess is stored as the whole word in the IncorrectList List
                
                WrongGuesses.hideturtle()
                WrongGuesses.up()
                WrongGuesses.goto(-J,-120) # Translates the turtle to the coodinates (-J,-150) where J is changing to prevent overlap of the letters
                WrongGuesses.write(str((IncorrectList[x])), align = "center", font = ("Arial", 15)) # Displays the incorrect guesses under the heading wrong guesses.
                WrongGuesses.down()
                
                x += 1 # Increments x every inorrect guess to retrieve the correct incorrect guess the user enters.
                Incorrect += 1 # Controls the animation of the ambulance as each incorrect guess increments the counter displaying a different part of the ambulance ech incorrect guess.


            Attempt.clear() # Clears the turtle Attempt which shows the attempts the user has remaining.
            Attempt.hideturtle()
            Attempt.up()
            Attempt.goto(0,-210) # Translates the turtle Attempt to the coordinates (0,-210).
            Attempt.write("You have " + str(Guess) + " Attempts Remaining",align = "center", font = ("Arial", 15, "bold")) # Displays on the turtle screen the guess attempts remaining in arial font, size 15 and bold which is centrally alligned.
            Attempt.down()
            
            if (Incorrect == 1): # If Incorrect is 1 then it will display the first part of the ambulance
                P1() # Calls the first Part of the ambulance to be drawn
            elif (Incorrect == 2):
                P2() # Calls the second Part of the ambulance to be drawn
            elif (Incorrect == 3):
                P3() # Calls the third Part of the ambulance to be drawn
            elif (Incorrect == 4):
                P4() # Calls the fourth Part of the ambulance to be drawn
            elif (Incorrect == 5):
                P5() # Calls the fifth Part of the ambulance to be drawn
            elif (Incorrect == 6):
                P6() # Calls the sixth Part of the ambulance to be drawn
            elif (Incorrect == 7):
                P7() # Calls the seventh Part of the ambulance to be drawn
            elif (Incorrect == 8):
                P8() # Calls the eighth Part of the ambulance to be drawn
            elif (Incorrect == 9):
                P9() # Calls the ninth Part of the ambulance to be drawn
            elif (Incorrect == 10):
                P10() # Calls the tenth Part of the ambulance to be drawn
            elif (Incorrect == 11):
                P11() # Calls the eleventh Part of the ambulance to be drawn
            elif (Incorrect == 12):
                P12() # Calls the twelfth Part of the ambulance to be drawn
            elif (Incorrect == 13):
                P13() # Calls the thirteenth Part of the ambulance to be drawn
            elif (Incorrect == 14):
                P14() # Calls the fourteenth Part of the ambulance to be drawn
            elif (Incorrect == 15):
                P15() # Calls the fifteenth Part of the ambulance to be drawn

            if (Guess == 0): # When the user uses all the guesses so when guess equals zero the code below is executed.
                ScoreP1 += 1 # Increments Variable if player 2 guesses the word
                Lose() # Calls the "Lose" Module/Function
                    
################################################
# Module/Function for the 1 Player Version of  #
# the Guess The Word game.                     #
# Also controls the animation of the           #
# ambulance.                                   #
################################################
def OnePlayer():

    PlayerScore.clear() # clears the player score turtles drawing from the screen.
    
    AlphaLetter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    Guess = 15 
    J = 240 
    Incorrect = 0 
    x = 0
    ran = random.randrange(7) # Variable that generates a random number to select a word randomly from the word list.
    
    
    GuessList = [] 
    IncorrectList = []
    
    WordList = ["secret","password","chocolate","banana","apple","power","television","super-mario"] # List of words that could be used in gameplay.

    Word = WordList[ran] # Selects and stores the random word in the variable named "word"

    for line in range(50):
        print("\n")

    print("------------------------ Guess A Letter ------------------------\n")

    while (Guess > 0): 
        
        Fail = 0
        L = 225
        CorrectChar.clear() 
        
        for Character in Word: 
            
            if Character in GuessList: 
                
                CorrectChar.hideturtle()
                CorrectChar.up()
                CorrectChar.goto(-L,200) 
                CorrectChar.write(str(Character), align = "center", font = ("Arial", 20, "bold"))  
                CorrectChar.down()
                L -= 20 
                
            else: 
                
                CorrectChar.hideturtle()
                CorrectChar.up()
                CorrectChar.goto(-L,200)
                CorrectChar.write("*", align = "center", font = ("Arial", 20, "bold")) 
                CorrectChar.down()
                L -= 20
                Fail += 1 
                
        if ((Fail == 0) or (Word in GuessList)): 
            Win() 
            
        GuessLetter = input("\nGuess a Letter: ").lower()
        
        LenOfGuess = len(GuessLetter)
        LenOfWord = len(Word)
        OED = True
        while OED == True:
            if LenOfGuess > LenOfWord:
                print("The word is ",LenOfWord," characters")
                GuessLetter = str(input("\nGuess a Letter: ")) 
                LenOfGuess = len(GuessLetter)
            elif ((GuessLetter in GuessList) and (GuessLetter in IncorrectList)):
                GuessLetter = str(input("\n[Letter Already Guessed Try Again]\n Guess A Letter: "))
                GuessList += GuessLetter
            elif (GuessLetter == ""): 
                GuessLetter = str(input("\n[You Have Not Entered A Letter]\nGuess A Letter: ").lower())
            elif ((GuessLetter not in AlphaLetter) and (LenOfGuess == 1) and (GuessLetter not in Word)):
                GuessLetter = str(input("\n[You Have Not Entered A Valid Letter]\nGuess A Lettter: ").lower())
            else:
                GuessList += GuessLetter 
                OED = False
        
        if GuessLetter not in Word: 
            
            Guess -= 1 
            
            WrongGuesses.up()
            WrongGuesses.goto(-80,-120) 
            WrongGuesses.write("Wrong Guesses:\n ", align = "right", font = ("Arial", 15)) 
            WrongGuesses.down()
            
            if (len(GuessLetter) == 1):
                
                
                IncorrectList += GuessLetter 
                J -= 30 
                
                WrongGuesses.hideturtle()
                WrongGuesses.up()
                WrongGuesses.goto(-J,-120) 
                WrongGuesses.write(str((IncorrectList[x])), align = "center", font = ("Arial", 15)) 
                WrongGuesses.down()

                x += 1 
                Incorrect += 1 

            else:
                
                J -= len(GuessLetter)*10 
                IncorrectList += GuessLetter.split() 
                
                WrongGuesses.hideturtle()
                WrongGuesses.up()
                WrongGuesses.goto(-J,-120) 
                WrongGuesses.write(str((IncorrectList[x])), align = "center", font = ("Arial", 15)) 
                WrongGuesses.down()
                
                x += 1 
                Incorrect += 1

            Attempt.clear() 
            Attempt.hideturtle()
            Attempt.up()
            Attempt.goto(0,-210) 
            Attempt.write("You have " + str(Guess) + " Attempts Remaining",align = "center", font = ("Arial", 15, "bold")) 
            Attempt.down()
            
            if (Incorrect == 1): 
                P1() 
            elif (Incorrect == 2):
                P2() 
            elif (Incorrect == 3):
                P3() 
            elif (Incorrect == 4):
                P4() 
            elif (Incorrect == 5):
                P5() 
            elif (Incorrect == 6):
                P6() 
            elif (Incorrect == 7):
                P7() 
            elif (Incorrect == 8):
                P8() 
            elif (Incorrect == 9):
                P9() 
            elif (Incorrect == 10):
                P10() 
            elif (Incorrect == 11):
                P11() 
            elif (Incorrect == 12):
                P12() 
            elif (Incorrect == 13):
                P13()
            elif (Incorrect == 14):
                P14() 
            elif (Incorrect == 15):
                P15() 

            if (Guess == 0): 
                ScoreP1 += 1 
                Lose() 
                
################################################
# Module/Function that controls the turtle     #
# that displays the first part of the          # 
# ambulance.                                   #
################################################
def P1():

    Ambulance.up()
    Ambulance.goto(-85,10) # Sends the turtle to the coordinates (-85,10)
    Ambulance.down()
        
    Ambulance.fillcolor("white") # Fills the shape drawn with the colour white.
    Ambulance.begin_fill() # Starts the fill command.
        
    Ambulance.hideturtle()

    for rec1 in range(2): # For loop used to reduce the amount of code written. rec1,rec2... written where there are for loops for rectangles to prevent nameclashes.  
        Ambulance.forward(95) # Moves the turtle forward 95 pixels.           
        Ambulance.left(90) # Changes the direction of the turtle to left 90.               
        Ambulance.forward(80) # Moves the turtle forward 80 pixels.            
        Ambulance.left(90)               
        
    Ambulance.end_fill() # Stops the fill command. 
        
################################################
# Module/Function that controls the turtle     #
# that displays the second part of the         # 
# ambulance.                                   #
################################################
def P2():
        
    Ambulance.up()
    Ambulance.forward(95) # Sets the position of the turtle to continue drawing.
    Ambulance.down()
        
    Ambulance.fillcolor("white") # Fills the shape drawn with the colour white.
    Ambulance.begin_fill()
        
    Ambulance.forward(60)
    Ambulance.left(90)
    Ambulance.forward(65)
    Ambulance.left(90)
    Ambulance.forward(60)
        
    Ambulance.end_fill()

    # The code below sets the turtle to the position for the next part to be drawn.
    Ambulance.up()
    Ambulance.left(90)
    Ambulance.forward(65)
    Ambulance.down()

################################################
# Module/Function that controls the turtle     #
# that displays the third part of the          # 
# ambulance.                                   #
################################################
def P3():

    # The code below sets the turtles position to draw.
    Ambulance.up()
    Ambulance.right(90)
    Ambulance.forward(35)
    Ambulance.right(90)
    Ambulance.forward(1)
    Ambulance.down()

    Ambulance.fillcolor("blue") # Fills the shape drawn with the colour blue.
    Ambulance.begin_fill()
        
    Ambulance.circle(25) # Draws one of the two circular wheels.
        
    Ambulance.end_fill()

################################################
# Module/Function that controls the turtle     #
# that displays the fourth part of the         # 
# ambulance.                                   #
################################################
def P4():

    # The code below sets the position of the turtle to begin drawing.    
    Ambulance.up()
    Ambulance.right(90)
    Ambulance.forward(85)
    Ambulance.left(90)
    Ambulance.forward(1)
    Ambulance.down()

    Ambulance.fillcolor("blue") # Fills the shape drawn with the colour blue.
    Ambulance.begin_fill()
        
    Ambulance.circle(25) # Draws the second of the two circular wheels.
        
    Ambulance.end_fill()
        
################################################
# Module/Function that controls the turtle     #
# that displays the fifth part of the          # 
# ambulance.                                   #
################################################
def P5():
        
    Ambulance.up()
    Ambulance.goto(55,65) # Sends the turtle to the coordinates (55,65).
    Ambulance.down()
        
    Ambulance.fillcolor("grey") # Fills the shape drawn with the colour grey.
    Ambulance.begin_fill()
        
    Ambulance.left(90)

    for rec5 in range(2): # For loop that draws the rectangle.
        Ambulance.forward(30)
        Ambulance.left(90)
        Ambulance.forward(15)
        Ambulance.left(90)
    
    Ambulance.right(90) # Sets the turtles position for the next drawing
        
    Ambulance.end_fill()
        
################################################
# Module/Function that controls the turtle     #
# that displays the sixth part of the          # 
# ambulance.                                   #
################################################
def P6():
        
    Ambulance.up()
        
    Ambulance.goto(-45,55) # Sends the turtle to the coordinates (-45,55).
    Ambulance.fillcolor("red") # Fills the shape drawn with the colour red.
    Ambulance.begin_fill()
        
    Ambulance.right(90)
        
    for rec6 in range(2): # For loop that draws the rectangle.
        Ambulance.forward(30)
        Ambulance.left(90)
        Ambulance.forward(15)
        Ambulance.left(90)
            
    Ambulance.right(90) # Sets the turtles position for the next drawing
    Ambulance.end_fill()
        
    Ambulance.down()
        
################################################
# Module/Function that controls the turtle     #
# that displays the seventh part of the        # 
# ambulance.                                   #
################################################
def P7():
        
    Ambulance.up()
    Ambulance.goto(-37.5,77.5) # Sends the turtle to the coordinates (-37.5,77.5).
        
    Ambulance.fillcolor("red") # Fills the shape drawn with the colour red.
    Ambulance.begin_fill()
    Ambulance.left(90)

    for rec7 in range(2): # For loop that draws the rectangle.
        Ambulance.forward(15)
        Ambulance.right(90)
        Ambulance.forward(30)
        Ambulance.right(90)
            
    Ambulance.left(90) # Sets the turtle up for the next drawing to occur.
    Ambulance.end_fill()
        
    Ambulance.down()
        
################################################
# Module/Function that controls the turtle     #
# that displays the eighth part of the         # 
# ambulance.                                   #
################################################
def P8():
        
    Ambulance.up()
    Ambulance.goto(-37.5,90) # Sends the turtle to the coordinates (-37.5,90).
    Ambulance.down()
        
    Ambulance.fillcolor("red") # Fills the shape drawn with the colour red.
    Ambulance.begin_fill()
        
    Ambulance.forward(10)
    Ambulance.right(90)
    Ambulance.forward(15)
    Ambulance.right(90)
    Ambulance.forward(10)
        
    Ambulance.end_fill()
        
################################################
# Module/Function that controls the turtle     #
# that displays the ninth part of the          # 
# ambulance.                                   #
################################################
def P9():
    
    Ambulance.up()
    Ambulance.goto(-85,10) # Sends the turtle to the coordinates (-85,10).
    Ambulance.down()
    Ambulance.fillcolor("black") # Fills the shape drawn with the colour black.
    Ambulance.begin_fill()
    
    for rec9 in range(2): # For loop that draws the rectangle.
        Ambulance.right(90)
        Ambulance.forward(8)
        Ambulance.right(90)
        Ambulance.forward(11)
        
    Ambulance.left(90) # Sets the turtle to the position for the next drawing
    
    Ambulance.end_fill()
    
################################################
# Module/Function that controls the turtle     #
# that displays the tenth part of the          # 
# ambulance.                                   #
################################################
def P10():

    Ambulance.up()
    Ambulance.goto(-85,90) # Sends the turtle to the coordinates (-85,90).
    Ambulance.down()
    
    Ambulance.fillcolor("red") # Fills the shape drawn with the colour red.
    Ambulance.begin_fill()
    Ambulance.right(90)
    Ambulance.forward(10)
    
    for sqr10 in range(4): # For loop that draws the square.
        Ambulance.left(90)
        Ambulance.forward(10)
    Ambulance.end_fill()
    
################################################
# Module/Function that controls the turtle     #
# that displays the eleventh part of the       # 
# ambulance.                                   #
################################################
def P11():

    Ambulance.up()
    Ambulance.goto(10,90) # Sends the turtle to the coordinates (10,90).
    # The code below sets the turtle in the correct location for the shape to be drawn
    Ambulance.right(90)
    Ambulance.forward(10)
    Ambulance.down()
    
    Ambulance.fillcolor("red") # Fills the shape drawn with the colour red.
    Ambulance.begin_fill()
    
    for sqr11 in range(4): # for loop used to iterate the lines of code below to make a square
        Ambulance.left(90)
        Ambulance.forward(10)
    Ambulance.end_fill()
    
################################################
# Module/Function that controls the turtle     #
# that displays the twelfth part of the        # 
# ambulance.                                   #
################################################
def P12():
    
    Ambulance.up()
    Ambulance.goto(-1,118) # Sends the turtle to the coordinates (-1,118).
    Ambulance.down()
    Ambulance.fillcolor("blue") # Fills the shape drawn with the colour blue.
    Ambulance.begin_fill()
    Ambulance.left(50)# Sets the turtle to an angle so the shape can be drawn in that angle.

    for rec12 in range(2): # For loop that draws the rectangle
        Ambulance.forward(20)
        Ambulance.right(90)
        Ambulance.forward(10)
        Ambulance.right(90)
    
    Ambulance.left(90)

    Ambulance.end_fill()
    
################################################
# Module/Function that controls the turtle     #
# that displays the thirteenth part of the     # 
# ambulance.                                   #
################################################
def P13():
    
    Ambulance.up()
    Ambulance.goto(-55,120) # Sends the turtle to the coordinates (-55,120).
    Ambulance.down()
    Ambulance.fillcolor("blue") # Fills the shape drawn with the colour blue.
    Ambulance.begin_fill()

    for rec13 in range(2): # For loop that draws the rectangle.
        Ambulance.forward(20)
        Ambulance.right(90)
        Ambulance.forward(10)
        Ambulance.right(90)

    Ambulance.left(90) # Sets the turtles position so that the next part can be drawn.
    
    Ambulance.end_fill()
    
################################################
# Module/Function that controls the turtle     #
# that displays the fourteenth part of the     # 
# ambulance.                                   #
################################################
def P14():
    
    Ambulance.up()
    Ambulance.goto(-37.5,110) # Sends the turtle to the coordinates (-37.5,110). Setting the turtle to draw.
    Ambulance.down()
    Ambulance.fillcolor("blue") # Fills the shape drawn with the colour blue.
    Ambulance.begin_fill()

    Ambulance.left(40)

    for rec14 in range(2): # For loop that draws the rectangle.
        Ambulance.forward(20)
        Ambulance.right(90)
        Ambulance.forward(10)
        Ambulance.right(90)

    Ambulance.end_fill()

################################################
# Module/Function that controls the turtle     #
# that displays the fifteenth part of the      #
# ambulance.                                   #
################################################
def P15():

    turtle.showturtle() # Shows the turtle as the turtle becomes the image.
    turtle.up()
    turtle.goto(-72,55) # Sends the turtle to the coordinates (-72,55)
    turtle.down()
    
    turtle.addshape("Emergency.gif") # Adds a turtle shape to TurtleScreen's shapelist.
    turtle.shape("Emergency.gif") # Changes the turtle into the predetermined shape.
    
################################################
# Module/Function that controls the turtle     #
# that displays the win message                #
################################################  
def Win():

    WinLose.up()
    WinLose.goto(0,135) # Sends the turtle to the coordinates (0,135)
    WinLose.write("You Win!", align = "center", font = ("Arial", 35, "bold")) # Displays the You Win message in the turtle window if the player guesses the word correctly.
    WinLose.down()
    Restart()
    
################################################
# Module/Function that controls the turtle     #
# that displays the lose message.              #
################################################      
def Lose():
    
    WinLose.up()
    WinLose.goto(0,135) # Sends the turtle to the coordinates (0,135)
    WinLose.write("You Lose!", align = "center", font = ("Arial", 35, "bold")) # Displays the You Lose message in the turtle window if the player does not guess the word correctly.
    WinLose.down()
    Restart()
    
################################################
# Module/Function that begins the restart      #
# module which will restart the program so     # 
# that the user can play again.                #           
################################################
def Restart():
    
    Exit = str(input("\nDo You Want To Play Again[Y/N]:").lower()) # Waits for user to acknowledge message and press enter to restart the game.
    while True: # While loop that iterates until break command.
        if Exit == "y": # if the user enters 'y' or 'Y' the code below is executed.
            # The code below clears the turtles so that the next round can be played.
            Ambulance.reset() # Clears the turtle and sends the turtle back to its intial position and direction.
            Attempt.clear()
            CorrectChar.clear()
            PlayerScore.clear()
            turtle.clear()
            Title.clear()
            WinLose.clear()
            WrongGuesses.clear()
            main() # Calls the main() function/module to restart the game.
            break
        elif Exit == "n": # If the user enters 'n' or 'N' the code below is executed.
            exit() # Exits the program and kills all processes python is running.
            break 
        else: # If the user does not enter 'y' 'Y' 'n' 'N' the code below is executed
            Exit = str(input("\nType 'Y' for Yes or 'N' for No: ").lower()) # User is asked to enter a correct value which is put in lowercase.

main() # Calls the main() function/module to begin the game once all the code has been compiled.
