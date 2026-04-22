class Solution:
    def search(self, nums: List[int], target: int) -> int:
        r = len(nums)
        l = 0
        while l<r:
            mid = (r + l)//2
            if target == nums[mid]:
                return mid
            elif target <= nums[mid]:
                r = mid
            elif target >= nums[mid]:
                l = mid+1
            
        return -1
