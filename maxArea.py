class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        lMax = 0
        rMax = len(height)-1
        
        while lMax < rMax:

            
            area = (rMax - lMax) * min(height[lMax], height[rMax])
            if area > maxArea:
                maxArea = area
            if height[lMax] > height[rMax]:
                rMax -= 1
            else:
                lMax += 1

        return maxArea