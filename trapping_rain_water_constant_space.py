class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        
        units = 0
        while left < right:
            if left_max < right_max:
                left += 1
                addition = left_max - height[left]
                if addition > 0:
                    units += addition
                left_max = max(left_max, height[left])
            else:
                right -= 1
                addition = right_max - height[right]
                if addition > 0:
                    units += addition
                right_max = max(right_max, height[right])
                    
        return units     
        