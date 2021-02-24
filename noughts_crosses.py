# The following lines of code import 3 modules into the program.
import random # Used to make random numbers.
import time # Used to represent time.
import sys # Used to access variables used or maintained by the interpreter.

# The following function print the current board to the command window.
def print_board(board):
    print()
    print(board[:3])
    print(board[3:6])
    print(board[6:])
    
# This function takes the existing board, position input from player,
# maker type (either x or o) and returns the updated board based on the arguments.
def draw_board(board, position, marker):
    board[position-1] = marker
    print_board(board)
    return board

# Add any other functions below for your program.

# The function below updates the board.   
def update_board():
    print_board(board)

# The following function allows a user to enter a position and,
# verify the users position is valid.
def player_input():
    loop = True 
    while(loop==True): # Starts a loop that wont end until the enterd value is valid.
        user_input = input("\nPlayer"+ str(player) +" please enter a number between 1 and 9: ") # Asks the user to enter a number between 1 & 9.
        if any(char.isdigit() for char in user_input): # Checks if the enterd value is a number.
            user_input = int(user_input) # If the entered value is a number this line converts it to an integer.
            if (user_input > 0 and user_input < 10): # Checks if the entered value is between 1 and 9.
                location = user_input - 1 # If the above condition is met the users enterd value has 1 taken away from it and is given the name location.
                if(board[location] == 'x' or board[location] == 'o'): # Checks if the location has either an x or an o in it.
                    print("This position is already taken by a player, \nPlease try a new position") # This line tells the user that that location is already taken.
                    continue # Starts the loops next iteration. 
                else:
                    location = user_input # If the entered location isn't taken then the value entered is set to the variable location.
                    loop = False # This ends the loop.
            else:
                print("Value is not a valid number, please try again.") # If the user doesn't enter a number between 1 & 9 this message is displayed.
                continue # Starts the loops next iteration.
        else:
            print("Value is not valid, please enter a number between 1 and 9.") # If the user enters a character this message is displayed.
            continue # Starts the loops next iteration.
    return location # Returns the location value that is valid.

# The following function checks the board for a win state.
def status_check(): 
    if (turns == 10): # This checks if the amount of turns has reached 10 if it has the board is full.
        print ("\nIts a draw!!\nYou filled the board.") # If the turn count has reached 10 this messaged is displayed,
        status = 2 # and the status is changed to stop the game playing.
        print("\nThe game will close in 5 sceonds") # This line informs the user that the game will close after five seconds.
        time.sleep(5) # This line pauses the program for 5 sconds before continuing.
        sys.exit # This causes the program to close without the user having to press anything.
        # Below is the wining combonations, this checks if a player has won.
    elif(board[0] == 'x' and board[1] == 'x' and board[2] == 'x' or board[0] == 'o' and board[1] == 'o' and board[2] == 'o' or 
         board[3] == 'x' and board[4] == 'x' and board[5] == 'x' or board[3] == 'o' and board[4] == 'o' and board[5] == 'o' or 
         board[6] == 'x' and board[7] == 'x' and board[8] == 'x' or board[6] == 'o' and board[7] == 'o' and board[8] == 'o' or 
         board[0] == 'x' and board[3] == 'x' and board[6] == 'x' or board[0] == 'o' and board[3] == 'o' and board[6] == 'o' or 
         board[1] == 'x' and board[7] == 'x' and board[4] == 'x' or board[1] == 'o' and board[7] == 'o' and board[4] == 'o' or 
         board[2] == 'x' and board[5] == 'x' and board[8] == 'x' or board[2] == 'o' and board[5] == 'o' and board[8] == 'o' or 
         board[0] == 'x' and board[4] == 'x' and board[8] == 'x' or board[0] == 'o' and board[4] == 'o' and board[8] == 'o' or 
         board[2] == 'x' and board[4] == 'x' and board[6] == 'x' or board[2] == 'o' and board[4] == 'o' and board[6] == 'o' ):

        print("\nPlayer "+str(player)+" won the game well done!!") # If a player has won this message is displayed'
        status = 3 # and the status is changed.
        print("\nThe game will close in 5 sceonds")
        time.sleep(5)
        sys.exit

    else:
        status = 1 # If no other condition is met the game continues.
    return status #  returns the status value.

# The following function allows the user to play agianst a computer that guesses.
def random_computer():
     x = True
     while(x==True): # Starts a loop.
        computer_input = random.randint(1,9) # Makes a random number between 1 & 9.
        location = computer_input - 1 # Takes that number and takes one to give a location.
        if(board[location] == 'x' or board[location] == 'o'): # Checks if the random location is already taken by a piece.
            print("\nThe computer has tried to play in position " + str(location)) # This line makes clear where the computer has tried to play to the user. 
            continue # Continues onto a new loop iteration
        else:
            location = computer_input # Sets the location variable to the random number that the computer has picked if the space is free.
            print("\nThe computer has played in position " + str(location)) # This line makes clear where the computer has played to the user. 
            x = False # terminates the loop.
     return location # Returns the location variable. 

# The following function checks if the human player is about to win. 
def player_win_test(i): # The function is passed one argument. 
    b_copy = board.copy() # This makes a copy of the board as we dont want to change the boards state while checking if the player can win. 
    b_copy[i] = 'x' # This will put an 'x' in the location specified by the functions argument.
    # the code below will take the copy of the board and see if any possible wins are avalible.  
    if(b_copy[0] == 'x' and b_copy[1] == 'x' and b_copy[2] == 'x' or
    b_copy[3] == 'x' and b_copy[4] == 'x' and b_copy[5] == 'x' or  
    b_copy[6] == 'x' and b_copy[7] == 'x' and b_copy[8] == 'x' or  
    b_copy[0] == 'x' and b_copy[3] == 'x' and b_copy[6] == 'x' or  
    b_copy[1] == 'x' and b_copy[7] == 'x' and b_copy[4] == 'x' or   
    b_copy[2] == 'x' and b_copy[5] == 'x' and b_copy[8] == 'x' or  
    b_copy[0] == 'x' and b_copy[4] == 'x' and b_copy[8] == 'x' or  
    b_copy[2] == 'x' and b_copy[4] == 'x' and b_copy[6] == 'x' ):
        player_win = 1 # If the player can win the variable is set to one.
        return player_win # Then returns the value of player_wins.
    else:
        player_win = 0 # If the player cannot win it returns a zero. .
        return player_win # Then returns the value of player_wins.

 # The below function checks if the computer is able to win the game, it is very similar to the player_win_test() function apart from the symbol it is using. 
def computer_win_test(i): # The function is passed one argument.
    b_copy = board.copy() # Again this lines gets a copy of the board, to avoid editing the actual board.   
    b_copy[i] = 'o'  # This will put an 'o' in the location specified by the functions argument.
    # the code below will take the copy of the board and see if any possible wins are avalible.
    if(b_copy[0] == 'o' and b_copy[1] == 'o' and b_copy[2] == 'o' or
    b_copy[3] == 'o' and b_copy[4] == 'o' and b_copy[5] == 'o' or  
    b_copy[6] == 'o' and b_copy[7] == 'o' and b_copy[8] == 'o' or  
    b_copy[0] == 'o' and b_copy[3] == 'o' and b_copy[6] == 'o' or  
    b_copy[1] == 'o' and b_copy[7] == 'o' and b_copy[4] == 'o' or   
    b_copy[2] == 'o' and b_copy[5] == 'o' and b_copy[8] == 'o' or  
    b_copy[0] == 'o' and b_copy[4] == 'o' and b_copy[8] == 'o' or  
    b_copy[2] == 'o' and b_copy[4] == 'o' and b_copy[6] == 'o' ):
        computer_win = 1 # If the computer can win it returns a one. 
        return computer_win
    else:
        computer_win = 0 # If the computer cannot win it returns a zero. 
        return computer_win

# The function uses the two above it to make a decision on where the computer should play. 
def computer_move():
    for i in range (0,9): # Starts a loop that will run 9 times. 
        computer_wins = computer_win_test(i) # This will run the function to test if the computer can win, passing the loop itteration as the argument. 
        if (computer_wins == 1 and board[i] == ' '): # Checks if the computer can win, and if the space is free. 
            location = i + 1 # If it can win this will take the location add one to it so it plays in the right spot. 
            return location # And returns the variable.
# if the computer cannot win it will move on to the following. 
    for i in range (0,9): # Starts a loop that will run 9 times.
        player_wins = player_win_test(i)  # This will run the function to test if the player can win, passing the loop itteration as the argument.
        if (player_wins == 1 and board[i] == ' '):  # Checks if the player can win, and if the space is free.
            location = i + 1 # If it can win this will take the location add one to it so it plays in the right spot.
            return location # And returns the variable.
# If neither the computer or the player can win the following will run.    
    if(board[4] == ' '): # Checks if the centre location on the board is empty. 
        location = 5 # If it is the the computer plays there.  
        return location
# If the centre position is already taken the following occurres.    
    for i in [1,3,7,9]: # Starts a loop that checks the corners of the board. 
        b = board.copy() 
        if (b[i-1] == ' '): # Checks if the location is empty if it is,
            location = i # it returns the location and the computer plays there. 
            return location
# If none of the above locations are avaliable the following occurs. 
    for i in [2,4,6,8]: # Starts a loop that checks the top, bottom, left, and right middle locations of the board.
        b = board.copy()
        if (b[i-1] == ' '): # Checks if the location is epmty. 
            location = i # it returns the location and the computer plays there.
            return location

# Program main starts from here, feel free to edit it. 
board = [" "," "," "," "," "," "," "," "," "]
position = ['1','2','3','4','5','6','7','8','9']

print_board(position) # Prints out the board showing where the locations are. 
print("\nThese are the positions of the board,\nEnter the location to place your marker there.") # Gives the user some information about the game. 

turns = 1 # Sets the turns counter to 1.
status = status_check() # Runs the status check function to set the variable to 1.
while(status == 1): # Starts a loop.
    play_type = input("\nHow would you like to play? \n[1 = With a person, 2 = With a guessing computer, 3 = With a smart computer]:") # Gives the user the options to play against another person or the computer guessing.
    if any(char.isdigit() for char in play_type): # Checks if the user entered a valid play style.
        play_type = int(play_type) # Changes the users entered value into an integer. 

        if(play_type == 1): # If the user has chosen to play with a person this loop is started. 
            player = 1 # Sets the player number to 1.
            turns = 1 # Sets the turns counter to 1.
            status = status_check() # Runs the status check function to set the variable to 1. 
            while(status == 1): #  If the status is equal to one the loop starts.
                location = player_input() # Runs the player_input function and assigns the value at the end to loctaion. 
                if (player == 1): # Checks if the player number is 1.
                    draw_board(board,location,'x') # If the players number is 1 then the board is drawn with an x in the location they wanted. 
                    turns = turns + 1 # Increases the turn counter by one. 
                    status = status_check() # Runs the status check function to see if this player has won the game. 
                    player = 2 # Sets the player number to 2.
                else: 
                    # This does the same as above but for player 2, who uses o's.
                    draw_board(board,location,'o') 
                    turns = turns + 1
                    print_board(position) # Prints out the positions on the board to help with game smoothness. (stop people having to scroll to the top.)
                    status = status_check()
                    player = 1

        elif(play_type == 2): # If the users chooses to play a guessing computer the following is run. 
            player = 1
            turns = 1
            status = status_check()
            while(status == 1):
                if (player == 1):
                    location = player_input()
                    draw_board(board,location,'x')
                    turns = turns + 1
                    status = status_check()
                    player = 2
                else: 
                    location = random_computer() # this runs the random computer function and takes the random number as the variable.
                    draw_board(board,location,'o')
                    turns = turns + 1
                    print_board(position)
                    status = status_check()
                    player = 1                    
         
        elif(play_type == 3): # If the users chooses to play a smart computer the following is run.
             player = 1
             turns = 1
             status = status_check()
             while(status == 1):
                if (player == 1):
                    location = player_input()
                    draw_board(board,location,'x')
                    turns = turns + 1
                    status = status_check()
                    player = 2
                else: 
                    location = computer_move() # This runs the computer move function and sets the returned variable to location 
                    draw_board(board,location,'o')
                    print("\nThe computer has played in location "+ str(location)) # This line tells the user where the computer has played. 
                    turns = turns + 1
                    print_board(position)
                    status = status_check()
                    player = 1
                    
        else:
            print("\nNot valid please try again.") # If the user does not enter one of the play types this message is displayed.
    else:
        print("\nPlease do not enter a word, please try again.") # If the player enters a word instead of a number this message is displayed.