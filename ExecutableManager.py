from Imports import *
from FilesReader import *
import FunctionManager
import EM0580106P
import EM0660046P
import EM0580107P
import FM05000102
import CSB6400802
import DF06600600
import RD05200200

def StartProgram():
    threading.Thread(target=StartInsertToDataBase()).start()

def StartInsertToDataBase():
    #Reading Files
    FilesReader = filesReader()
    FilesReader.ReadAllFiles()

    # EM0580106P.InsertToDataBase()
    # EM0660046P.InsertToDataBase()
    
    # EM0580107P.InsertToDataBase()

    # FM05000102.InsertToDataBase()

    # CSB6400802.InsertToDataBase()

    # DF06600600.InsertToDataBase()

    # RD05200200.InsertToDataBase()




