def minimax(node, isMax, name):
    if type(node) == int:
        return node

    values = []
    for child in node:
        values.append(minimax(child, not isMax, name))

    result = max(values) if isMax else min(values)
    return result


tree = [
        [[2, 3], [5, 9]],
        [[0, 1], [7, 5]]
       ]

print("Value at A:", minimax(tree, True, 'A'))
