#균형잡힌 세상
n = int(input())
result = []
S_total = 0
B_total = 0
for i in range(n):
    w = input()
    for j in range(len(w)):
        if w[j] == "(":
            S_total += 1
        elif w[j] == "[":
            B_total += 1
        elif w[j] == ")":
            if S_total == 0:
                result.append("No")
                break
            else:
                S_total -= 1
        elif w[j] == "]":
            if B_total == 0:
                result.append("No")
                break
            else:
                B_total -= 1
    if S_total == 0 and B_total == 0:
        result.append("Yes")
    elif S_total > 0 or B_total > 0:
        result.append("No")
    total = 0

for i in range(n):
    print(result[i])