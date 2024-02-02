import math


def print_board(board):
    a = 3
    for row in board:
        print("  |  ".join(row))
        a = a - 1
        if a > 0:
            print("-" * 15)
    print()


def check_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def is_draw(board):
    return all(board[i][j] != "." for i in range(3) for j in range(3))


def minimax(board, depth, is_maximizing, alpha, beta, player, max_depth):
    next_player = 'O' if player == 'X' else 'X'
    if check_winner(board, next_player):
        return -1
    if check_winner(board, player):
        return 1
    if is_draw(board):
        return 0
    if depth == max_depth:
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ".":
                    board[i][j] = player
                    score = minimax(board, depth + 1, False, alpha, beta, player, max_depth)
                    board[i][j] = "."
                    best_score = max(best_score, score)
                    # Beta Pruning
                    if best_score >= beta:
                        break
                    alpha = max(alpha, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ".":
                    board[i][j] = next_player
                    score = minimax(board, depth + 1, True, alpha, beta, player, max_depth)
                    board[i][j] = "."
                    best_score = min(best_score, score)
                    # Alpha Pruning
                    if best_score <= alpha:
                        break
                    beta = min(beta, best_score)
        return best_score


def best_move(board, player, max_depth):
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ".":

                board[i][j] = player
                alpha = -math.inf
                beta = math.inf
                score = minimax(board, 0, False, alpha, beta, player, max_depth)

                board[i][j] = "."
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move


def choose_difficulty():
    while True:
        print("Select difficulty level:")
        print("1. Easy")
        print("2. Hard")
        choice = input("Enter your choice (1 or 2): ")
        if choice == "1":
            return 3  # Set depth for easy
        elif choice == "2":
            return 9  # Set depth for hard
        else:
            print("Invalid choice. Please select 1 or 2.")


def AlgorithmVsAlgorithm():
    board = [["."] * 3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)
        move = best_move(board, player, 9)
        if move:
            board[move[0]][move[1]] = player
        else:
            print("The game ended in a draw!")
            break

        if check_winner(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            break
        elif is_draw(board):
            print_board(board)
            print("The game ended in a draw!")
            break

        player = "O" if player == "X" else "X"


def AlgorithmVsPlayer():
    difficulty = choose_difficulty()
    board = [["."] * 3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        if player == "X":
            row, col = map(int, input(f"Player {player}, enter your move (row column): ").split())
            if board[row][col] == ".":
                board[row][col] = player
            else:
                print("Invalid move. Try again.")
                continue
        else:
            move = best_move(board, "O", difficulty)
            if move:
                board[move[0]][move[1]] = player
            else:
                print("The game ended in a draw!")
                break

        if check_winner(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            break
        elif is_draw(board):
            print_board(board)
            print("The game ended in a draw!")
            break

        player = "O" if player == "X" else "X"


def tic_tac_toe():
    print(" Tic Tac Toe Game ")
    print("1. Player Vs Algorithm")
    print("2. Algorithm Vs Algorithm")
    choice = input("Enter your choice (1 or 2): ")
    if choice == "1":
        AlgorithmVsPlayer()
    elif choice == "2":
        AlgorithmVsAlgorithm()
    else:
        print("Invalid choice. Please select 1 or 2.")


tic_tac_toe()
