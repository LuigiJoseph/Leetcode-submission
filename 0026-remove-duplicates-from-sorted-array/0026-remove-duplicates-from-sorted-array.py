class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unique = []

        for i in range(len(nums)):
            if nums[i] not in unique:
                unique.append(nums[i])
        k = len(unique)

        # while len(nums) != len(unique):
            # unique.append(_)

        # Modify nums in place: replace the first k elements with unique elements
        for i in range(k):
            nums[i] = unique[i]

            
        return k