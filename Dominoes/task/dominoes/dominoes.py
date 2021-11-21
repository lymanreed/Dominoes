import random
random.seed()


def create_dominoes():
    dominoes = []
    for i in range(7):
        for j in range(i, 7):
            dominoes.append([i, j])
    random.shuffle(dominoes)
    return dominoes


def print_snake(snake):
    shown = ""
    if len(snake) < 7:
        for domino in snake:
            shown += str(domino)
    else:
        for i, domino in enumerate(snake):
            if i < 2:
                shown += str(domino)
            elif i == 2:
                shown += str(domino) + "..."
            elif i >= len(snake) - 3:
                shown += str(domino)
    print(shown)


def check_winner(computer, player, snake, stock):
    if len(computer) == 0:
        return "computer"
    if len(player) == 0:
        return "player"
    if snake[0][0] == snake[-1][1]:
        count = 0
        for d in snake:
            for e in d:
                if e == snake[0][0]:
                    count += 1
        if count == 8:
            return "draw"
    if len(stock) == 0:
        return "draw"
    return ""


def game_move(status, pieces, stock, snake):
    if status == "player":
        while True:
            try:
                move = int(input())
            except ValueError:
                print("Invalid input. Please try again.")
                continue
            if abs(move) > len(pieces):
                print("Invalid input. Please try again.")
                continue
            if move == 0:
                if len(stock):
                    random.shuffle(stock)
                    pieces.append(stock.pop())
                break
            else:
                side = "left" if move < 0 else "right"
                move = abs(move) - 1
                if not check_move(pieces[move], snake, side):
                    print("Illegal move. Please try again.")
                    continue
                piece = pieces[move]
                if side == "left":
                    if piece[1] != snake[0][0]:
                        piece.reverse()
                    snake.insert(0, piece)
                else:
                    if piece[0] != snake[-1][1]:
                        piece.reverse()
                    snake.append(piece)
                del pieces[move]
                break
        return [pieces, stock, snake]
    else:
        input()
        while True:
            move = get_computer_move(pieces, snake)
            if move == 0:
                if len(stock):
                    random.shuffle(stock)
                    pieces.append(stock.pop())
                break
            else:
                side = "left" if move < 0 else "right"
                move = abs(move) - 1
                piece = pieces[move]
                if side == "left":
                    if piece[1] != snake[0][0]:
                        piece.reverse()
                    snake.insert(0, piece)
                else:
                    if piece[0] != snake[-1][1]:
                        piece.reverse()
                    snake.append(piece)
                del pieces[move]
                break
        return [pieces, stock, snake]


def check_move(domino, snake, side):
    if side == "left":
        return True if snake[0][0] in domino else False
    else:
        return True if snake[-1][1] in domino else False


def get_computer_move(pieces, snake):
    # first find all legal dominoes
    legal_pieces = []
    for domino in pieces:
        if check_move(domino, snake, "left") or check_move(domino, snake, "right"):
            legal_pieces.append(domino)
    if not legal_pieces:
        return 0

    score_dict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    all_pieces = legal_pieces + snake
    for i in all_pieces:
        for j in i:
            score_dict[j] += 1

    scores = []
    for domino in legal_pieces:
        scores.append(score_dict[domino[0]] + score_dict[domino[1]])
    i = scores.index(max(scores))
    best_choice = legal_pieces[i]
    if best_choice[0] in snake[0] or best_choice[1] in snake:
        left = -1
    else:
        left = 1
    return (pieces.index(best_choice) + 1) * left


def main():
    doubles = [[6, 6], [5, 5], [4, 4], [3, 3], [2, 2], [1, 1], [0, 0]]

    while True:
        dominoes = create_dominoes()
        computer = dominoes[:7]
        player = dominoes[7:14]
        stock = dominoes[14:]
        snake = []
        status = ""

        for double in doubles:
            if double in player:
                player.remove(double)
                snake.append(double)
                status = "computer"
                break
            elif double in computer:
                computer.remove(double)
                snake.append(double)
                status = "player"
                break

        if status != "":
            break

    winner = ""
    while winner == "":
        print("=" * 70)
        print("Stock size:", len(stock))
        print("Computer pieces:", len(computer))
        print()
        print_snake(snake)
        print()
        print("Your pieces:")
        for i, piece in enumerate(player):
            print(f"{i + 1}:{piece}")
        print()
        winner = check_winner(computer, player, snake, stock)
        if winner:
            break
        print("Status: ", end="")
        if status == "player":
            print("It's your turn to make a move. Enter your command.")
            player, stock, snake = game_move(status, player, stock, snake)
            status = "computer"
        else:
            print("Computer is about to make a move. Press Enter to continue...")
            computer, stock, snake = game_move(status, computer, stock, snake)
            status = "player"

    print()
    print("Status: The game is over. ", end="")
    if winner == "player":
        print("You won!")
    elif winner == "computer":
        print("The computer won!")
    else:
        print("It's a draw!")


if __name__ == "__main__":
    main()
