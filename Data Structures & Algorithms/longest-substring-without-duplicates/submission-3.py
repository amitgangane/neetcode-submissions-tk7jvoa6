class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        my_dict = {}
        l = 0
        r = l
        maxi = 0
        while r < len(s):
            if s[r] in my_dict:
                l = max(l, my_dict[s[r]]+1)



            maxi = max(maxi, r-l+1)
            my_dict[s[r]] = r
            r +=1
        return maxi


