class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        j = len(numbers)-1
        i = 0
        
        while i<j:
            if target - numbers[i] < numbers[j]:
                j -=1
                continue
            if target -numbers[j] > numbers[i]:
                i +=1
                continue
            else:
                return [i+1,j+1]
           
        return []