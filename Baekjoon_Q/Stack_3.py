#괄호
n = int(input())
word = []
result = []
total = 0
for i in range(n):
    w = input()
    word.append(w)
    for j in range(len(w)):
        if w[j] == "(":
            total += 1
        else:
            if total == 0:
                total -= 1
                break
            else:
                total -= 1
    if total == 0:
        result.append("Yes")
    else:
        result.append("No")
    total = 0

for i in range(n):
    print(result[i])