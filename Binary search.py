"""
Question one
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

Ref: LeetCode

"""
class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_aixs, max_aixs = 0, len(nums) - 1
        while max_aixs > min_aixs:
            mid_aixs = (min_aixs + max_aixs) // 2
            if nums[mid_aixs] < nums[max_aixs]:
                max_aixs = mid_aixs
            else:
                min_aixs = mid_aixs + 1
        return nums[min_aixs]
      
"""
Question two
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,4,4,5,6,7] might become:

[4,5,6,7,0,1,4] if it was rotated 4 times.
[0,1,4,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums that may contain duplicates, return the minimum element of this array.

You must decrease the overall operation steps as much as possible.

Ref: LeetCode
 
 """
class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_aixs, max_aixs = 0, len(nums) - 1
        while max_aixs > min_aixs:
            mid_aixs = (min_aixs + max_aixs) // 2
            if nums[mid_aixs] < nums[max_aixs]:
                max_aixs = mid_aixs
            elif nums[mid_aixs] == nums[max_aixs]:
                max_aixs -= 1
            else:
                min_aixs = mid_aixs + 1
        return nums[min_aixs]
