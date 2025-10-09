class Solution(object):
    def helper(self, index, N, candidates, temp, result, target):
        if target == 0:
            result.append(list(temp))
            return
        
        for i in range(index, N):
            # ✅ Skip duplicates at the same recursion depth
            if i > index and candidates[i] == candidates[i - 1]:
                continue
            
            # Stop early since array is sorted
            if candidates[i] > target:
                break

            temp.append(candidates[i])
            self.helper(i + 1, N, candidates, temp, result, target - candidates[i])
            temp.pop()

    def combinationSum2(self, candidates, target):
        candidates.sort()  # ✅ Sort to handle duplicates easily
        result = []
        self.helper(0, len(candidates), candidates, [], result, target)
        return result
