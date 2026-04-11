class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) -1
        max_size = 0
        while i<j:
            s = min(heights[i],heights[j]) * (j-i)
            max_size = max(max_size, s)
            if heights[i] <= heights[j]:
                i +=1
            
            else:
                j-=1
                
            

            
        return max_size

