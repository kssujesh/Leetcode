class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        mini = 99999
        maxi = 0

        for i in prices:
            mini = min(i,mini)
            maxi = max(maxi,i-mini)
        return maxi
