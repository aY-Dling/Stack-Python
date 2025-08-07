# 南華大學資料結構-第一次作業報告
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


  
