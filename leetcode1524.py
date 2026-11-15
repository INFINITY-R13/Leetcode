class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        MOD = 10**9 + 7

        even = 1
        odd = 0
        result = 0

        prefix_parity = 0

        for num in arr:
            prefix_parity = (prefix_parity + num) % 2

            if prefix_parity == 1:
                result += even
                odd += 1
            else:
                result += odd
                even += 1

            result %= MOD

        return result
