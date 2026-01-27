def alphabeta(node, alpha, beta, isMax):
    if type(node) == int:
        return node

    if isMax:
        for child in node:
            alpha = max(alpha, alphabeta(child, alpha, beta, False))
            if beta <= alpha:
                break
        return alpha
    else:
        for child in node:
            beta = min(beta, alphabeta(child, alpha, beta, True))
            if beta <= alpha:
                break
        return beta


tree = [
        [[2, 3], [5, 9]],
        [[0, 1], [7, 5]]
       ]

print("Optimal value:", alphabeta(tree, -1000, 1000, True))
