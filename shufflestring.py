class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        answer = ""
        for i in range(len(indices)):
            answer += s[indices.index(i)]
        return answer
