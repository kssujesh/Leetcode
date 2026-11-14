class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        w = 0
        for i in nums:
            if w == 0 or nums[w-1] != i:
                nums[w] = i
                w += 1
        return w