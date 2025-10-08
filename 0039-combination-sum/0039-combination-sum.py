class Solution(object):
    def helper(self, index, N, candidates, temp, result, target):
        # Base condition
        if target == 0:
            result.append(list(temp))
            return
        if index == N:
            return
        
        # Include current element if it's <= target
        if candidates[index] <= target:
            temp.append(candidates[index])
            self.helper(index, N, candidates, temp, result, target - candidates[index])
            temp.pop()
        
        # Exclude current element
        self.helper(index + 1, N, candidates, temp, result, target)

    def combinationSum(self, candidates, target):
        result = []
        self.helper(0, len(candidates), candidates, [], result, target)
        return result
