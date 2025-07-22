from Imports import *
import FunctionManager

def StartInsertToDataBase():
    threading.Thread(target=FunctionManager.InsertToDataBase).start()