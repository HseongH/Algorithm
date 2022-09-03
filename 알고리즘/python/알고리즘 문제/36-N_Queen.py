from sys import stdin

input = stdin.readline

def is_available(current_col, candidate):
    current_row = len(candidate)

    for queen_row in range(current_row):
        if current_col == candidate[queen_row] or abs(current_col - candidate[queen_row]) == current_row - queen_row:
            return False
    return True

def dfs(N, current_row, result, candidate):
    if current_row == N:
        result.append(candidate[:])
        return

    for current_col in range(N):
        if is_available(current_col, candidate):
            candidate.append(current_col)
            dfs(N, current_row + 1, result, candidate)
            candidate.pop()

def n_queen(N):
    result = list()
    dfs(N, 0, result, list())
    return result

n = int(input())
queen = n_queen(n)
print(queen)
