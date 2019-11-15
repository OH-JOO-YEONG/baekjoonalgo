# 백준 별찍기 10

def Star(x, y, num, matrix):
    if num == 1:
        matrix[x][y] = '*'
        return

    div = num // 3
    for i in range (3):
        for j in range (3):
            if i == 1 and j == 1:
                pass
            else:
                Star(x + (i * div), y + (j * div), div, matrix)
        #         print(i * div, end=' ')
        #         print(j * div, end=' ')
        #         print(div)
        # print('----')

mat = [[' '] * 2201 for i in range(2201)]
n = int(input())

Star(0, 0, n, mat)

for i in range(n):
    for j in range(n):
        print(mat[i][j], end='')
    print()