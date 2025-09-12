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

    GuiManager.InsertInLogWindow("EM0580106P STARTED")
    GuiManager.Loading()

    Sql.SqlConnection()

    #Creating Empty Columns
    ColumnCreator.createEmptyColumn()
    compiledFrame = pd.DataFrame(columns=ColumnCreator.emptyColumn)

    for a in range(len(EM0580106PData)):
        #Resetting Variables
        columnMover = 6
        emptyDetected = 0

        #Getting The Row, Column Location Of SUPPLIER
        findSupplier = [(index, column) for index, row in EM0580106PData[a].iterrows() for column, value in row.items() if value == "SUPPLIER"]
        supplierRow = [index for index, _ in findSupplier]
        supplierColumn = [column for _, column in findSupplier]
        
        while True:
            try:
                # Get the Neighboring Data Of SUPPLIER
                supplierFiltered = EM0580106PData[a].iloc[
                    max(0, supplierRow[0] - 3):min(len(EM0580106PData[a]), supplierRow[0] + 10),
                    EM0580106PData[a].columns.get_loc(supplierColumn[0] + columnMover):EM0580106PData[a].columns.get_loc(supplierColumn[0]) + 5 + columnMover
                ]
                columnMover += 5

                dataFrame = {
                    "ID": supplierFiltered.iloc[0, 0] + " " + str(supplierFiltered.iloc[1, 0]),
                    "Lot_Number": supplierFiltered.iloc[0, 0],
                    "Date": str(supplierFiltered.iloc[1, 0]),
                    "Inspection_3_Resistance_Minimum": f"{supplierFiltered.iloc[5].min():.2f}",
                    "Inspection_3_Resistance_Average": f"{supplierFiltered.iloc[5].mean():.2f}",
                    "Inspection_3_Resistance_Maximum": f"{supplierFiltered.iloc[5].max():.2f}",

                    "Inspection_4_Dimension_Minimum": f"{supplierFiltered.iloc[6].min():.2f}",
                    "Inspection_4_Dimension_Average": f"{supplierFiltered.iloc[6].mean():.2f}",
                    "Inspection_4_Dimension_Maximum": f"{supplierFiltered.iloc[6].max():.2f}",

                    "Inspection_5_Dimension_Minimum": f"{supplierFiltered.iloc[7].min():.2f}",
                    "Inspection_5_Dimension_Average": f"{supplierFiltered.iloc[7].mean():.2f}",
                    "Inspection_5_Dimension_Maximum": f"{supplierFiltered.iloc[7].max():.2f}",

                    "Inspection_10_Pull_Test": supplierFiltered.iloc[12, 0]
                }

                dataFrame = pd.DataFrame([dataFrame])

                Sql.InsertDataToEM0580106PInspectionTable(dataFrame)

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
    GuiManager.InsertInLogWindow("EM0580106P FINISHED")