class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        total = sum(nums)
        curS = 0
        ans = []
        
        for i in nums:
            curS += i
            ans.append(i)
            
            if curS > total-curS:
                break
        return ans
        