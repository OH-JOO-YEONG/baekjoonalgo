# 백준 크로아티아 알파벳

string = input()

croa = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']


for word in croa:
    string = string.replace(word, "0")
print(len(string))