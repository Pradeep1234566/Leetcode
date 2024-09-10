class MinStack(object):

    def __init__(self, data):
        self.top = None
        self.data = data
        self.next = None

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        newnode = Minstack(data):
        newnode.next = self.top
        self.top = newnode
        

    def pop(self):
        """
        :rtype: None
        """
        if self.top == None:
            return -1
        else:
            k = self.top.data
            self.top = self.top.next
            return k
        

    def top(self):
        """
        :rtype: int
        """
        

    def getMin(self):
        """
        :rtype: int
        """
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()