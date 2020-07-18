#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 旋转数组
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n, count = len(nums), 0
        k %= n
        cur, start = 0, 0

        while count < n:
            cur, prev = start, nums[start]

            while True:
                nxt = (cur + k) % n
                tmp = nums[nxt]
                nums[nxt] = prev
                prev = tmp
                cur = nxt
                count += 1

                if start == cur:
                    break
            
            start += 1


# @lc code=end

