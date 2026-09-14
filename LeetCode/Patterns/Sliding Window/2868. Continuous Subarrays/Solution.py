class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        min_q = deque()
        max_q = deque()

        left = 0
        ans = 0

        for right in range(len(nums)):

            # Maintain increasing deque for minimum
            while min_q and nums[min_q[-1]] > nums[right]:
                min_q.pop()
            min_q.append(right)

            # Maintain decreasing deque for maximum
            while max_q and nums[max_q[-1]] < nums[right]:
                max_q.pop()
            max_q.append(right)

            # Window is invalid
            while nums[max_q[0]] - nums[min_q[0]] > 2:
                if min_q[0] == left:
                    min_q.popleft()

                if max_q[0] == left:
                    max_q.popleft()

                left += 1

            # Number of valid subarrays ending at right
            ans += right - left + 1

        return ans

        