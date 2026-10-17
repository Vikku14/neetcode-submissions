class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2
        arr = [1,2]
        for i in range(n-2):
            arr.append(arr[-1] + arr[-2])
        return arr[-1]


        