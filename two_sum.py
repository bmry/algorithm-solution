class Solution(object):
    def twoSum(self, nums, target):
        indices = []
        for num in nums:
            match = target - num
            
            if(match in nums):
                indices.append(nums.index(match))
                indices.append(nums.index(num))
                break
                               
        return indices               
        