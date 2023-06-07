class Solution:
    # Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
    # Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
    # Output: 6
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        maxLeft = 0
        maxRight = 0
        left = 0
        right = len(height) - 1
        water = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] > maxLeft:
                    maxLeft = height[left]
                else:
                    water += maxLeft - height[left]
                left += 1
            else:
                if height[right] > maxRight:
                    maxRight = height[right]
                else:
                    water += maxRight - height[right]
                right -= 1
        return water
