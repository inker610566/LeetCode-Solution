from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        q = deque() # (value, index)
        def Add(value, index):
            while q and q[-1][0] <= value:
                q.pop()
            q.append((value, index))
        result = []
        for idx, v in enumerate(nums):
            Add(v, idx)
            if idx >= k:
                # pop
                if idx-k >= q[0][1]:
                    q.popleft()
            if idx >= k-1:
                result += [q[0][0]]
        return result

if __name__ == '__main__':
    print Solution().maxSlidingWindow([2,1,2,1,2,1,1], 2)

