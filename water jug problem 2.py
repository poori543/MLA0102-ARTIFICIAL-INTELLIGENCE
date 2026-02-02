from collections import deque

def water_jug_3_bfs(cap):
    # capacities
    c1, c2, c3 = cap

    # initial state: (jug3L, jug5L, jug8L)
    start = (0, 0, c3)

    # goal: 4L in 5L jug and 4L in 8L jug
    def is_goal(state):
        return state[1] == 4 and state[2] == 4

    visited = set()
    queue = deque()
    queue.append((start, [start]))

    while queue:
        (a, b, c), path = queue.popleft()

        if (a, b, c) in visited:
            continue
        visited.add((a, b, c))

        if is_goal((a, b, c)):
            return path

        states = []

        # Pour operations
        def pour(x, y, cap_y):
            t = min(x, cap_y - y)
            return x - t, y + t

        # 3L -> 5L
        na, nb = pour(a, b, c2)
        states.append((na, nb, c))

        # 3L -> 8L
        na, nc = pour(a, c, c3)
        states.append((na, b, nc))

        # 5L -> 3L
        nb, na = pour(b, a, c1)
        states.append((na, nb, c))

        # 5L -> 8L
        nb, nc = pour(b, c, c3)
        states.append((a, nb, nc))

        # 8L -> 3L
        nc, na = pour(c, a, c1)
        states.append((na, b, nc))

        # 8L -> 5L
        nc, nb = pour(c, b, c2)
        states.append((a, nb, nc))

        for s in states:
            if s not in visited:
                queue.append((s, path + [s]))

    return None


# capacities of jugs
capacities = (3, 5, 8)

solution = water_jug_3_bfs(capacities)

# OUTPUT
if solution:
    print("Steps (3L, 5L, 8L):")
    for step in solution:
        print(step)
else:
    print("No solution found")
