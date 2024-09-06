class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        HashMap = {} #val : index

        for index, val in enumerate(nums): #enumerate allows to iterate and get both index and value at the same time
            difference = target - val           #check if both the values exit so far in the hashmap
            if difference in HashMap:
                return [HashMap[difference], index] 
            HashMap[val] = index # if not, update the index of the hash with the current iterated value and repeat
        return