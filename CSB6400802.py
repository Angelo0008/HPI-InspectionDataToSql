#%%
from Imports import *
import Sql
from FilesReader import *
import DateAndTimeManager
import ColumnCreator
import GuiManager

def InsertToDataBase():
    global supplierFiltered

    columnMover = 6
    emptyDetected = 0
    supplierFiltered = None

    GuiManager.InsertInLogWindow("Started!")
    GuiManager.Loading()

    Sql.SqlConnection()

    for a in range(len(CSB6400802Data)):
        #Resetting Variables
        columnMover = 6
        emptyDetected = 0

        #Getting The Row, Column Location Of SUPPLIER
        findSupplier = [(index, column) for index, row in CSB6400802Data[a].iterrows() for column, value in row.items() if value == "SUPPLIER"]
        supplierRow = [index for index, _ in findSupplier]
        supplierColumn = [column for _, column in findSupplier]
        
        while True:
            try:
                # Get the Neighboring Data Of SUPPLIER
                supplierFiltered = CSB6400802Data[a].iloc[
                    max(0, supplierRow[0] - 3):min(len(CSB6400802Data[a]), supplierRow[0] + 10),
                    CSB6400802Data[a].columns.get_loc(supplierColumn[0] + columnMover):CSB6400802Data[a].columns.get_loc(supplierColumn[0]) + 5 + columnMover
                ]
                columnMover += 5

                dataFrame = {
                    "ID": supplierFiltered.iloc[0, 0] + " " + str(supplierFiltered.iloc[1, 0]),
                    "Lot_Number": supplierFiltered.iloc[0, 0],
                    "Date": str(supplierFiltered.iloc[1, 0]),
                    "Inspection_1_Minimum": f"{supplierFiltered.iloc[3].min():.2f}",
                    "Inspection_1_Average": f"{supplierFiltered.iloc[3].mean():.2f}",
                    "Inspection_1_Maximum": f"{supplierFiltered.iloc[3].max():.2f}"
                }

                dataFrame = pd.DataFrame([dataFrame])

                Sql.InsertDataToCSB6400802InspectionTable(dataFrame)

                if emptyDetected != 0:
                    GuiManager.InsertInLogWindow(f"Empty Detected Beside {str(supplierFiltered.iloc[1, 0])}")
                
                emptyDetected = 0
                
            except:
                emptyDetected += 1

                if emptyDetected < 6:
                    print("Empty Detected Trying Again")
                else:
                    print("Reached The End Of Column")
                    break

        emptyDetected = 0

    GuiManager.FinishedLoading()
    GuiManager.InsertInLogWindow("Finished!")

#Reading Files
# FilesReader = filesReader()
# FilesReader.ReadAllFiles()
# %%
