from collections import OrderedDict

word = OrderedDict()

for _ in range(int(input())):
    key = input()
    word[key] = word.get(key, 0) + 1

print(len(word))

for key,value in word.items():
    print(value,end = " ")
