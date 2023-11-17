n, m = map(int, input().split())

board = [input().strip() for _ in range(n)]

def get_color(i, j):
    if board[i][j] == '.':
        return 'B' if (i + j) % 2 == 0 else 'W'
    else:
        return '-'

for i in range(n):
    row = [get_color(i, j) for j in range(m)]
    print("".join(row))