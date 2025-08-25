# Example: Ask user for a number and check if it's 10
#ser_input = input("Enter a number: ")

# Step 1: Try to convert input to integer
#ry:
  # number = int(user_input)   # if this fails, user gave a string or invalid input
    
    # Step 2: Check the value
    #f number == 10:
      # print("Correct! ✅")
    #lse:
        #rint("Wrong! ❌ Expected 10 but got", number)

#xcept ValueError:
    #rint("Invalid input. Please enter a number only.")   

    #loat ("3.14") 
    #rint("Float conversion successful:", 3.14) 

   #try:
     #  Guess_a_number = float(input("Guess a number between 1 and 10: "))
       #if Guess_a_number == 7.0:
       #    print("Correct! 🎉")
       #else:
     #      print("Wrong! ❌ Expected 7 but got", Guess_a_number)
   #except ValueError:
     #  print("Invalid input. Please enter a valid number.") 

      # some_value = "100"
      # some_value.isdigit  


board = ["-"] * 9
current_player = "X"
winner = None
gameRunning = True

def reset_game():
    global board, current_player, winner, gameRunning
    board = ["-"] * 9
    current_player = "X"
    winner = None
    gameRunning = True

def checkHorizontal(board):
    global winner
    for a, b, c in [(0,1,2), (3,4,5), (6,7,8)]:
        if board[a] == board[b] == board[c] != "-":
            winner = board[a]
            return True
    return False

def checkVertical(board):
    global winner
    for a, b, c in [(0,3,6), (1,4,7), (2,5,8)]:
        if board[a] == board[b] == board[c] != "-":
            winner = board[a]
            return True
    return False

def checkDiagonal(board):
    global winner
    for a, b, c in [(0,4,8), (2,4,6)]:
        if board[a] == board[b] == board[c] != "-":
            winner = board[a]
            return True
    return False

def checkWin(board):
    return checkHorizontal(board) or checkVertical(board) or checkDiagonal(board)

def checkTie(board):
    return "-" not in board

def switchPlayer():
    global current_player
    current_player = "O" if current_player == "X" else "X"

def make_move(pos):
    global gameRunning, board, current_player, winner
    if not gameRunning:
        return {"board": board, "winner": winner}

    if board[pos] == "-":
        board[pos] = current_player
        if checkWin(board):
            gameRunning = False
            return {"board": board, "winner": winner}
        elif checkTie(board):
            gameRunning = False
            return {"board": board, "winner": "Tie"}
        else:
            switchPlayer()
            return {"board": board, "winner": None}
    else:
        return {"board": board, "winner": None, "error": "Invalid move"}

