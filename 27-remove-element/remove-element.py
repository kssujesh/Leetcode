class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0
        for i in nums:
            if i == val:
                continue
            else:
                nums[k] = i
                k += 1
        return k