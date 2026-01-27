def minimax(values, isMax):
    if len(values) == 1:
        return values[0]

    mid = len(values) // 2
    left = minimax(values[:mid], not isMax)
    right = minimax(values[mid:], not isMax)

    return max(left, right) if isMax else min(left, right)


values = list(map(int, input("Enter leaf values: ").split()))
print("Optimal value:", minimax(values, True))
