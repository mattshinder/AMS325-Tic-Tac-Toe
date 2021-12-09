import csv
import numpy as np
import matplotlib.pyplot as plt


# Function to print Tic Tac Toe
def print_tic_tac_toe(values):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[0], values[1], values[2]))
    print('\t_____|_____|_____')

    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[3], values[4], values[5]))
    print('\t_____|_____|_____')

    print("\t     |     |")

    print("\t  {}  |  {}  |  {}".format(values[6], values[7], values[8]))
    print("\t     |     |")
    print("\n")


# Function to print the score-board
def print_scoreboard(score_board):
    print("\t--------------------------------")
    print("\t              SCOREBOARD       ")
    print("\t--------------------------------")

    players = list(score_board.keys())
    print("\t   ", players[0], "\t    ", score_board[players[0]])
    print("\t   ", players[1], "\t    ", score_board[players[1]])

    print("\t--------------------------------\n")


# Function to check if any player has won
def check_win(player_pos, cur_player):
    # All possible winning combinations
    soln = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

    # Loop to check if any winning combination is satisfied
    for x in soln:
        if all(y in player_pos[cur_player] for y in x):
            # Return True if any winning combination satisfies
            return True
    # Return False if no combination is satisfied
    return False


# Function to check if the game is drawn
def check_draw(player_pos):
    if len(player_pos['X']) + len(player_pos['O']) == 9:
        return True
    return False


# Function for a single game of Tic Tac Toe
def single_game(cur_player):
    # Represents the Tic Tac Toe
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Stores the positions occupied by X and O
    player_pos = {'X': [], 'O': []}

    # Game Loop for a single game of Tic Tac Toe
    while True:
        print_tic_tac_toe(values)

        # Try exception block for MOVE input
        try:
            print("Player ", cur_player, " turn. Which box? : ", end="")
            move = int(input())
        except ValueError:
            print("Wrong Input!!! Try Again")
            continue

        # Sanity check for MOVE inout
        if move < 1 or move > 9:
            print("Wrong Input!!! Try Again")
            continue

        # Check if the box is not occupied already
        if values[move - 1] != move:
            print("Place already filled. Try again!!")
            continue

        # Update game information

        # Updating grid status
        values[move - 1] = cur_player

        # Updating player positions
        player_pos[cur_player].append(move)

        # Function call for checking win
        if check_win(player_pos, cur_player):
            print_tic_tac_toe(values)
            print("Player ", cur_player, " has won the game!!")
            print("\n")
            return cur_player

        # Function call for checking draw game
        if check_draw(player_pos):
            print_tic_tac_toe(values)
            print("Game Drawn")
            print("\n")
            return 'D'

        # Switch player moves
        if cur_player == 'X':
            cur_player = 'O'
        else:
            cur_player = 'X'


def winmove(cur_player, values):
    soln = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

    for x in soln:
        if values[x[0] - 1] == cur_player and values[x[1] - 1] == cur_player and values[x[2] - 1] != 'X' and \
                values[x[2] - 1] != 'O':
            return x[2]
        if values[x[1] - 1] == cur_player and values[x[2] - 1] == cur_player and values[x[0] - 1] != 'X' and \
                values[x[0] - 1] != 'O':
            return x[0]
        if values[x[0] - 1] == cur_player and values[x[2] - 1] == cur_player and values[x[1] - 1] != 'X' and \
                values[x[1] - 1] != 'O':
            return x[1]
    # nothing found, return 0
    return 0


def blockmove(cur_player, values):
    soln = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    opp_player = 'O'
    if cur_player == 'O':
        opp_player = 'X'

    for x in soln:
        if values[x[0] - 1] == opp_player and values[x[1] - 1] == opp_player and values[x[2] - 1] != 'X' and \
                values[x[2] - 1] != 'O':
            return x[2]
        if values[x[1] - 1] == opp_player and values[x[2] - 1] == opp_player and values[x[0] - 1] != 'X' and \
                values[x[0] - 1] != 'O':
            return x[0]
        if values[x[0] - 1] == opp_player and values[x[2] - 1] == opp_player and values[x[1] - 1] != 'X' and \
                values[x[1] - 1] != 'O':
            return x[1]
    # nothing found, return 0
    return 0


def evaluate(values, cur_player):
    # calculate win
    soln = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

    for x in soln:
        if values[x[0] - 1] == values[x[1] - 1] and values[x[1] - 1] == values[x[2] - 1]:
            if values[x[0] - 1] == cur_player:
                return 10
            else:
                return -10
    # nothing found, return 0
    return 0


def calcscore(values, depth, cur_player, turn):
    if cur_player == 'X':
        opp_player = 'O'
    else:
        opp_player = 'X'
    score = evaluate(values, cur_player)
    if score == 10:
        return score - depth
    if score == -10:
        return score + depth
    # count spaces
    count = 0
    for x in values:
        if x == 'O' or x == 'X':
            count = count + 1
    if count == 9:
        # tie
        return 0

    if turn:
        best = -1000
        for x in values:
            if x != 'X' and x != 'O':
                # save move
                save = x
                # make move
                values[int(x) - 1] = cur_player
                # calc score
                best = max(best, calcscore(values, depth + 1, opp_player, not turn))
                # undo move
                values[int(x) - 1] = save

        return best
    else:
        best = 1000
        for x in values:
            if x != 'X' and x != 'O':
                # save move
                save = x
                # make move
                values[int(x) - 1] = opp_player
                # calc score
                best = min(best, calcscore(values, depth + 1, cur_player, not turn))
                # undo move
                values[int(x) - 1] = save
        return best


def findbestmove(values, cur_player):
    # values is board, cur_player is either X or O

    bestval = -1000
    bestmove = 0
    # loop through values looking for empty space
    for x in values:
        if x != 'X' and x != 'O':
            # save move
            save = x
            # make move
            values[int(x) - 1] = cur_player
            # calc score
            tempval = calcscore(values, 0, cur_player, False)
            # undo move
            values[int(x) - 1] = save
            # if score > bestval, then update bestval and bestmove
            if tempval == bestval:
                if int(x) == 1 or int(x) == 3 or int(x) == 7 or int(x) == 9:
                    bestmove = int(x)
            elif tempval > bestval:
                bestval = tempval
                bestmove = int(x)
    return bestmove


# Function for a single game of Tic Tac Toe
def cpu_game(cur_user, cur_player, mode, player):
    # Represents the Tic Tac Toe
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Stores the positions occupied by X and O
    player_pos = {'X': [], 'O': []}

    # Game Loop for a single game of Tic Tac Toe
    while True:
        print_tic_tac_toe(values)

        # Try exception block for MOVE input
        try:
            if cur_user == 'CPU':
                # CPU turn
                # decipher mode
                if mode == 'easy':
                    # pick randomly
                    move = np.random.randint(1, 9)
                if mode == 'medium':
                    # Search for win, then block, then random pick
                    # search for win
                    move = winmove(cur_player, values)
                    if move == 0:
                        # block move
                        move = blockmove(cur_player, values)
                        if move == 0:
                            # random move
                            if move == 0:
                                move = np.random.randint(1, 9)
                if mode == 'hard':
                    # Search for win, then block, then choose best pick
                    # search for win
                    move = winmove(cur_player, values)
                    if move == 0:
                        # block move
                        move = blockmove(cur_player, values)
                        if move == 0:
                            # best pick
                            if move == 0:
                                # count values open
                                count = 0
                                for x in values:
                                    if x == 'O' or x == 'X':
                                        count = count + 1
                                # 0 values
                                if count == 0:
                                    move = 1
                                elif count == 1:
                                    if values[8] != 9:
                                        move = 1
                                    else:
                                        move = findbestmove(values, cur_player)
                                else:
                                    move = findbestmove(values, cur_player)

            else:
                print("Player ", cur_player, " turn. Which box? : ", end="")
                move = int(input())
        except ValueError:
            print("Wrong Input!!! Try Again")
            continue

        # Sanity check for MOVE inout
        if move < 1 or move > 9:
            print("Wrong Input!!! Try Again")
            continue

        # Check if the box is not occupied already
        if values[move - 1] != move:
            print("Place already filled. Try again!!")
            continue

        # Update game information

        # Updating grid status
        values[move - 1] = cur_player

        # Updating player positions
        player_pos[cur_player].append(move)

        # Function call for checking win
        if check_win(player_pos, cur_player):
            print_tic_tac_toe(values)
            print("Player ", cur_player, " has won the game!!")
            print("\n")
            return cur_player

        # Function call for checking draw game
        if check_draw(player_pos):
            print_tic_tac_toe(values)
            print("Game Drawn")
            print("\n")
            return 'D'

        # Switch player moves
        if cur_user == 'CPU':
            cur_user = player
        else:
            cur_user = 'CPU'
        if cur_player == 'X':
            cur_player = 'O'
        else:
            cur_player = 'X'


def oneplayer(mode):
    player = input("Enter player name: ")
    cpu = 'CPU'
    cur_player = player

    # Stores the choice of players
    player_choice = {'X': "", 'O': ""}
    # Stores the options
    options = ['X', 'O']

    while True:

        # Player choice Menu
        print("Turn to choose for", cur_player)
        print("Enter 1 for X")
        print("Enter 2 for O")
        print("Enter 3 to Quit")

        # Try exception for CHOICE input
        try:
            choice = int(input())
        except ValueError:
            print("Wrong Input!!! Try Again\n")
            continue

        # Conditions for player choice
        if choice == 1:
            player_choice['X'] = cur_player
            if cur_player == player:
                player_choice['O'] = cpu
            else:
                player_choice['O'] = player

        elif choice == 2:
            player_choice['O'] = cur_player
            if cur_player == player:
                player_choice['X'] = cpu
            else:
                player_choice['X'] = player

        elif choice == 3:
            break

        else:
            print("Wrong Choice!!!! Try Again\n")

        # Stores the winner in a single game of Tic Tac Toe
        winner = cpu_game(cur_player, options[choice - 1], mode, player)

        # Edits the scoreboard according to the winner
        if winner != 'D':
            player_won = player_choice[winner]
            # get loser
            playerwin = False
            if player_won == player:
                playerwin = True
            # update scores
            playwin = False
            playlose = False
            for x in dict:
                if x[0] == player and playerwin == True:
                    x[1] = int(x[1]) + 1
                    playwin = True
                if x[0] == player and playerwin == False:
                    x[2] = int(x[2]) + 1
                    playlose = True
            if not playwin and playerwin:
                dict.append([player, 1, 0, 0])
            if not playlose and not playerwin:
                dict.append([player, 0, 1, 0])
        if winner == 'D':
            # update scores
            play1 = False
            for x in dict:
                if x[0] == player:
                    x[3] = int(x[3]) + 1
                    play1 = True
            if not play1:
                dict.append([player, 0, 0, 1])
        # writing to csv file
        with open('scores.csv', 'w+') as csvfile:
            # creating a csv writer object
            csvwriter = csv.writer(csvfile, lineterminator="\n")

            # write data to file
            csvwriter.writerows(dict)

        # Switch player who chooses X or O
        if cur_player == player:
            cur_player = cpu
        else:
            cur_player = player


def twoplayer():
    print("Player 1")
    player1 = input("Enter the name: ")
    print("\n")

    print("Player 2")
    player2 = input("Enter the name: ")
    print("\n")

    # Stores the player who chooses X and O
    cur_player = player1

    # Stores the choice of players
    player_choice = {'X': "", 'O': ""}

    # Stores the options
    options = ['X', 'O']

    # Stores the scoreboard
    score_board = {player1: 0, player2: 0}
    print_scoreboard(score_board)

    # Game Loop for a series of Tic Tac Toe
    # The loop runs until the players quit
    while True:

        # Player choice Menu
        print("Turn to choose for", cur_player)
        print("Enter 1 for X")
        print("Enter 2 for O")
        print("Enter 3 to Quit")

        # Try exception for CHOICE input
        try:
            choice = int(input())
        except ValueError:
            print("Wrong Input!!! Try Again\n")
            continue

        # Conditions for player choice
        if choice == 1:
            player_choice['X'] = cur_player
            if cur_player == player1:
                player_choice['O'] = player2
            else:
                player_choice['O'] = player1

        elif choice == 2:
            player_choice['O'] = cur_player
            if cur_player == player1:
                player_choice['X'] = player2
            else:
                player_choice['X'] = player1

        elif choice == 3:
            print("Final Scores")
            print_scoreboard(score_board)
            break

        else:
            print("Wrong Choice!!!! Try Again\n")

        # Stores the winner in a single game of Tic Tac Toe
        winner = single_game(options[choice - 1])

        # Edits the scoreboard according to the winner
        if winner != 'D':
            player_won = player_choice[winner]
            score_board[player_won] = score_board[player_won] + 1
            # get loser
            player_lose = player1
            if player_won == player1:
                player_lose = player2
            # update scores
            playerwin = False
            playerlose = False
            for x in dict:
                if x[0] == player_won:
                    x[1] = int(x[1]) + 1
                    playerwin = True
                if x[0] == player_lose:
                    x[2] = int(x[2]) + 1
                    playerwin = True
            if not playerwin:
                dict.append([player_won, 1, 0, 0])
            if not playerlose:
                dict.append([player_lose, 0, 1, 0])
        if winner == 'D':
            # update scores
            play1 = False
            play2 = False
            for x in dict:
                if x[0] == player1:
                    x[3] = int(x[3]) + 1
                    play1 = True
                if x[0] == player2:
                    x[3] = int(x[3]) + 1
                    play2 = True
            if not play1:
                dict.append([player1, 0, 0, 1])
            if not play2:
                dict.append([player2, 0, 0, 1])
        # writing to csv file
        with open('scores.csv', 'w+') as csvfile:
            # creating a csv writer object
            csvwriter = csv.writer(csvfile, lineterminator="\n")

            # write data to file
            csvwriter.writerows(dict)

        # scoreboard
        print_scoreboard(score_board)
        # Switch player who chooses X or O
        if cur_player == player1:
            cur_player = player2
        else:
            cur_player = player1


def showscores():
    score = False
    data = []
    user = ''
    while not score:
        user = input("Enter name: ")
        print("\n")
        # look for name
        for x in dict:
            if x[0] == user:
                score = True
                data.append(x[1])
                data.append(x[2])
                data.append(x[3])
        if not score:
            print('Name not found, try again.\n')

    labels = 'Wins', 'Losses', 'Ties'

    fig1, ax1 = plt.subplots()
    ax1.pie(data, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title('Scores for ' + user)
    plt.show()


if __name__ == "__main__":

    # import csv
    f = open('scores.csv')
    csv_f = csv.reader(f)

    dict = []
    for row in csv_f:
        dict.append(row)

    # Ask for choice of game mode
    print("Pick a Game Mode")
    print("Enter 1 for Easy CPU")
    print("Enter 2 for Medium CPU")
    print("Enter 3 for Hard CPU")
    print("Enter 4 for 2 Player")
    print("Enter 5 for Scores")
    gamemode = int(input("Choice: "))
    print("\n")

    if gamemode == 1:
        oneplayer('easy')
    if gamemode == 2:
        oneplayer('medium')
    if gamemode == 3:
        oneplayer('hard')
    if gamemode == 4:
        twoplayer()
    if gamemode == 5:
        showscores()
