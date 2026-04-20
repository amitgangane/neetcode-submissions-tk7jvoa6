class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {")":"(", "]":"[", "}":"{"}
        stack = []
        for i in s:
            if i in mapping.values():
                stack.append(i)
            elif i not in mapping.values():
                if not stack or stack[-1]!=mapping[i]:
                    return False
                else:
                    stack.pop(-1)
                
        return len(stack)==0