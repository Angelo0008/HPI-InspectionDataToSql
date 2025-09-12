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

    GuiManager.InsertInLogWindow("EM0660046P STARTED!")
    GuiManager.Loading()

    Sql.SqlConnection()

    for a in range(len(EM0660046PData)):
        #Resetting Variables
        columnMover = 6
        emptyDetected = 0

        #Getting The Row, Column Location Of SUPPLIER
        findSupplier = [(index, column) for index, row in EM0660046PData[a].iterrows() for column, value in row.items() if value == "SUPPLIER"]
        supplierRow = [index for index, _ in findSupplier]
        supplierColumn = [column for _, column in findSupplier]
        
        while True:
            try:
                # Get the Neighboring Data Of SUPPLIER
                supplierFiltered = EM0660046PData[a].iloc[
                    max(0, supplierRow[0] - 3):min(len(EM0660046PData[a]), supplierRow[0] + 10),
                    EM0660046PData[a].columns.get_loc(supplierColumn[0] + columnMover):EM0660046PData[a].columns.get_loc(supplierColumn[0]) + 5 + columnMover
                ]
                columnMover += 5

                dataFrame = {
                    "ID": supplierFiltered.iloc[0, 0] + " " + str(supplierFiltered.iloc[1, 0]),
                    "Lot_Number": supplierFiltered.iloc[0, 0],
                    "Date": str(supplierFiltered.iloc[1, 0]),

                    "Inspection_3_Minimum": f"{supplierFiltered.iloc[5].min():.2f}",
                    "Inspection_3_Average": f"{supplierFiltered.iloc[5].mean():.2f}",
                    "Inspection_3_Maximum": f"{supplierFiltered.iloc[5].max():.2f}",

                    "Inspection_6_Pull_Test": f"{supplierFiltered.iloc[8].max():.2f}"
                }

                dataFrame = pd.DataFrame([dataFrame])

                Sql.InsertDataToEM0660046PInspectionTable(dataFrame)

                if emptyDetected != 0:
                    GuiManager.InsertInLogWindow(f"Empty Detected Beside {str(supplierFiltered.iloc[1, 0])}")
                
                emptyDetected = 0
                
            except Exception as error:
                print(f"ERROR: {error}")
                emptyDetected += 1

                if emptyDetected < 6:
                    print("Empty Detected Trying Again")
                else:
                    print("Reached The End Of Column")
                    break

        emptyDetected = 0

    GuiManager.FinishedLoading()
    GuiManager.InsertInLogWindow("EM0660046P FINISHED!")

# Reading Files
# FilesReader = filesReader()
# FilesReader.ReadAllFiles()
# %%
