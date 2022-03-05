## 题目描述
找出数组中重复的数字。


在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

## 示例
示例 1：

输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3 
## 方法一
从当前位置的后面的元素查找当前位置的元素。
```python
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        a = nums[0]
        for i in range(1, len(nums)):
            if a in nums[i:]:
                return a
            else:
                a = nums[i]
```

## 方法二
利用排序思想，如果相邻两个元素相等则返回。
```python
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == nums[i+1]:
                return nums[i]
```

## 方法三
建立一个空列表，然后遍历列表，如果当前元素不在列表中，则入列表，否则返回当前元素。
```python
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        a = []
        for i in nums:
            if i in a:
                return i
            else:
                a.append(i)
```

