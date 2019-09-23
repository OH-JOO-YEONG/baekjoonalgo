# 백준 문자열

# 포인트는 A가 B보다 길이가 작거나 같고 다른 부분은 추가가 된다는 부분이다.
# 이때, A의 첫 문자를 B의 어떤 지점부터 비교해서 시작할 때 가장 값이 작은지를 구하면 된다.

# 즉
# A가 "abc"이고
# B가 "abcdef" 일 때
# A[0]을 B[0]부터 비교하면 모두 같고 B[3]부터 B[5]는 def로 채우면 된다.
# A[0]을 B[1]부터 비교하면 모두 다르고 B[0]과 B[4],B[5]는 각각 a,e,f로 채우면 된다.

x, y = input().split()
min_cnt = 50
for i in range(len(y)-len(x) + 1):
    count = 0
    for j in range(len(x)):
        if x[j] != y[j + i]:
            count += 1
    min_cnt = min(count, min_cnt)
print(min_cnt)