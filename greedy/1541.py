# 백준 잃어버린 괄호

int_list = list(map(int, input().replace("+", ",+").replace("-", ",-").split(","))) # replace 메서드를 가지고 정수형으로 바꾸기
result, check = 0, False

for sol in int_list:
    if check:
        result -= abs(sol)
    else:
        if sol >= 0:
            result += sol
        else:
            result += sol
            check = True
print(result)

# 현재 19-09-24 때 처음 이걸 접한 나로써는 리플레이스 메서드를 활용하는 걸 생각 못해서 구글링으로 뒤져보고 어떤 분의 코드를 참고했다.