# 백준 한수

n = int(input())

count = 0
def han(n):
    hansu = []
    while True:
        if n <= 0:
            break
        hansu.append(n % 10)
        n = n // 10
    if (hansu[0] - hansu[1]) == (hansu[1] - hansu[2]):
        return True


for i in range(1, n + 1):
    if i < 100:
        count += 1
    elif i == 1000:
        break
    else:
        if han(i):
            count += 1
print(count)

