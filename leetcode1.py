# 1. Two Sum
"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order."""


def twoSum(nums, target):
       num_to_index = {}
       for index, num in enumerate(nums):
           required = target - num
           if required in num_to_index:
               return [num_to_index[required], index]
           num_to_index[num] = index
       return []

# Test cases
print(twoSum([2, 7, 11, 15], 9))  # [0, 1]
print(twoSum([3, 2, 4], 6))       # [1, 2]
print(twoSum([3, 3], 6))          # [0, 1]
