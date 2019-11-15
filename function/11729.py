# 백준 하노이 탑

num = int(input())
hanoilist = []
def hanoi(n, one, two, three, hanoilist):
    if n == 1:
        hanoilist.append([one, three])
        return

    hanoi(n - 1, one, three, two, hanoilist)
    hanoilist.append([one, three])
    hanoi(n - 1, two, one, three, hanoilist)

hanoi(num, 1, 2, 3, hanoilist)

print(len(hanoilist))
for a, b in hanoilist:
    print(a, b)