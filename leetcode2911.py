from typing import List
import math

class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        INF = 10**9

        # Precompute all proper divisors of every possible length
        divisors = [[] for _ in range(n + 1)]
        for L in range(2, n + 1):
            for d in range(1, L):
                if L % d == 0:
                    divisors[L].append(d)

        # cost[i][j] = min changes to make s[i..j] a semi-palindrome
        cost = [[INF] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):          # length >= 2
                L = j - i + 1
                best = INF
                for d in divisors[L]:
                    cur = 0
                    for r in range(d):
                        # build the group (or just walk the pairs)
                        left = i + r
                        right = i + r + d * ((L // d) - 1)
                        while left < right:
                            if s[left] != s[right]:
                                cur += 1
                            left += d
                            right -= d
                    best = min(best, cur)
                cost[i][j] = best

        # dp[p][i] = min cost for first i characters into p parts
        dp = [[INF] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0

        for p in range(1, k + 1):
            for i in range(2 * p, n + 1):       # at least 2 chars per part
                for prev in range(2 * (p - 1), i - 1):
                    if dp[p - 1][prev] < INF:
                        dp[p][i] = min(dp[p][i],
                                       dp[p - 1][prev] + cost[prev][i - 1])

        return dp[k][n]
