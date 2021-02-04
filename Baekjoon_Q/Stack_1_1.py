#Stack
class Node:
    def __init__(self,num):
        self.num = num
        self.next = None

    def set_next(self,num2):
        self.next = num2

    def get_num(self):
        print(int(self.num))

class Stack:
    def __init__(self):
        self.header = None
        self.top = None
        self.size = 0

    def push(self,num):
        node = Node(num)
        if(self.header == None):
            self.header = node
            self.top = node
            self.size += 1
        else:
            node.set_next(self.top)
            self.top = node
            self.size += 1

    def pop(self):
        if self.size == 0:
            print(-1)
        else:
            print(self.top.get_num())
            self.top = (self.top).next
            self.size -= 1


n = int(input())
order = []

for i in range(n):
    order.append(input().split())

stack = Stack()
for j in range(n):
    order_text = order[j][0]

    if order_text == "push":
        stack.push(int(order[j][1]))
    elif order_text == "pop":
        stack.pop()
    elif order_text == "size":
        print(stack.size)
    elif order_text == "empty":
        if stack.size == 0:
            print(1)
        else:
            print(0)
    elif order_text == "top":
        if stack.size == 0:
            print(-1)
        else:
            print(stack.top.get_num())