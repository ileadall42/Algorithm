class Solution:

    # 找一个时间重构逻辑
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        finalList = []

        def getSpaceList(spaceNum, padNum):
            spaceList = [(spaceNum//padNum)+1] * padNum
            modNum = spaceNum % padNum
            for i in range(modNum):
                spaceList[i] += 1
            return spaceList

        currentLine = ""
        while (words):
            headWord = words[0]
            if len(currentLine) + len(headWord) <= maxWidth:
                headWord = words.pop(0)
                currentLine = currentLine + headWord + " "
            else:
                currentNew = currentLine.strip()
                currentLen = len(currentLine)
                if currentLen <= maxWidth:
                    currentLine = currentLine.strip()  # 恰好为16时
                    if len(currentLine) == maxWidth:
                        currentNew = currentLine
                    else:
                        lineWords = currentLine.split(" ")
                        pad = len(lineWords) - 1
                        if pad == 0:
                            currentNew = lineWords[0] + \
                                (maxWidth-len(currentLine)) * " "
                        else:
                            spaceList = getSpaceList(
                                maxWidth-len(currentLine), pad)
                            currentNew = ""
                            for i in range(pad):
                                currentNew = currentNew + \
                                    lineWords[i] + " " * spaceList[i]
                            currentNew = currentNew + lineWords[-1]
                finalList.append(currentNew)
                currentLine = ""
        currentLine = currentLine.strip()
        currentLine = currentLine + (maxWidth-len(currentLine)) * " "
        finalList.append(currentLine)
        return finalList
