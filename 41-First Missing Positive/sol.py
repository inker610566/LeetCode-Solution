class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums += [0]
        for i in nums:
            j = i
            while len(nums) > j > 0 and nums[j-1] != j:
                k = nums[j-1]
                nums[j-1] = j
                j = k
        for i, v in enumerate(nums):
            if i+1 != v:
                return i+1
        return len(nums)+1

if __name__ == '__main__':
    print Solution().firstMissingPositive([2, 1])
