from collections import Counter

class Solution:
    def smallestUniqueSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        # Base and moduli for double rolling hash
        BASE1, MOD1 = 911382323, 10**9 + 7
        BASE2, MOD2 = 972663749, 10**9 + 9

        # Precompute powers
        pow1 = [1] * (n + 1)
        pow2 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow1[i] = (pow1[i - 1] * BASE1) % MOD1
            pow2[i] = (pow2[i - 1] * BASE2) % MOD2

        # Prefix hashes
        h1 = [0] * (n + 1)
        h2 = [0] * (n + 1)
        for i in range(n):
            h1[i + 1] = (h1[i] * BASE1 + nums[i]) % MOD1
            h2[i + 1] = (h2[i] * BASE2 + nums[i]) % MOD2

        def get_hash(l: int, r: int) -> tuple[int, int]:
            # hash of nums[l..r] (0-based, inclusive)
            x1 = (h1[r + 1] - h1[l] * pow1[r - l + 1]) % MOD1
            x2 = (h2[r + 1] - h2[l] * pow2[r - l + 1]) % MOD2
            return (x1, x2)

        def has_unique(mid: int) -> bool:
            if mid > n:
                return False
            cnt = Counter()
            for i in range(n - mid + 1):
                cnt[get_hash(i, i + mid - 1)] += 1
            return any(v == 1 for v in cnt.values())

        lo, hi = 1, n
        ans = n
        while lo <= hi:
            mid = (lo + hi) // 2
            if has_unique(mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return ans
