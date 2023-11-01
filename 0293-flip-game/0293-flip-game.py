class Solution(object):
    def generatePossibleNextMoves(self, currentState):
        """
        :type currentState: str
        :rtype: List[str]
        """
        res = []
        for i in range(len(currentState)-1):
            f = (i+1) % len(currentState)
            if (currentState[i] + currentState[f]) == '++':
                res.append(currentState[:i] + '--' + currentState[f + 1:])

        return res

