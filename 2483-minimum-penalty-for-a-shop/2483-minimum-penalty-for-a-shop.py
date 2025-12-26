class Solution:
    def bestClosingTime(self, customers):
        penalty = customers.count('Y')  # closing at hour 0
        min_penalty = penalty
        best_hour = 0

        for j in range(len(customers)):
            if customers[j] == 'Y':
                penalty -= 1
            else:  # 'N'
                penalty += 1

            if penalty < min_penalty:
                min_penalty = penalty
                best_hour = j + 1

        return best_hour
