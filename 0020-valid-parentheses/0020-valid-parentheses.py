class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)
    

class Solution(object):
    def isValid(self, s):
        stack = Stack()
        matching_brackets = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in matching_brackets.values():
                stack.push(char)
            elif char in matching_brackets.keys():
                if stack.is_empty() or stack.pop() != matching_brackets[char]:
                    return False
        
        return stack.is_empty()