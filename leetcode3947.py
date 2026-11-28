from typing import List
from collections import Counter

class Solution:
    def maximumItems(self, items: List[List[int]], budget: int) -> int:
        # Rename this method if your judge expects a different signature.
        freq = Counter(factor for factor, _ in items)
        max_factor = max(freq)
        p_min = min(price for _, price in items)

        cache = {}

        def count_free(f):
            if f not in cache:
                # Use whichever way of counting is cheaper
                if max_factor // f <= len(freq):
                    total = sum(freq.get(m, 0)
                                for m in range(f, max_factor + 1, f))
                else:
                    total = sum(v for x, v in freq.items() if x % f == 0)
                cache[f] = total - 1  # exclude the item itself
            return cache[f]

        answer = 0
        remaining = budget

        # Only these bonus copies are worth buying
        useful = sorted(
            (price, factor)
            for factor, price in items
            if price < 2 * p_min
        )

        for price, factor in useful:
            take = min(count_free(factor), remaining // price)
            answer += 2 * take
            remaining -= take * price

        # Spend the rest on the cheapest item
        return answer + remaining // p_min
