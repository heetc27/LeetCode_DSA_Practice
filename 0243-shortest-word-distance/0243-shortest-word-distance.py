class Solution(object):
    def shortestDistance(self, wordsDict, word1, word2):
        """
        :type wordsDict: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        mark1 = []
        mark2 = []
        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                mark1.append(i)
            elif wordsDict[i] == word2:
                mark2.append(i)
            else:
                continue
        dist = []
        for i in range(len(mark1)):
            for j in range(len(mark2)):
                dist.append(abs(mark1[i] - mark2[j]))
        print(mark1)
        print(mark2)
        print(dist)
        return min(dist)

 


