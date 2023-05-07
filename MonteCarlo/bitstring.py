import numpy as np
import random


class BitString:
    """
    Simple class to implement a string of bits
    """
    def __init__(self, string):
        self.string = string
        
    def __str__(self):
        newString = ""
        for idx, i in enumerate(self.string):
            newString += str(self.string[idx])
        return newString
        
    def flip(self, index):
        newString = ""
        bitString = str(self)
        for idx, i in enumerate(bitString):
            if(idx == index):
                if(bitString[idx] == '1'):
                    newString += '0'
                else:
                    newString += '1'
            else:
                newString += bitString[idx]
        self.string = newString
        
    def __len__(self):
        count = 0
        for i in self.string:
            count += 1
        return count
    
    def set_string(self, bitString):
        newString = ""
        for i in range(len(bitString)):
            newString += str(bitString[i])
        self.string = newString
        return self.string
        
    def on(self):
        count = 0
        bitString = str(self)
        for idx, i in enumerate(bitString):
            if(bitString[idx] == '1'):
                count += 1
        return count
    
    def off(self):
        return len(self) - self.on()
    
    def int(self):
        intVal = 0
        for idx, i in enumerate(reversed(self.string)):
            intVal += int(i) * 2**idx
        return intVal
    
    def set_int(self, intVal, digits=0):
        newVal = ""
        index = 0
        count = 0
        while(intVal > 0):
            newVal = str(intVal % 2) + newVal
            count += 1
            intVal = intVal // 2
        appendage = ""
        appendageLen = digits - count
        for i in range(appendageLen):
            appendage += '0'
        newVal = appendage + newVal
        self.string = newVal
        return newVal
    
    def __eq__(self, other):
        if(str(self) != str(other)):
            return False
        return True
    
    def initialize(self, M=0, verbose=0):
        """
        Initialize spin configuration with specified magnetization
        
        Parameters
        ----------
        M   : Int, default: 0
            Total number of spin up sites 
        """
        self.config = np.zeros(len(self.string), dtype=int) 
        randomlist = random.sample(range(0, len(self.string)), M)
        for i in randomlist:
            self.flip(i)