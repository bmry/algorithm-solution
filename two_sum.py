class Solution(object):
    def twoSum(self, nums, target):
        indices = []
        if(len(nums) == 2):
            return [0,1]
        
        for i,num in enumerate(nums):
            match = target - num
            
            if(match in nums):
                first_number_index = nums.index(match)
                current_index = i
                if(first_number_index != current_index):
                    indices.append(first_number_index)
                    indices.append(current_index)
                    break
                                 
        return indices               
        