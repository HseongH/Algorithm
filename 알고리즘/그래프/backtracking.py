# 백 트래킹 (Backtracking)
# 제약 조건 만족 문제에서 해를 찾기 위한 전략
# 후보군의 제약 조건을 점진적으로 판단하다가 해당 후보군이 제약 조건을 만족할 수 없다고 판단되면 다시는 해당 후보군을 체크하지 않을 것을 표기하고 다른 후보군으로 넘어가 해를 찾는 방법

# N Queen 문제 - 대표적인 백 트래킹 문제

def is_available(current_col, candidate):
    current_row = len(candidate)

    for queen_row in range(current_row):
        if candidate[queen_row] == current_col or abs(candidate[queen_row] - current_col) == current_row - queen_row:
            return False
    return True

def dfs(N, current_row, candidate, result):
    if current_row == N:
        result.append(candidate[:])
        return
    
    for current_col in range(N):
        if is_available(current_col, candidate):
            candidate.append(current_col)
            dfs(N, current_row + 1, candidate, result)
            candidate.pop()

def n_queen(N):
    result = list()
    dfs(N, 0, list(), result)
    return result

print(n_queen(8))
