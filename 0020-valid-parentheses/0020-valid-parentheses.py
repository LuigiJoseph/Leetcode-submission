class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        Close_to_open = { ")" : "(",
                                       "}" : "{",
                                       "]" : "["} #Hash map for parentheseess
        for c in s:
            if c in Close_to_open:
                if stack and stack[-1] == Close_to_open[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        
        if not stack:
            return True
        return False