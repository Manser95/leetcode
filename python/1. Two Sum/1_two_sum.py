class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i, num in enumerate(nums):
            m = target-num
            if m in d:
                return([d[m], i])
            else:
                 d[num] = i


if __name__ == "__main__":
    s = Solution()
    print(s.twoSum(nums=[2, 7, 11, 15], target=9))
