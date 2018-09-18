class ArrayList:

    def __init__(self):
        self.valueList = []
        self.length = len(self.valueList)

    def insertData(self, i, data):
        self.valueList.insert(i, data)
        return True

    def deleteData(self, i):
        if (i < 0 or i > self.length):
            return False
        value = self.valueList[i]
        for j in range(i, self.length):
            self.valueList[j] = self.valueList[j+1]
        del self.valueList[-1]
        return value

    
