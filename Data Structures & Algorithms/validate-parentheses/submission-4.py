from collections import defaultdict
class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {"(": ")", "{": "}", "[": "]"}

        hashmap0 = defaultdict(str)
        stack = []
        # if len(s) == 0:
        #     return True
        if not s:
            return True
        for i in s:
            if i in hashmap:
                stack.append(i)
            else:
                if len(stack) != 0 and i == hashmap[stack[-1]]: 
                    stack.pop()
                else:
                    return False 
        # if len(stack) == 0:
        #     return True
        # else:
        #     return False
        return True if not stack else False