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

    global rateOfChangeList
    global rateOfChangeMin
    global rateOfChangeAve
    global rateOfChangeMax

    global startForceList
    global startForceMin
    global startForceAve
    global startForceMax

    global terminatingForceList
    global terminatingForceMin
    global terminatingForceAve
    global terminatingForceMax


    compileFrame = pd.DataFrame()

    rateOfChangeList = []
    rateOfChangeMin = None
    rateOfChangeAve = None
    rateOfChangeMax = None

    startForceList = []
    startForceMin = None
    startForceAve = None
    startForceMax = None

    terminatingForceList = []
    terminatingForceMin = None
    terminatingForceAve = None
    terminatingForceMax = None

    GuiManager.InsertInLogWindow("TENSILE STARTED!")
    GuiManager.Loading()

    Sql.SqlConnection()

    for file in TENSILEData:
        row = 0

        pd.set_option('display.max_columns', None)
        pd.set_option('display.max_rows', None)

        filterData = file.iloc[4:, 1:]

        filterData.columns = [
            "DATE",
            "ITEM_CODE",
            "DF_LOT_NO",
            "HARDNESS",
            "RECORD",
            "RATE_OF_CHANGE",
            "AVERAGE_RATE_OF_CHANGE",
            "START_POSITION",
            "END_POSITION",
            "START_FORCE_N",
            "TERMINATING_FORCE_N",
            "AIR_VOLUME",
            "WATTAGE"
        ]

        filterData = filterData.drop(["DATE", "HARDNESS", "AVERAGE_RATE_OF_CHANGE", "START_POSITION", "END_POSITION", "AIR_VOLUME", "WATTAGE", "RECORD"], axis=1)
        
        lotNumbers = filterData["DF_LOT_NO"].str.replace(" ", "").unique()

        for a in lotNumbers:
            print(a)
            df = filterData[(filterData["DF_LOT_NO"].str.replace(" ", "").isin([a]))]

            rateOfChangeMin = df["RATE_OF_CHANGE"].min()
            rateOfChangeMin = f"{rateOfChangeMin:.2f}"

            rateOfChangeAve = df["RATE_OF_CHANGE"].mean()
            rateOfChangeAve = f"{rateOfChangeAve:.2f}"

            rateOfChangeMax= df["RATE_OF_CHANGE"].max()
            rateOfChangeMax = f"{rateOfChangeMax:.2f}"

            startForceMin = df["START_FORCE_N"].min()
            startForceMin = f"{startForceMin:.1f}"

            startForceAve = df["START_FORCE_N"].mean()
            startForceAve = f"{startForceAve:.1f}"

            startForceMax = df["START_FORCE_N"].max()
            startForceMax = f"{startForceMax:.1f}"

            terminatingForceMin = df["TERMINATING_FORCE_N"].min()
            terminatingForceMin = f"{terminatingForceMin:.1f}"

            terminatingForceAve = df["TERMINATING_FORCE_N"].mean()
            terminatingForceAve = f"{terminatingForceAve:.1f}"

            terminatingForceMax = df["TERMINATING_FORCE_N"].max()
            terminatingForceMax = f"{terminatingForceMax:.1f}"
            




            dataFrame = {
                "ID": f"DF06600600-{a}",
                "ITEM_CODE": "DF06600600",
                "DF_LOT_NO": [a],
                "RATE_OF_CHANGE_MIN": rateOfChangeMin,
                "RATE_OF_CHANGE_AVE": rateOfChangeAve,
                "RATE_OF_CHANGE_MAX": rateOfChangeMax,

                "START_FORCE_MIN": startForceMin,
                "START_FORCE_AVE": startForceAve,
                "START_FORCE_MAX": startForceMax,

                "TERMINATING_FORCE_MIN": terminatingForceMin,
                "TERMINATING_FORCE_AVE": terminatingForceAve,
                "TERMINATING_FORCE_MAX": terminatingForceMax
            }

            dataFrame = pd.DataFrame(dataFrame)

            Sql.InsertDataToDfbTensileTable(dataFrame)

            # compileFrame = pd.concat([compileFrame, dataFrame], ignore_index = True)

    GuiManager.InsertInLogWindow("TENSILE FINISHED!")
    GuiManager.Loading()