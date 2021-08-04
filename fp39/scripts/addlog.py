#!/usr/bin/env python
import re
import os
import sys
""" 
At times, we may not know the flow. In order to see, we add the log statement in the operation / method of .act file.
This script can add the log statement at begin and end of an operation in act file instead of manually add the same.
It is helpful to automatically add the log when the file is big or required to change multiple files.
And generates changed file under /tmp directory. This is to not overwrite the original in case of this script incorrect places the logging.
Once you confirm the new file is good, have backup of original and place this file before building the component.
Takes an input parameter i.e., absolute path of .act file
"""

class AddLog :
 
    def __init__(self, inputFile) :        
        text = '\tSWBuiltIn::traceMsg("===%s %s");'
        message = ''
        self.outputFile = '/tmp/' + os.path.basename(inputFile)        
        self.myList = []
        with open(inputFile) as f :
            content = f.read().splitlines()
            
        for line in content :
            pattern = 'action ([::]?[\w]?)+'
            result = re.match(pattern, line)
            if result :
                self.myList.append(line)
                message = line.replace('action ', '')
            elif line.startswith('{`') :        
                self.myList.append(line)
                self.myList.append(text%(message, 'start'))
            elif line.startswith('`}') :
                self.myList.append(text%(message, 'end'))
                self.swapLineIfReturn()
                self.myList.append(line)
                message = ''
            else :
                self.myList.append(line)
                
    def getIndex(self, index) :
        previousItem = self.myList[len(self.myList)-index]
        if ('}' in previousItem) or ('{`' in previousItem) :
            return 0
        elif previousItem.endswith(';') and 'return' in previousItem :
            return 2
        elif 'return' in previousItem :
            return index
        elif previousItem.endswith(',') :
            return self.getIndex(index+1)
        elif previousItem.endswith(';') and not('return' in previousItem) :
            return self.getIndex(index+1)
        else :
            return 0
            
    def swapLineIfReturn(self) :
        newIndex = self.getIndex(2)
        length = len(self.myList)
        value = self.myList[length -1] 
        if (0 == newIndex) :	
            pass
        else:
            if 2 == newIndex :
               self.myList[length-1], self.myList[length-newIndex] = self.myList[length-newIndex], self.myList[length-1]
            else :
                self.myList.remove(value)
                self.myList.insert(length - newIndex, value)        
                 
    
    def write(self) :
        print('writing file at {0}'.format(self.outputFile))
        f=open(self.outputFile,"w")
        for r in self.myList :
            print >> f, r

        f.close()
        return

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise ValueError('Please provide input file name')
    log = AddLog(sys.argv[1])
    log.write()
