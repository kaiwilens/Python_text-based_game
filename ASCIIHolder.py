
#Generic wrapper for ASCII text to be treated as an object
class ASCII:
    __name = str()
    __value = str()

    def __init__(self, name, value):
        self.__name = name
        self.__value = value

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getValue(self):
        return self.__value

    def setValue(self, value):
        self.__value = value

#Generic wrapper to hold ASCII text and generate it into ASCII objects when requested
class ASCIIHolder:
    __indexName=str()
    __arts = dict()
    __indexes = dict()

    def __init__(self, indexName):
        """
        Initializes ASCIIHolder object with values in Index file

        :param indexName
        Loads indexName, text files from indexName, their contents, and stores in the holder's dicts
        """
        self.__indexName=indexName
        self.loadIndex()
        self.updateFiles()

    def getIndex(self): #Get name of index file
        """
        Returns the name of the index file

        :returns self.__indexName
        """
        return self.__indexName

    def setIndex(self, index): #Set name of index file
        """
        Sets the name of the index file

        :param index
        Sets self.__indexName to index param
        """
        self.__indexName=index

    def getArt(self, artKey): #Get art at artKey position
        """
        Returns the art requested as an object of the the ASCII wrapper class

        :param artKey
        Used to find which art you want

        :returns ASCII(artKey, self.__arts[artKey])
        Returns an object of the ASCII wrapper class containing the art requested
        """
        return ASCII(artKey, self.__arts[artKey])

    def setArt(self, artKey, value): #Set art at artKey position
        """
        Sets the art at artKey to the value requested

        :param artKey
        Index of which art to set

        :param value
        Value of what to set the art to
        """
        self.__arts[artKey]=value

    def updateFiles(self): #Read art from folder using stored value of index file
        """
        Updates ASCII art stored in holder

        Used by some initialization functions to load text files properly
        """
        length = len(self.__indexes)
        i = 0
        while(i < length):
            workingFile = open(self.__indexes[i]) #Reads filename from number
            value = workingFile.readLines(len(workingFile.readlines())) #Gets value of fileName
            self.__arts[self.__indexes[i]] = value #Correlates value to filename in dict
            workingFile.close()
            value = ""
            i = i + 1

    def loadNewIndex(self, indexName): #Read values of index file to class
        """
        Reads values of index file to a dictionary in the class

        :param indexName
        Name of the index file to read
        """
        file = open(indexName, "r")
        i = 0
        length = len(file.readlines())
        while(i < length):
            self.__indexes[i] = file.readline(i) #Correlates numbers to filenames
            i = i + 1
        file.close()

    def loadIndex(self): #Same as above but calls on already stored index file name to update without params
        """
        Used to reload the index file currently stored
        """
        self.loadNewIndex(self.__indexName)