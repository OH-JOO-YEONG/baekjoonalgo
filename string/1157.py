# 백준 단어공부
import collections

string1 = input()

def strstudy(s):
    s = s.upper()
    string = []
    max_dict = []
    for i in s:
        string += i
    string_dict = collections.Counter(string)
    for key, value in string_dict.items():
        if value == max(string_dict.values()):
            max_dict.append(key)
    if len(max_dict) >= 2:
        return "?"
    else:
        return max_dict[0]
a = strstudy(string1)

print(a)