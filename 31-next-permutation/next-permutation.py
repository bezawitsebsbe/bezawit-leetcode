class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
    
    # Step 1: Find the longest non-increasing suffix
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:  # Step 2: Find the rightmost successor
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            # Step 3: Swap the pivot
            nums[i], nums[j] = nums[j], nums[i]

        # Step 4: Reverse the suffix
        nums[i + 1:] = reversed(nums[i + 1:])