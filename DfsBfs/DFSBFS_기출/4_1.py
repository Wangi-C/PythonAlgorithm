#괄호 변환 #2
def balance(p):
    count = 0
    for i in range(len(p)):
        if p[i] == "(":
            count += 1
        else:
            count -= 1
        if count == 0:
            return i

def check(p):
    count = 0
    for i in p:
        if i == "(":
            count += 1
        else:
            if count == 0:
                return False
            count -= 1
    return True

def change(p):
    answer = ""
    if p == "":
        return answer
    index = balance(p)
    u = p[:index+1]
    v = p[index+1:]
    if check(u):
        answer =  u + change(v)
    else:
        answer = "("
        answer += change(v)
        answer += ")"
        u = list(u[1:-1]) #??
        for i in range(len(u)):
            if u[i] == "(":
                u[i] = ")"
            else:
                u[i] = "("
        answer += "".join(u)
    return answer

p = input()
print(change(p))