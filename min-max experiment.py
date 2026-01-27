def minimax(node, isMax):
    
    # BASE CONDITION: leaf node (number)
    if type(node) == int:
        return node

    # MAX player
    if isMax:
        best = -1000
        for child in node:
            value = minimax(child, False)
            best = max(best, value)
        return best

    # MIN player
    else:
        best = 1000
        for child in node:
            value = minimax(child, True)
            best = min(best, value)
        return best


# -------- TREE (same as your diagram) --------
tree = [
            [       # B (MIN)
                [2, 3],    # D (MAX)
                [5, 9]     # E (MAX)
            ],
            [       # C (MIN)
                [0, 1],    # F (MAX)
                [7, 5]     # G (MAX)
            ]
        ]

# Root A is MAX
result = minimax(tree, True)

print("Optimal value at root (A):", result)

