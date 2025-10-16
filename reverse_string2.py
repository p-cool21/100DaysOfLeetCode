class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        res = ""
        for i in range(0, len(s), 2 * k):
            part = s[i:i + 2 * k]
            res += part[:k][::-1] + part[k:]
        return res

        
       
