from math import inf
from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        f = [0] * (budget + 1)          # f[j] = max copies obtainable by activating a subset that costs exactly j
        mn = inf
        for factor, price in items:
            mn = min(mn, price)
            # number of items whose factor is a multiple of 'factor' (includes itself)
            cnt = sum(fj % factor == 0 for fj, _ in items)
            # 0-1 knapsack update (reverse order)
            for j in range(budget, price - 1, -1):
                f[j] = max(f[j], f[j - price] + cnt)
        # for every possible activation cost i, add as many cheapest items as the leftover budget allows
        return max(x + (budget - i) // mn for i, x in enumerate(f))
