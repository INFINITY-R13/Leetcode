# LeetCode Problem 118: Pascal's Triangle


from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """
        Generates the first numRows of Pascal's triangle.
        """
        # Edge case: if numRows is 0, return an empty list
        if numRows == 0:
            return []

        # Initialize the triangle with the first row
        triangle = [[1]]

        for i in range(1, numRows):
            # Start every row with a 1
            prev_row = triangle[i - 1]
            current_row = [1]

            # Each internal element is the sum of the two elements above it
            for j in range(1, i):
                current_row.append(prev_row[j - 1] + prev_row[j])

            # End every row with a 1
            current_row.append(1)
            triangle.append(current_row)

        return triangle

# --- Test Runner ---
if __name__ == "__main__":
    sol = Solution()
    
    # Define test cases: (input, expected_output)
    test_cases = [
        (5, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]),
        (1, [[1]]),
        (0, [])
    ]

    print("Running Pascal's Triangle Tests...\n" + "-"*30)
    for i, (num, expected) in enumerate(test_cases):
        result = sol.generate(num)
        status = "✅ PASS" if result == expected else "❌ FAIL"
        print(f"Test {i+1}: numRows={num}")
        print(f"Result:   {result}")
        print(f"Expected: {expected}")
        print(f"Status:   {status}\n" + "-"*30)