## 第三部分：棧的實際應用
1. 運算式求值
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
 
# 測試尾碼運算式求值
expr = "23*54*+9-"
print("尾碼運算式求值結果:", evaluate_postfix(expr))  # 輸出: 17


2. 括弧匹配
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
 
# 測試括弧匹配
expr1 = "(a+b)*[c-d]"
expr2 = "(a+b*[c-d)"
print("運算式1括弧匹配:", is_valid_parentheses(expr1))  # 輸出: True
print("運算式2括弧匹配:", is_valid_parentheses(expr2))  # 輸出: False


3. 流覽器的前進後退功能
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
 
# 測試流覽器
browser = Browser()
browser.visit("google.com")
browser.visit("youtube.com")
browser.visit("github.com")
print("後退到:", browser.back())  # 輸出: youtube.com
print("前進到:", browser.forward())  # 輸出: github.com

