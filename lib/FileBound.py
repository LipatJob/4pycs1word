from abc import ABC, abstractmethod

class FileBound(ABC):
    """ An abstract class that allows children classes to serialize and deserialize data """
    def __init__(self, fileHandler, dataDecodingStrategy, dataEncodingStrategy):
        self.fileHandler = fileHandler
        self.dataEncodingStrategy = dataEncodingStrategy
        self.dataDecodingStrategy = dataDecodingStrategy
    
    
    def saveState(self):
        """ Write data of this object to the attached file """
        try:
            dataString = self.dataEncodingStrategy.encode(self.toSerializable())
            self.fileHandler.updateData(dataString)
        except:
            print("There was a problem with saving a file")
        
        
    def retrieveState(self):
        """ Set data of this object from the attached file"""
        try:
            dataString = self.fileHandler.readData()
            dataArray = self.dataDecodingStrategy.decode(dataString)
        except:
            print("There was a problem with reading a file")
        self.setData(dataArray)
    
    
    @abstractmethod
    def toSerializable(self):
        """ Convert the data object into a datatype that can be serializable by the strategy """
        pass
    
    
    @abstractmethod
    def setData(self, data):
        """ Set values from data parameter into fields of this object """
        pass