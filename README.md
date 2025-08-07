# 南華大學資料結構-第一次期中報告
11124209蔡岱伶
# ex-8題目: Python 棧（Stack）
棧（Stack）是一種常見且重要的資料結構，因其簡單的操作邏輯和廣泛的應用場景，在電腦科學中扮演了不可替代的角色。本文將解析棧的基本原理、Python 中的實現方法，以及其實際應用場景。
# 目錄
第一部分：棧的基礎概念

第二部分：Python 中的棧實現
1. 使用列表實現棧
2. 使用 collections.deque 實現棧
   
第三部分：棧的實際應用
1. 運算式求值
2. 括弧匹配
3. 流覽器的前進後退功能

## 第一部分：棧的基礎概念
棧是一種 後進先出（LIFO, Last In First Out） 的資料結構。也就是說，最後壓入棧的資料會最先被取出。

### 棧的基本操作包括：

  Push：將數據壓入棧頂。
  
  Pop：從棧頂彈出數據。
  
  Peek/Top：查看棧頂數據，但不移除。
  
  IsEmpty：檢查棧是否為空。
  
### 棧的應用場景廣泛，例如：

  運算式求值與括弧匹配。
  
  深度優先搜索（DFS）。
  
  實現遞迴。
  
  流覽器前進後退功能。
## 第二部分：Python 中的棧實現
### 1. 使用列表實現棧
Python 的列表（list）天然支持棧的操作，可以通過 append 和 pop 方法實現。

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
 
#### 測試棧

      if __name__ == "__main__":
         stack = Stack()
         stack.push(10)
         stack.push(20)
         stack.push(30)
         print("棧頂元素:", stack.peek())  # 輸出: 棧頂元素: 30
         print("彈出元素:", stack.pop())  # 輸出: 彈出元素: 30
         print("棧是否為空:", stack.is_empty())  # 輸出: 棧是否為空: False
         print("棧的大小:", stack.size())  # 輸出: 棧的大小: 2

### 2. 使用 collections.deque 實現棧
Python 的 collections.deque 是一個雙端佇列，具有更高效的棧操作。

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
 
#### 測試棧

      if __name__ == "__main__":
         stack = Stack()
         stack.push(100)
         stack.push(200)
         print("棧頂元素:", stack.peek())  # 輸出: 棧頂元素: 200
         stack.pop()
         print("棧的大小:", stack.size())  # 輸出: 棧的大小: 1
         
## 第三部分：棧的實際應用
### 1. 運算式求值
棧可以用來將中綴運算式轉換為尾碼運算式，並進行求值。

    def evaluate_postfix(expression):
       stack = Stack()
       for char in expression:
         if char.isdigit():
            stack.push(int(char))
         else:
            b = stack.pop()
            a = stack.pop()
            if char == '+':
                stack.push(a + b)
            elif char == '-':
                stack.push(a - b)
            elif char == '*':
                stack.push(a * b)
            elif char == '/':
                stack.push(a / b)
       return stack.pop()
 
#### 測試尾碼運算式求值
      expr = "23*54*+9-"
      print("尾碼運算式求值結果:", evaluate_postfix(expr))  # 輸出: 17
### 2. 括弧匹配

    def is_valid_parentheses(expression):
      stack = Stack()
      matching = {')': '(', ']': '[', '}': '{'}
 
      for char in expression:
        if char in "([{":
            stack.push(char)
        elif char in ")]}":
           if stack.is_empty() or stack.pop() != matching[char]:
               return False
       return stack.is_empty()

#### 測試括弧匹配
      expr1 = "(a+b)*[c-d]"
      expr2 = "(a+b*[c-d)"
      print("運算式1括弧匹配:", is_valid_parentheses(expr1))  # 輸出: True
      print("運算式2括弧匹配:", is_valid_parentheses(expr2))  # 輸出: False
### 3. 流覽器的前進後退功能
流覽器中，前進和後退操作可以通過兩個棧實現。

    class Browser:
       def __init__(self):
         self.back_stack = Stack()
         self.forward_stack = Stack()
 
       def visit(self, url):
         if not self.back_stack.is_empty():
             self.forward_stack = Stack()  # 清空前進棧
         self.back_stack.push(url)
 
       def back(self):
         if self.back_stack.size() > 1:
             self.forward_stack.push(self.back_stack.pop())
             return self.back_stack.peek()
         return "No more pages to go back"
 
       def forward(self):
         if not self.forward_stack.is_empty():
             url = self.forward_stack.pop()
             self.back_stack.push(url)
             return url
         return "No more pages to go forward"

#### 測試流覽器
      browser = Browser()
      browser.visit("google.com")
      browser.visit("youtube.com")
      browser.visit("github.com")
      print("後退到:", browser.back())  # 輸出: youtube.com
      print("前進到:", browser.forward())  # 輸出: github.com

