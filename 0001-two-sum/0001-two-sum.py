class Solution(object):
    def twoSum(self, nums, target):
        self.x = nums
        self.y = target
        n = len(self.x)
        a = []
        key = 0
        
        for i in range(n):
            for j in range(i+1,n):
                if(self.x[i] + self.x[j] == self.y):
                    a.append(i)
                    a.append(j)
                    key = 1
                    break
            
        if key == 1:
            return a
        else:
            return 0
                
                
                
                
                    
                    