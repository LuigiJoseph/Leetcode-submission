class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        HashMap = {} #val : index

        for index, val in enumerate(nums):
            difference = target - val
            if difference in HashMap:
                return [HashMap[difference], index]
            HashMap[val] = index
        return