#%%
from Imports import *
import Sql
from FilesReader import *
import DateAndTimeManager
import ColumnCreator
import GuiManager

def InsertToDataBase():
    global filterData
    global perRowFilteredData
    global compileFrame

    compileFrame = pd.DataFrame()
    firstRow = 7

    GuiManager.InsertInLogWindow("RDB5200200CheckSheet STARTED")
    GuiManager.Loading()

    Sql.SqlConnection()

    for file in RDB5200200CheckSheet:
        for s in file.sheet_names:
            firstRow = 7

            if "mastercopy" not in s.lower():
                print(s)
                RDB5200200Data = file.get_sheet_by_name(s).to_python(skip_empty_area=True)
                RDB5200200Data = pd.DataFrame(RDB5200200Data)
                RDB5200200Data = RDB5200200Data.replace(r'\s+', '', regex=True)

                pd.set_option('display.max_columns', None)
                pd.set_option('display.max_rows', None)

                filterData = RDB5200200Data.iloc[4:, 0:13]

                while True:
                    try:
                        print(firstRow)
                        perRowFilteredData = filterData.loc[[firstRow]]
                        perRowFilteredData.columns = [
                            "Prod_Date",
                            "1",
                            "2",
                            "3",
                            "4",
                            "5",
                            "6",
                            "7",
                            "Letter_Code",
                            "Material_Lot_Number",
                            "QR_CODE",
                            "PRODUCE_QTY",
                            "JO_NUMBER"
                        ]
                        
                        #Getting The Row, Column Location Of Lot Number
                        findLotNumber = [(index, column) for index, row in RDB5200200Data.iterrows() for column, value in row.items() if str(value) == str(perRowFilteredData["Prod_Date"].values[0])]
                        lotNumberRow = [index for index, _ in findLotNumber]
                        lotNumberColumn = [column for _, column in findLotNumber]

                        #Getting The Tesla Table
                        inspectionData = RDB5200200Data.iloc[max(0, lotNumberRow[0]):min(len(RDB5200200Data), lotNumberRow[0] + 7), RDB5200200Data.columns.get_loc(lotNumberColumn[0] + 21):RDB5200200Data.columns.get_loc(lotNumberColumn[0]) + 26]

                        perRowFilteredData["Rod_Blk_Tesla_1_Minimum_Data"] = inspectionData.iloc[0].min()
                        perRowFilteredData["Rod_Blk_Tesla_1_Average_Data"] = inspectionData.iloc[0].mean()
                        perRowFilteredData["Rod_Blk_Tesla_1_Max_Data"] = inspectionData.iloc[0].max()

                        perRowFilteredData["Rod_Blk_Tesla_2_Minimum_Data"] = inspectionData.iloc[2].min()
                        perRowFilteredData["Rod_Blk_Tesla_2_Average_Data"] = inspectionData.iloc[2].mean()
                        perRowFilteredData["Rod_Blk_Tesla_2_Max_Data"] = inspectionData.iloc[2].max()

                        perRowFilteredData["Rod_Blk_Tesla_3_Minimum_Data"] = inspectionData.iloc[4].min()
                        perRowFilteredData["Rod_Blk_Tesla_3_Average_Data"] = inspectionData.iloc[4].mean()
                        perRowFilteredData["Rod_Blk_Tesla_3_Max_Data"] = inspectionData.iloc[4].max()

                        perRowFilteredData["Rod_Blk_Tesla_4_Minimum_Data"] = inspectionData.iloc[6].min()
                        perRowFilteredData["Rod_Blk_Tesla_4_Average_Data"] = inspectionData.iloc[6].mean()
                        perRowFilteredData["Rod_Blk_Tesla_4_Max_Data"] = inspectionData.iloc[6].max()

                        #Converting Prod_Date To Date Format
                        perRowFilteredData["Prod_Date"].values[0] = pd.to_datetime(perRowFilteredData["Prod_Date"].values[0], dayfirst=True).strftime("%Y%m%d")
                        #Combining Prod_Date And Letter_Code
                        perRowFilteredData["Prod_Date"].values[0] = f"{perRowFilteredData["Prod_Date"].values[0]}-{perRowFilteredData["Letter_Code"].values[0]}"

                        perRowFilteredData["ID"] = f"{perRowFilteredData["Prod_Date"].values[0]}-{firstRow}"

                        perRowFilteredData = perRowFilteredData.drop([
                            "Letter_Code",
                            "1",
                            "2",
                            "3",
                            "4",
                            "5",
                            "6",
                            "7"
                        ], axis=1)

                        # Reorder columns to move DateTime to second position
                        cols = perRowFilteredData.columns.tolist()
                        cols.remove('ID')
                        cols.insert(0, 'ID')
                        perRowFilteredData = perRowFilteredData[cols]

                        Sql.InsertDataToRDB5200200ChecksheetTable(perRowFilteredData)
                        # compileFrame = pd.concat([compileFrame, perRowFilteredData], ignore_index = True)

                    except IndexError as error:
                        print(f"ERROR: {type(error)} : {error}")
                        break

                    except Exception as error:
                        print(f"ERROR: {type(error)} : {error}")
                    
                    #CHECKING IF PROD DATE CONTAINS HPI, TO STOP THE LOOP
                    if "HPI" in str(perRowFilteredData["Prod_Date"].values[0]):
                        print("HPI DETECTED")
                        break

                    firstRow += 1

    GuiManager.FinishedLoading()
    GuiManager.InsertInLogWindow("RDB5200200CheckSheet FINISHED")

# Reading Files
# FilesReader = filesReader()
# FilesReader.ReadAllFiles()
#%%