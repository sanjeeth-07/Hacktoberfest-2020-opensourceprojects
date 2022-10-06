class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        current_index = 0
        for i in range(0,len(nums)):
            if nums[i] != 0:
                nums[current_index] = nums[i]
                current_index += 1
        for j in range(current_index, len(nums)):
            nums[j] = 0
