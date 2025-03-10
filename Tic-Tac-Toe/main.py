import random

#Display the board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
        
#Check for a win
def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

#check if the board is full
def is_full(board):
    return all(cell != " " for row in board for cell in row)

#Get available moves
def get_available_moves(board):
    
    return[(r, c) for r in range(3) for c in range (3) if board[r][c] == " "]

#Minimax Algorithm for AI
def minimax(board, depth, is_maximizing):
    if check_winner(board, "0"):
        return 10 - depth
    if check_winner(board, "X"):
        return depth - 10
    if is_full(board):
        return 0
    
    if is_maximizing:
        best_score = -float("inf")
        for r, c, in get_available_moves(board):
            board[r][c] = "0"
            score = minimax(board, depth + 1, False)
            board[r][c] = " "
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = float("inf")
        for r, c, in get_available_moves(board):
            board[r][c] = "X"
            score = minimax(board, depth + 1, True)
            board[r][c] = " "
            best_score = min(best_score, score)
        return best_score
    
#AI Move (Unbeatable)
def best_move(board):
    best_score = -float("inf")
    move = None
    for r, c in get_available_moves(board):
        board[r][c] = "0"
        score = minimax(board, 0, False)
        board[r][c] = " "
        if score > best_score:
            best_score = score
            move = (r, c)
    return move

#Main Game Loop
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Tic-Tac-Toe\n1. Player vs Player\n2. Player vs AI")
    mode = input("Choose mode (1/2)" )
    
    player_turn = True #X starts first
    
    while True:
        print_board(board)
        
        if mode == "2" and not player_turn: #AI Move
            r, c = best_move(board)
        else: #Player Move
            try:
                r, c = map(int, input("Enter row and column (1-3): ").split())
                r, c = r - 1, c - 1
                if board[r][c] != " ":
                    print("Invalid move. Try again.")
                    continue
            except:
                print("Invalid input. Try again.")
                continue
            
        board[r][c] = "X" if player_turn else "0"
        
        if check_winner(board, "X" if player_turn else "0"):
            print_board(board)
            print(f"{'Player' if player_turn else 'AI'} wins!")
            break
        if is_full(board):
            print_board(board)
            print("It's a tie!")
            break
        
        player_turn = not player_turn # switch turns
        
play_game()