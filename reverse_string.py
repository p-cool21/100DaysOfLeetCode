## Day 1 — LeetCode Problem 344: Reverse String

**Problem Description:**
Write a function that reverses a string in-place with O(1) extra memory.

**Approach:**
Used Python's built-in `reverse()` function to reverse the list of characters directly in-place.
This is the most efficient and clean solution since it modifies the list without using extra space.

**Python Solution:**
```python
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
