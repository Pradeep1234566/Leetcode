class Solution(object):
    def helper(self, candidates, target, index, n, result, temp):
        if target == 0:
            result.append(temp[:])
            return 
        
        if index == n:
            return 

        if candidates[index] <= target:
            temp.append(candidates[index])
            self.helper(candidates, target-candidates[index], index, n, result, temp)
            temp.pop()
        
        self.helper(candidates, target, index+1, n, result, temp)


    def combinationSum(self, candidates, target):
        result = []
        temp = []
        n = len(candidates)
        index = 0
        
        
        self.helper( candidates, target,  index, n, result, temp)

        return result
