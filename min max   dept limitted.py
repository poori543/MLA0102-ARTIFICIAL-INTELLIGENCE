def minimax(node, depth, isMax):
    if depth == 0 or type(node) == int:
        return node if type(node) == int else 0

    if isMax:
        return max(minimax(child, depth-1, False) for child in node)
    else:
        return min(minimax(child, depth-1, True) for child in node)


tree = [
        [[2, 3], [5, 9]],
        [[0, 1], [7, 5]]
       ]

print("Optimal value:", minimax(tree, 3, True))
