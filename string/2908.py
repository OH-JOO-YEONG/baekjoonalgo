# 백준 상수

a, b = input().split()

def reverse_compare(a, b):
    a = a[::-1]
    b = b[::-1]

    comp = max(int(a), int(b))

    return comp
c = reverse_compare(a, b)
print(c)