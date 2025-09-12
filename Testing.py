#%%
from Imports import *
import Sql
import ExecutableManager
# import GuiManager
# from FunctionManager import *
from FilesReader import *

# Sql.SqlConnection()

# Sql.CreateEM0580106PInspection()
# Sql.CreateEM0580107PInspection()
# Sql.CreateFM05000102Inspection()
# Sql.CreateCSB6400802Inspection()
# Sql.CreateDF06600600Inspection()
# Sql.CreateRD05200200Inspection()
# Sql.CreateRD05200200ChecksheetTable()
# Sql.CreateDfbSnapData()
# Sql.CreateDfbTensileData()

# em0660046PDataManager = EM0660046PDataManager()
# em0660046PDataManager.InsertToDatabase()


# FilesReader = filesReader()
# FilesReader.ReadAllFiles()

DFBSNAPData = []

vt1Directory = (fr'\\192.168.2.19\production\2025\2. Online Checksheet\Outjob\OUTJOB MATERIAL MONITORING CHECKSHEET')
os.chdir(vt1Directory)

files = glob.glob('*.xlsx') + glob.glob('*.xlsm')
files2 = []
for a in files:
    if '$' not in a:
        files2.append(a)

#Checking Each Files In Files;
for f in files2:
    if 'SNAP' in f:
        workbook = CalamineWorkbook.from_path(f)
        DFBSNAPData.append(workbook)



# #Checking Each Files In Files;
# for f in files:
#     if 'SNAP' in f:
#         workbook = CalamineWorkbook.from_path(f)

#         snapData = pd.DataFrame(workbook)
#         snapData = snapData.replace(r'\s+', '', regex=True)

#         DFBSNAPData.append(snapData)

# %%
