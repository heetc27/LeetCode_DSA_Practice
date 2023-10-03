class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        for p in path.split("/"):
            if p == "..":
                if stack:
                    stack.pop()
            elif p == "." or not p:
                continue
            else:
                stack.append(p)
        ans = "/"+"/".join(stack)
        return ans




