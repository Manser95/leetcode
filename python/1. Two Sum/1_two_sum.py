class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, num in enumerate(nums):
            for j in range(i+1,len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]
                    
            


if __name__ == "__main__":
    s = Solution()
    print(s.twoSum(nums = [2,7,11,15], target = 9))