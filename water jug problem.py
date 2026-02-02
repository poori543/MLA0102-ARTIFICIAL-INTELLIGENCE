from collections import deque

def water_jug_bfs(capacity1, capacity2, target):
    visited = set()
    queue = deque()

    # state: (jug1, jug2, path)
    queue.append((0, 0, []))

    while queue:
        jug1, jug2, path = queue.popleft()

        if (jug1, jug2) in visited:
            continue

        visited.add((jug1, jug2))
        path = path + [(jug1, jug2)]

        # Goal check
        if jug1 == target or jug2 == target:
            return path

        # All possible operations
        next_states = [
            (capacity1, jug2),        # Fill jug1
            (jug1, capacity2),        # Fill jug2
            (0, jug2),                # Empty jug1
            (jug1, 0),                # Empty jug2
            (jug1 - min(jug1, capacity2 - jug2),
             jug2 + min(jug1, capacity2 - jug2)),  # Pour jug1 -> jug2
            (jug1 + min(jug2, capacity1 - jug1),
             jug2 - min(jug2, capacity1 - jug1))   # Pour jug2 -> jug1
        ]

        for state in next_states:
            if state not in visited:
                queue.append((state[0], state[1], path))

    return None


# INPUT
jug1_capacity = 5
jug2_capacity = 3
target = 4

# CALL FUNCTION
solution = water_jug_bfs(jug1_capacity, jug2_capacity, target)

# OUTPUT
if solution:
    print("Steps to reach target:")
    for step in solution:
        print(step)
else:
    print("No solution found")
