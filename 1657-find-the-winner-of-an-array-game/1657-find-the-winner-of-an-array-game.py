class Solution(object):
    def getWinner(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """

        count = 1
        N = len(arr)
        index = 1
        winner = max(arr[0], arr[1])
        loser = min(arr[0], arr[1])
        arr = [winner] + arr[2:] + [loser]

        while count < k and index < N:
            if arr[0] > arr[index]:
                count += 1
            
            else:
                count = 1
                arr[0] = arr[index]
            
            index += 1
            
        return arr[0]

