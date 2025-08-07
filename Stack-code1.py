##  第二部分：Python 中的棧實現
1. 使用列表實現棧
class Stack:
    def __init__(self):
        self.stack = []
 
    def push(self, data):
        """將數據壓入棧"""
        self.stack.append(data)
 
    def pop(self):
        """從棧頂彈出數據"""
        if not self.is_empty():
            return self.stack.pop()
        return "Stack is empty"
 
    def peek(self):
        """查看棧頂數據"""
        if not self.is_empty():
            return self.stack[-1]
        return "Stack is empty"
 
    def is_empty(self):
        """檢查棧是否為空"""
        return len(self.stack) == 0
 
    def size(self):
        """返回棧的大小"""
        return len(self.stack)
 
# 測試棧
if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print("棧頂元素:", stack.peek())  # 輸出: 棧頂元素: 30
    print("彈出元素:", stack.pop())  # 輸出: 彈出元素: 30
    print("棧是否為空:", stack.is_empty())  # 輸出: 棧是否為空: False
    print("棧的大小:", stack.size())  # 輸出: 棧的大小: 2


2. 使用 collections.deque 實現棧
from collections import deque
 
class Stack:
    def __init__(self):
        self.stack = deque()
 
    def push(self, data):
        self.stack.append(data)
 
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "Stack is empty"
 
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return "Stack is empty"
 
    def is_empty(self):
        return len(self.stack) == 0
 
    def size(self):
        return len(self.stack)
 
# 測試棧
if __name__ == "__main__":
    stack = Stack()
    stack.push(100)
    stack.push(200)
    print("棧頂元素:", stack.peek())  # 輸出: 棧頂元素: 200
    stack.pop()
    print("棧的大小:", stack.size())  # 輸出: 棧的大小: 1
