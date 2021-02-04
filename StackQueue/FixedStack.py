class FixedStack:
    '''고정 길이 스택 클래스'''
    class Empty(Exception): #예외 처리 클래스
        pass #비어 있는 FixedStack에 팝 또는 피크할때 내보내는 예외 처리

    class Full(Exception):
        pass

    def __init__(self,capacity : int = 256):
        self.capacity = capacity #스택의 크기
        self.stk = []*capacity #스택 본체
        self.ptr = 0 #스택 포인터 -> 스택에 쌓여 있는 데이터의 개수

    def __len__(self):
        return self.ptr

    def is_Empty(self):
        return self.ptr <= 0

    def is_Full(self):
        return self.ptr >= self.capacity

    def push(self, value):
        if self.is_Full(): #스택이 가득 차 있는 경우
            raise FixedStack.Full #예외 처리 발생
        self.stk[self.ptr] = value
        self.ptr += 1

    def pop(self):
        if self.is_Empty():
            raise FixedStack.Empty
        self.ptr -= 1 #ptr값을 하나 줄이고
        return self.stk[self.ptr]

    def peek(self):
        if self.is_Empty():
            raise FixedStack.Empty
        return self.stk[self.ptr-1]

    def clear(self):
        self.ptr = 0

    def find(self,value):
        for i in self.stk:
            if(i == value):
                return i
        return -1

    def count(self, value):
        c = 0
        for i in range(self.ptr):
            if self.stk[i] == value:
                c += 1
        return c

    def __contains__(self, item):
        return self.count(item)

    def dump(self):
        if self.is_Empty():
            print("스택이 비었음")
        else:
            print(self.stk[:self.ptr])