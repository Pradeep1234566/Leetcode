class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        for i in tokens:
            if i=='+':
                k = int(stack.pop())
                l = int(stack.pop())
                k = k + l
                stack.append(k)
            elif i == '-':
                k = int(stack.pop())
                l = int(stack.pop())
                l = l - k
                stack.append(l)
            elif  i == '*':
                k = int(stack.pop())
                l = int(stack.pop())
                l = l * k
                stack.append(l)
            elif i == '/':
                k = int(stack.pop())
                l = int(stack.pop())
                l = int(float(l) / k)
                stack.append(l)          
            else:
                stack.append(int(i))
                #print(stack)
        return stack[0]