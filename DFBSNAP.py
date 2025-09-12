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

    GuiManager.InsertInLogWindow("DFBSNAP STARTED!")
    GuiManager.Loading()

    Sql.SqlConnection()
    
    for file in DFBSNAPData:
        for s in file.sheet_names:
            row = 0

            if "master" not in s.lower():
                print(s)
                DFBSNAP = file.get_sheet_by_name(s).to_python(skip_empty_area=True)
                DFBSNAP = pd.DataFrame(DFBSNAP)
                DFBSNAP = DFBSNAP.replace(r'\s+', '', regex=True)

                pd.set_option('display.max_columns', None)
                pd.set_option('display.max_rows', None)

                filterData = DFBSNAP.iloc[8:]

                while True:
                    try:
                        perRowFilteredData = filterData.iloc[[row]]
                        perRowFilteredData.columns = [
                            "DATE",
                            "ITEM_BLOCK_CODE",
                            "LETTER_CODE",
                            "DF_RUBBER",
                            "CENTER_PLATE_A",
                            "CENTER_PLATE_B",
                            "DATE_AND_TIME_ANNEALED",
                            "PRODUCED_QTY",
                            "OPERATOR",
                            "JOB_NUMBER"
                        ]

                        # return filterData

                        #Converting Prod_Date To Date Format
                        perRowFilteredData["DATE"].values[0] = f"{pd.to_datetime(perRowFilteredData["DATE"].values[0], dayfirst=True).strftime("%Y%m%d")}-{perRowFilteredData["LETTER_CODE"].values[0]}"

                        perRowFilteredData = perRowFilteredData.drop(['LETTER_CODE'], axis=1)

                        perRowFilteredData["ID"] = f"{perRowFilteredData["DATE"].values[0]}-{row}"

                        cols = perRowFilteredData.columns.tolist()
                        cols.remove('ID')
                        cols.insert(0, 'ID')
                        perRowFilteredData = perRowFilteredData[cols]

                        #CHECKING IF PROD DATE CONTAINS HPI, TO STOP THE LOOP
                        if "HPI" in str(perRowFilteredData["DATE"].values[0]):
                            print("HPI DETECTED")
                            break

                        print(f"LENGTH {len(perRowFilteredData["ITEM_BLOCK_CODE"].values[0])}")

                        if len(perRowFilteredData["ITEM_BLOCK_CODE"].values[0]) == 0:
                            print("BLANK DETECTED")
                            break

                        # compileFrame = pd.concat([compileFrame, perRowFilteredData], ignore_index = True)
                        Sql.InsertDataToDfbSnapTable(perRowFilteredData)

                    except Exception as error:
                        print(error)
                        break

                    row += 1

    GuiManager.InsertInLogWindow("DFBSNAP FINISHED!")
    GuiManager.Loading()

#Reading Files
# FilesReader = filesReader()
# FilesReader.ReadAllFiles()
#%%