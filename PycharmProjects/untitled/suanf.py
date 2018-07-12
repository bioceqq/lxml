dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

arr = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
x_len = len(arr)
y_len = len(arr[0])
islands_len = 0

def count(x, y, arr):
    if (-1 < x < x_len) and (-1 < y < y_len):
        return 1 if (arr[x][y] == 0) else 0
    return 1

if __name__ == "__main__":
    for x in range(x_len):
        for y in range(y_len):
            if arr[x][y] == 1:
                for index in range(4):
                    islands_len += count(x + dx[index], y + dy[index], arr)
    print(islands_len)