from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = None
        margin = None
        for price in prices:
            if min_price is None or price < min_price:
                min_price = price
            else:
                if margin is None or price - min_price > margin:
                    margin = price - min_price
        return margin if margin else 0


print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
print(Solution().maxProfit([7, 6, 4, 3, 1]))
