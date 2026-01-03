class Solution(object):
    def numOfWays(self, n):
        MOD = 10**9 + 7
        memo = [[-1,-1] for _ in range(n)]
        def dfs(row, prev_type):
            if row == n:
                return 1
            
            if memo[row][prev_type] != -1:
                return memo[row][prev_type]

            if prev_type == 0:  
                ways = (
                    2 * dfs(row + 1, 0) +
                    2 * dfs(row + 1, 1)
                ) % MOD
            else:  
                ways =  (
                    2 * dfs(row + 1, 0) +
                    3 * dfs(row + 1, 1)
                ) % MOD
            
            memo[row][prev_type] = ways
            return memo[row][prev_type]
        # First row choices
        abc = 6 * dfs(1, 0)
        aba = 6 * dfs(1, 1)

        return (abc + aba) % MOD
