class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            # Calculate the area with the current left and right pointers
            current_height = min(height[left], height[right])
            width = right - left
            current_area = current_height * width
            
            # Update max_area if the current area is larger
            max_area = max(max_area, current_area)

            # Move the pointer pointing to the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
        