class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count, max = 0, 0
        for i in nums:
            if i == 1: count += 1
            else:
                if count >= max: max = count
                count = 0
        else:
            if count > max: max = count
        return max

            