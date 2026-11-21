from collections import defaultdict
from typing import List

class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(s)
        g = [[] for _ in range(n)]
        for i in range(1, n):
            g[parent[i]].append(i)

        d = defaultdict(list)          # character -> stack of nodes on current path
        ans = [0] * n

        def dfs(i: int, fa: int) -> None:
            ans[i] = 1
            d[s[i]].append(i)
            for j in g[i]:
                dfs(j, i)
            # closest same-character ancestor, or original parent
            k = d[s[i]][-2] if len(d[s[i]]) > 1 else fa
            if k != -1:
                ans[k] += ans[i]
            d[s[i]].pop()

        dfs(0, -1)
        return ans
