def game_minimax(scores, turn):
    if len(scores) == 1:
        return scores[0]

    if turn == "MAX":
        return max(game_minimax(scores[:-1], "MIN"),
                   game_minimax(scores[1:], "MIN"))
    else:
        return min(game_minimax(scores[:-1], "MAX"),
                   game_minimax(scores[1:], "MAX"))


scores = [2, 3, 5, 9]
print("Best score:", game_minimax(scores, "MAX"))
