tree = [
    [[4, 6], [2, 5]],
    [[1, 3], [7, 8]]
]
count = 0
def minimax(node, max_turn):
    global count
    if isinstance(node, int):
        count += 1
        return node
    if max_turn:
        best = -999

        for child in node:
            value = minimax(child, False)
            best = max(best, value)
        return best
    else:
        best = 999
        for child in node:
            value = minimax(child, True)
            best = min(best, value)
        return best
count = 0
answer = minimax(tree, True)
print("Minimax Answer:", answer)
print("Leaves Checked:", count)
def alpha_beta(node, max_turn, alpha, beta):
    global count
    if isinstance(node, int):
        count += 1
        return node

    if max_turn:
        best = -999

        for child in node:
            value = alpha_beta(child, False, alpha, beta)
            best = max(best, value)
            alpha = max(alpha, best)

            if alpha >= beta:
                break

        return best

    else:
        best = 999

        for child in node:
            value = alpha_beta(child, True, alpha, beta)
            best = min(best, value)
            beta = min(beta, best)

            if alpha >= beta:
                break

        return best


count = 0
answer = alpha_beta(tree, True, -999, 999)
print("\nAlpha-Beta :", answer)
print("Leaves Checked:", count)
