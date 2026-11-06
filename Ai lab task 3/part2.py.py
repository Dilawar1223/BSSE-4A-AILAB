graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["G"],
    "F": [],
    "G": []
}


def dls(current, goal, depth, path):

    if current == goal:
        return "FOUND", path

    if depth == 0:
        return "CUTOFF", None

    had_cutoff = False

    for next_node in graph[current]:

        if next_node in path:
            continue

        status, new_path = dls(
            next_node,
            goal,
            depth - 1,
            path + [next_node]
        )

        if status == "FOUND":
            return status, new_path

        if status == "CUTOFF":
            had_cutoff = True

    if had_cutoff:
        return "CUTOFF", None

    return "FAILURE", None


# DLS test

print("DLS Results")

for depth in [1, 2, 3, 4]:

    status, path = dls("A", "G", depth, ["A"])

    print("Limit:", depth)
    print("Status:", status)
    print("Path:", path)
    print()


# IDDFS test

print("IDDFS Results")

for depth in [1, 2, 3, 4]:

    status, path = dls("A", "G", depth, ["A"])

    print("Limit:", depth)
    print("Status:", status)
    print("Path:", path)
    print()

    if status == "FOUND":
        break
