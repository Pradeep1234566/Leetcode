class Solution:
    def maxProduct(self, root):
        MOD = 10**9 + 7
        self.max_product = 0

        # First DFS to get total sum
        def totalSum(node):
            if not node:
                return 0
            return node.val + totalSum(node.left) + totalSum(node.right)

        total = totalSum(root)

        # Second DFS to compute subtree sums and products
        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            subtree_sum = node.val + left + right

            # Product if we cut above this node
            product = subtree_sum * (total - subtree_sum)
            self.max_product = max(self.max_product, product)

            return subtree_sum

        dfs(root)
        return self.max_product % MOD
