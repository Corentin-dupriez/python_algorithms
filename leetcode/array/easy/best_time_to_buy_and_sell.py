from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_index = None
        max_index = 0
        for i in range(0, len(prices)): 
            if min_index is None:
                min_index = i
            elif prices[min_index] > prices[i]:
                min_index = i
        for j in range(min_index, len(prices)): 
            if min_index == len(prices):
                return 0
            if not max_index and prices[j] > prices[min_index]: 
                max_index = j
            elif prices[max_index] < prices[j]: 
                max_index = j
        return  prices[max_index] - prices[min_index] if max_index > min_index -1 else 0

print(Solution().maxProfit([7,1,5,3,6,4]))
print(Solution().maxProfit([7,6,4,3,1]))
print(Solution().maxProfit([1,2]))
print(Solution().maxProfit([1,2,4]))
print(Solution().maxProfit([2,4,1]))