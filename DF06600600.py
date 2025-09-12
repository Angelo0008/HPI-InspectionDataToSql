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

    GuiManager.InsertInLogWindow("DF06600600 STARTED!")
    GuiManager.Loading()

    Sql.SqlConnection()

    for a in range(len(DF06600600Data)):
        #Resetting Variables
        columnMover = 6
        emptyDetected = 0

        #Getting The Row, Column Location Of SUPPLIER
        findSupplier = [(index, column) for index, row in DF06600600Data[a].iterrows() for column, value in row.items() if value == "SUPPLIER"]
        supplierRow = [index for index, _ in findSupplier]
        supplierColumn = [column for _, column in findSupplier]
        
        while True:
            try:
                # Get the Neighboring Data Of SUPPLIER
                supplierFiltered = DF06600600Data[a].iloc[
                    max(0, supplierRow[0] - 3):min(len(DF06600600Data[a]), supplierRow[0] + 10),
                    DF06600600Data[a].columns.get_loc(supplierColumn[0] + columnMover):DF06600600Data[a].columns.get_loc(supplierColumn[0]) + 5 + columnMover
                ]
                columnMover += 5

                dataFrame = {
                    "ID": supplierFiltered.iloc[0, 0] + " " + str(supplierFiltered.iloc[1, 0]),
                    "Lot_Number": supplierFiltered.iloc[0, 0],
                    "Date": str(supplierFiltered.iloc[1, 0]),
                    
                    "Inspection_1_Minimum": f"{supplierFiltered.iloc[3].min():.2f}",
                    "Inspection_1_Average": f"{supplierFiltered.iloc[3].mean():.2f}",
                    "Inspection_1_Maximum": f"{supplierFiltered.iloc[3].max():.2f}",
                                    
                    "Inspection_2_Minimum": f"{supplierFiltered.iloc[4].min():.2f}",
                    "Inspection_2_Average": f"{supplierFiltered.iloc[4].mean():.2f}",
                    "Inspection_2_Maximum": f"{supplierFiltered.iloc[4].max():.2f}",
                                    
                    "Inspection_3_Minimum": f"{supplierFiltered.iloc[5].min():.2f}",
                    "Inspection_3_Average": f"{supplierFiltered.iloc[5].mean():.2f}",
                    "Inspection_3_Maximum": f"{supplierFiltered.iloc[5].max():.2f}",
                                    
                    "Inspection_4_Minimum": f"{supplierFiltered.iloc[6].min():.2f}",
                    "Inspection_4_Average": f"{supplierFiltered.iloc[6].mean():.2f}",
                    "Inspection_4_Maximum": f"{supplierFiltered.iloc[6].max():.2f}",
                                    
                    "Inspection_6_Hardness_Test": f"{supplierFiltered.iloc[8].min():.2f}",
                }

                dataFrame = pd.DataFrame([dataFrame])

                Sql.InsertDataToDF06600600InspectionTable(dataFrame)

                if emptyDetected != 0:
                    GuiManager.InsertInLogWindow(f"Empty Detected Beside {str(supplierFiltered.iloc[1, 0])}")
                
                emptyDetected = 0
                # if isInserted > 0:
                #     dataReadCount += 1

                # compiledFrame = pd.concat([compiledFrame, dataFrame], ignore_index=True)
            except:
                emptyDetected += 1

                if emptyDetected < 6:
                    print("Empty Detected Trying Again")
                else:
                    print("Reached The End Of Column")
                    break

        emptyDetected = 0

    GuiManager.FinishedLoading()
    GuiManager.InsertInLogWindow("DF06600600 FINISHED!")

# Reading Files
# FilesReader = filesReader()
# FilesReader.ReadAllFiles()

# InsertToDataBase()
# %%
