# LeetCode Problem 121: Best Time to Buy and Sell Stock


def maxProfit(prices):
    if not prices or len(prices) < 2:
        return 0
    
    min_price = float('inf')
    max_profit = 0
    
    for price in prices:
        # Update minimum price if current price is lower
        min_price = min(min_price, price)
        
        # Calculate profit if we sell at current price
        profit = price - min_price
        
        # Update maximum profit if current profit is better
        max_profit = max(max_profit, profit)
    
    return max_profit


# Test Cases
print("Test Case 1:")
prices1 = [7, 1, 5, 3, 6, 4]
result1 = maxProfit(prices1)
print(f"Input: {prices1}")
print(f"Output: {result1}")
print(f"Expected: 5 (buy at 1, sell at 6)")
print()

print("Test Case 2:")
prices2 = [7, 6, 4, 3, 1]
result2 = maxProfit(prices2)
print(f"Input: {prices2}")
print(f"Output: {result2}")
print(f"Expected: 0 (no profit possible)")
print()

print("Test Case 3:")
prices3 = [1, 2]
result3 = maxProfit(prices3)
print(f"Input: {prices3}")
print(f"Output: {result3}")
print(f"Expected: 1 (buy at 1, sell at 2)")
print()

print("Test Case 4:")
prices4 = [5]
result4 = maxProfit(prices4)
print(f"Input: {prices4}")
print(f"Output: {result4}")
print(f"Expected: 0 (only one day)")
print()

print("Test Case 5:")
prices5 = [2, 4, 1]
result5 = maxProfit(prices5)
print(f"Input: {prices5}")
print(f"Output: {result5}")
print(f"Expected: 2 (buy at 2, sell at 4)")
print()

print("Test Case 6:")
prices6 = [3, 2, 6, 5, 0, 3]
result6 = maxProfit(prices6)
print(f"Input: {prices6}")
print(f"Output: {result6}")
print(f"Expected: 4 (buy at 2, sell at 6)")