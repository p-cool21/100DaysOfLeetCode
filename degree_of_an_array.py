class Solution(object):
    def findShortestSubArray(self, nums):
        count = {}
        start = {}
        end = {}
        for i in range(len(nums)):
            if nums[i] not in count:
                count[nums[i]] = 1
                start[nums[i]] = i
                end[nums[i]] = i
            else:
                count[nums[i]] += 1
                end[nums[i]] = i
            result = []
            max_count = max(count.values())
            for i,j in count.items():
                if j == max_count:
                 total = end[i]-start[i] + 1
                 result.append(total)
        return min(result)            