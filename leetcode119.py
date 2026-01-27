# LeetCode Problem 119: Pascal's Triangle II


from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        """
        Returns the rowIndex-th row of Pascal's triangle.
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        # The first element of any row is always 1
        row = [1]
        
        # We use the mathematical property: C(n, k) = C(n, k-1) * (n - k + 1) / k
        for k in range(1, rowIndex + 1):
            # Using integer division // to ensure the result stays an int
            next_element = row[-1] * (rowIndex - k + 1) // k
            row.append(next_element)
            
        return row

# --- Test Examples ---
if __name__ == "__main__":
    sol = Solution()
    
    # Test cases: (input_index, expected_output)
    test_cases = [
        (0, [1]),
        (1, [1, 1]),
        (3, [1, 3, 3, 1]),
        (4, [1, 4, 6, 4, 1])
    ]
    
    print("--- Pascal's Triangle: Row Retriever ---")
    for index, expected in test_cases:
        result = sol.getRow(index)
        status = "✅ PASS" if result == expected else "❌ FAIL"
        print(f"Row Index {index}: {result} | {status}")