#스택
n = int(input())
order = []

for i in range(n):
    order.append(input().split())

stack = []

count = 0
top = 0
next = 0

def push(num):
    global top,next,count,stack
    if count == 0:
        stack.append(num)
    elif count > 0:
        stack.append(num)
        next = top
        top = num
        print(top)
        print(next)
    print(stack)
    count += 1

def pop():
    global top,next,count
    if count == 0:
        print(-1)
    else:
        print(top)
        top = next
        stack.remove(top)
        count -= 1

def size():
    global count
    print(count)

def empty():
    global count
    if count == 0:
        print(1)
    else:
        print(0)

def top():
    global top
    if empty() == 1:
        print(-1)
    else:
        print(top)

for j in range(n):
    order_text = order[i][0]
    if order_text == "push":
        push(order[i][1])
    elif order_text == "pop":
        pop()
    elif order_text == "size":
        size()
    elif order_text == "empty":
        empty()
    elif order_text == "top":
        top()
