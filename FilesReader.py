#%%
from Imports import *
import DateAndTimeManager

#EM2P
EM0580106PData = []
EM0660046PData = []
EM0660044PData = []

#EM3P
EM0580107PData = []
EM0660047PData = []
EM0660045PData = []

#FM
FM05000102Data = []

#CSB
CSB6400802Data = []

#DFB
DFBSNAPData = []
DF06600600Data = []
TENSILEData = []

#RDB
RDB5200200CheckSheet = []
HPIQAQCData = []
RD05200200Data = []
RDB4200801Data = []

class filesReader():
    global EM0580106PData
    global EM0660046PData
    global EM0660044PData

    global EM0580107PData
    global EM0660047PData
    global EM0660045PData 

    global FM05000102Data

    global CSB6400802Data

    global DFBSNAPData
    global DF06600600Data
    global TENSILEData

    global RDB5200200CheckSheet
    global HPIQAQCData
    global RD05200200Data
    global RDB4200801Data

    #RESETING VALUES
    EM0580106PData = []
    EM0660046PData = []
    EM0660044PData = []

    EM0580107PData = []
    EM0660047PData = []
    EM0660045PData = []

    FM05000102Data = []

    CSB6400802Data = []

    DFBSNAPData = []
    DF06600600Data = []
    TENSILEData = []

    RDB5200200CheckSheet = []
    HPIQAQCData = []
    RD05200200Data = []
    RDB4200801Data = []

    readingYearStored = ""
    readingYear = ""

    def __init__(self):
        DateAndTimeManager.GetDateToday()
        self.readingYearStored = DateAndTimeManager.yearNow
    def ReadEm2pFiles(self):
        self.readingYear = self.readingYearStored

        while True:
            try:
                vt1Directory = (fr'\\192.168.2.19\quality control\{str(self.readingYear)}')

                for d in os.listdir(vt1Directory):
                    if "supplier" in d.lower():
                        vt1Directory = os.path.join(vt1Directory, d)
                        for d in os.listdir(vt1Directory):
                            if "inspection standard" in d.lower():
                                vt1Directory = os.path.join(vt1Directory, d)
                                for d in os.listdir(vt1Directory):
                                    if "receiving inspection record" in d.lower():
                                        vt1Directory = os.path.join(vt1Directory, d)

                                        #GETTING EM0580106P FILES
                                        try:
                                            for d in os.listdir(vt1Directory):
                                                if "gaptec" in d.lower():
                                                    directory = os.path.join(vt1Directory, d)

                                                    #Finding A Folder That Contains New Trend
                                                    for d in os.listdir(directory):
                                                        if 'new trend' in d.lower():
                                                            directory = os.path.join(directory, d)
                                                            print(f"Updated vt1Directory: {directory}")
                                                            break

                                                    os.chdir(directory)

                                                    files = glob.glob('*EM0580106P*.xlsm')
                                                    print(files)

                                                    for f in files:
                                                        print(f'File Readed {f}')
                                                        workbook = CalamineWorkbook.from_path(f)

                                                        em2PData = workbook.get_sheet_by_name("format").to_python(skip_empty_area=True)
                                                        em2PData = pd.DataFrame(em2PData)
                                                        em2PData = em2PData.replace(r'\s+', '', regex=True)
                                                        
                                                        print(f"EM2P FINDED IN {self.readingYear} NEW TREND")
                                                        EM0580106PData.append(em2PData)
                                        except:
                                            print("NO DATA FOUND IN GAPTEC")
                                        try:
                                            for d in os.listdir(vt1Directory):
                                                if "dhye" in d.lower():
                                                    directory = os.path.join(vt1Directory, d)

                                                    #Finding A Folder That Contains New Trend
                                                    for d in os.listdir(directory):
                                                        if 'new trend' in d.lower():
                                                            directory = os.path.join(directory, d)
                                                            print(f"Updated vt1Directory: {directory}")
                                                            break

                                                    os.chdir(directory)

                                                    files = glob.glob('*EM0580106P*.xlsm')
                                                    print(files)

                                                    for f in files:
                                                        print(f'File Readed {f}')
                                                        workbook = CalamineWorkbook.from_path(f)

                                                        em2PData = workbook.get_sheet_by_name("format").to_python(skip_empty_area=True)
                                                        em2PData = pd.DataFrame(em2PData)
                                                        em2PData = em2PData.replace(r'\s+', '', regex=True)
                                                        
                                                        print(f"EM2P FINDED IN {self.readingYear} NEW TREND")
                                                        EM0580106PData.append(em2PData)
                                        except:
                                            print("NO DATA FOUND IN DHYE")






                                        #GETTING EM0660046P FILES
                                        try:
                                            for d in os.listdir(vt1Directory):
                                                if "gaptec" in d.lower():
                                                    directory = os.path.join(vt1Directory, d)

                                                    #Finding A Folder That Contains New Trend
                                                    for d in os.listdir(directory):
                                                        if 'new trend' in d.lower():
                                                            directory = os.path.join(directory, d)
                                                            print(f"Updated vt1Directory: {directory}")
                                                            break

                                                    os.chdir(directory)

                                                    files = glob.glob('*EM0660046P*.xlsm')

                                                    for f in files:
                                                        print(f'File Readed {f}')
                                                        workbook = CalamineWorkbook.from_path(f)

                                                        em2PData = workbook.get_sheet_by_name("format").to_python(skip_empty_area=True)
                                                        em2PData = pd.DataFrame(em2PData)
                                                        em2PData = em2PData.replace(r'\s+', '', regex=True)
                                                        
                                                        print(f"EM2P FINDED IN {self.readingYear} NEW TREND")
                                                        EM0660046PData.append(em2PData)
                                        except:
                                            print("NO DATA FOUND IN GAPTEC")

                                        try:
                                            for d in os.listdir(vt1Directory):
                                                if "dhye" in d.lower():
                                                    directory = os.path.join(vt1Directory, d)

                                                    #Finding A Folder That Contains New Trend
                                                    for d in os.listdir(directory):
                                                        if 'new trend' in d.lower():
                                                            directory = os.path.join(directory, d)
                                                            print(f"Updated vt1Directory: {directory}")
                                                            break

                                                    os.chdir(directory)

                                                    files = glob.glob('*EM0660046P*.xlsm')

                                                    for f in files:
                                                        print(f'File Readed {f}')
                                                        workbook = CalamineWorkbook.from_path(f)

                                                        em2PData = workbook.get_sheet_by_name("format").to_python(skip_empty_area=True)
                                                        em2PData = pd.DataFrame(em2PData)
                                                        em2PData = em2PData.replace(r'\s+', '', regex=True)
                                                        
                                                        print(f"EM2P FINDED IN {self.readingYear} NEW TREND")
                                                        EM0660046PData.append(em2PData)
                                        except:
                                            print("NO DATA FOUND IN DHYE")






                                        #GETTING EM0660044P FILES
                                        try:
                                            for d in os.listdir(vt1Directory):
                                                if "gaptec" in d.lower():
                                                    directory = os.path.join(vt1Directory, d)

                                                    #Finding A Folder That Contains New Trend
                                                    for d in os.listdir(directory):
                                                        if 'new trend' in d.lower():
                                                            directory = os.path.join(directory, d)
                                                            print(f"Updated vt1Directory: {directory}")
                                                            break

                                                    os.chdir(directory)

                                                    files = glob.glob('*EM0660044P*.xlsm')

                                                    for f in files:
                                                        print(f'File Readed {f}')
                                                        workbook = CalamineWorkbook.from_path(f)

                                                        em2PData = workbook.get_sheet_by_name("format").to_python(skip_empty_area=True)
                                                        em2PData = pd.DataFrame(em2PData)
                                                        em2PData = em2PData.replace(r'\s+', '', regex=True)
                                                        
                                                        print(f"EM2P FINDED IN {self.readingYear} NEW TREND")
                                                        EM0660044PData.append(em2PData)
                                        except:
                                            print("NO DATA FOUND IN GAPTEC")

                                        try:
                                            for d in os.listdir(vt1Directory):
                                                if "dhye" in d.lower():
                                                    directory = os.path.join(vt1Directory, d)

                                                    #Finding A Folder That Contains New Trend
                                                    for d in os.listdir(directory):
                                                        if 'new trend' in d.lower():
                                                            directory = os.path.join(directory, d)
                                                            print(f"Updated vt1Directory: {directory}")
                                                            break

                                                    os.chdir(directory)

                                                    files = glob.glob('*EM0660046P*.xlsm')

                                                    for f in files:
                                                        print(f'File Readed {f}')
                                                        workbook = CalamineWorkbook.from_path(f)

                                                        em2PData = workbook.get_sheet_by_name("format").to_python(skip_empty_area=True)
                                                        em2PData = pd.DataFrame(em2PData)
                                                        em2PData = em2PData.replace(r'\s+', '', regex=True)
                                                        
                                                        print(f"EM2P FINDED IN {self.readingYear} NEW TREND")
                                                        EM0660044PData.append(em2PData)
                                        except:
                                            print("NO DATA FOUND IN DHYE")
                                        

            except:
                pass

            if self.readingYear > 2021:
                self.readingYear -= 1
            else:
                # self.fileFinishedReading = True
                break

        #REPLACING BLANK VALUES WITH N/A
        for file in EM0580106PData:
            file.replace('', np.nan, inplace=True)  
        for file in EM0660046PData:
            file.replace('', np.nan, inplace=True)  
        for file in EM0660044PData:
            file.replace('', np.nan, inplace=True)  

    def ReadEm3pFiles(self):
        self.readingYear = self.readingYearStored

        while True:
            try:
                vt1Directory = (fr'\\192.168.2.19\quality control\{str(self.readingYear)}')

                for d in os.listdir(vt1Directory):
                    if "supplier" in d.lower():
                        vt1Directory = os.path.join(vt1Directory, d)
                        for d in os.listdir(vt1Directory):
                            if "inspection standard" in d.lower():
                                vt1Directory = os.path.join(vt1Directory, d)
                                for d in os.listdir(vt1Directory):
                                    if "receiving inspection record" in d.lower():
                                        vt1Directory = os.path.join(vt1Directory, d)

                                        #GETTING EM0580107P FILES
                                        try:
                                            for d in os.listdir(vt1Directory):
                                                if "gaptec" in d.lower():
                                                    directory = os.path.join(vt1Directory, d)

                                                    #Finding A Folder That Contains New Trend
                                                    for d in os.listdir(directory):
                                                        if 'new trend' in d.lower():
                                                            directory = os.path.join(directory, d)
                                                            print(f"Updated vt1Directory: {directory}")
                                                            break

                                                    os.chdir(directory)

                                                    files = glob.glob('*EM0580107P*.xlsm')

                                                    for f in files:
                                                        print(f'File Readed {f}')
                                                        workbook = CalamineWorkbook.from_path(f)

                                                        em3PData = workbook.get_sheet_by_name("format").to_python(skip_empty_area=True)
                                                        em3PData = pd.DataFrame(em3PData)
                                                        em3PData = em3PData.replace(r'\s+', '', regex=True)
                                                        
                                                        print(f"EM3P FINDED IN {self.readingYear} NEW TREND")
                                                        EM0580107PData.append(em3PData)
                                        except:
                                            print("NO DATA FOUND IN GAPTEC")
                                        try:
                                            for d in os.listdir(vt1Directory):
                                                if "dhye" in d.lower():
                                                    directory = os.path.join(vt1Directory, d)

                                                    #Finding A Folder That Contains New Trend
                                                    for d in os.listdir(directory):
                                                        if 'new trend' in d.lower():
                                                            directory = os.path.join(directory, d)
                                                            print(f"Updated vt1Directory: {directory}")
                                                            break

                                                    os.chdir(directory)

                                                    files = glob.glob('*EM0580107P*.xlsm')

                                                    for f in files:
                                                        print(f'File Readed {f}')
                                                        workbook = CalamineWorkbook.from_path(f)

                                                        em3PData = workbook.get_sheet_by_name("format").to_python(skip_empty_area=True)
                                                        em3PData = pd.DataFrame(em3PData)
                                                        em3PData = em3PData.replace(r'\s+', '', regex=True)
                                                        
                                                        print(f"EM3P FINDED IN {self.readingYear} NEW TREND")
                                                        EM0580107PData.append(em3PData)
                                        except:
                                            print("NO DATA FOUND IN DHYE")






                                        #GETTING EM0660047P FILES
                                        try:
                                            for d in os.listdir(vt1Directory):
                                                if "gaptec" in d.lower():
                                                    directory = os.path.join(vt1Directory, d)

                                                    #Finding A Folder That Contains New Trend
                                                    for d in os.listdir(directory):
                                                        if 'new trend' in d.lower():
                                                            directory = os.path.join(directory, d)
                                                            print(f"Updated vt1Directory: {directory}")
                                                            break

                                                    os.chdir(directory)

                                                    files = glob.glob('*EM0660047P*.xlsm')

                                                    for f in files:
                                                        print(f'File Readed {f}')
                                                        workbook = CalamineWorkbook.from_path(f)

                                                        em3PData = workbook.get_sheet_by_name("format").to_python(skip_empty_area=True)
                                                        em3PData = pd.DataFrame(em3PData)
                                                        em3PData = em3PData.replace(r'\s+', '', regex=True)
                                                        
                                                        print(f"EM3P FINDED IN {self.readingYear} NEW TREND")
                                                        EM0660047PData.append(em3PData)
                                        except:
                                            print("NO DATA FOUND IN GAPTEC")
                                        try:
                                            for d in os.listdir(vt1Directory):
                                                if "dhye" in d.lower():
                                                    directory = os.path.join(vt1Directory, d)

                                                    #Finding A Folder That Contains New Trend
                                                    for d in os.listdir(directory):
                                                        if 'new trend' in d.lower():
                                                            directory = os.path.join(directory, d)
                                                            print(f"Updated vt1Directory: {directory}")
                                                            break

                                                    os.chdir(directory)

                                                    files = glob.glob('*EM0660047P*.xlsm')

                                                    for f in files:
                                                        print(f'File Readed {f}')
                                                        workbook = CalamineWorkbook.from_path(f)

                                                        em3PData = workbook.get_sheet_by_name("format").to_python(skip_empty_area=True)
                                                        em3PData = pd.DataFrame(em3PData)
                                                        em3PData = em3PData.replace(r'\s+', '', regex=True)
                                                        
                                                        print(f"EM3P FINDED IN {self.readingYear} NEW TREND")
                                                        EM0660047PData.append(em3PData)
                                        except:
                                            print("NO DATA FOUND IN DHYE")




                                        #GETTING EM0660045P FILES
                                        try:
                                            for d in os.listdir(vt1Directory):
                                                if "gaptec" in d.lower():
                                                    directory = os.path.join(vt1Directory, d)

                                                    #Finding A Folder That Contains New Trend
                                                    for d in os.listdir(directory):
                                                        if 'new trend' in d.lower():
                                                            directory = os.path.join(directory, d)
                                                            print(f"Updated vt1Directory: {directory}")
                                                            break

                                                    os.chdir(directory)

                                                    files = glob.glob('*EM0660045P*.xlsm')

                                                    for f in files:
                                                        print(f'File Readed {f}')
                                                        workbook = CalamineWorkbook.from_path(f)

                                                        em3PData = workbook.get_sheet_by_name("format").to_python(skip_empty_area=True)
                                                        em3PData = pd.DataFrame(em3PData)
                                                        em3PData = em3PData.replace(r'\s+', '', regex=True)
                                                        
                                                        print(f"EM3P FINDED IN {self.readingYear} NEW TREND")
                                                        EM0660045PData.append(em3PData)
                                        except:
                                            print("NO DATA FOUND IN GAPTEC")
                                        try:
                                            for d in os.listdir(vt1Directory):
                                                if "dhye" in d.lower():
                                                    directory = os.path.join(vt1Directory, d)

                                                    #Finding A Folder That Contains New Trend
                                                    for d in os.listdir(directory):
                                                        if 'new trend' in d.lower():
                                                            directory = os.path.join(directory, d)
                                                            print(f"Updated vt1Directory: {directory}")
                                                            break

                                                    os.chdir(directory)

                                                    files = glob.glob('*EM0660045P*.xlsm')

                                                    for f in files:
                                                        print(f'File Readed {f}')
                                                        workbook = CalamineWorkbook.from_path(f)

                                                        em3PData = workbook.get_sheet_by_name("format").to_python(skip_empty_area=True)
                                                        em3PData = pd.DataFrame(em3PData)
                                                        em3PData = em3PData.replace(r'\s+', '', regex=True)
                                                        
                                                        print(f"EM3P FINDED IN {self.readingYear} NEW TREND")
                                                        EM0660045PData.append(em3PData)
                                        except:
                                            print("NO DATA FOUND IN DHYE")


            except:
                pass

            if self.readingYear > 2021:
                self.readingYear -= 1
            else:
                # self.fileFinishedReading = True
                break

        #REPLACING BLANK VALUES WITH N/A
        for file in EM0580107PData:
            file.replace('', np.nan, inplace=True)
        for file in EM0660047PData:
            file.replace('', np.nan, inplace=True)  
        for file in EM0660045PData:
            file.replace('', np.nan, inplace=True)  

    def ReadFmFiles(self):
        self.readingYear = self.readingYearStored

        while True:
            try:
                vt1Directory = (fr'\\192.168.2.19\quality control\{str(self.readingYear)}')

                for d in os.listdir(vt1Directory):
                    if "supplier" in d.lower():
                        vt1Directory = os.path.join(vt1Directory, d)
                        for d in os.listdir(vt1Directory):
                            if "inspection standard" in d.lower():
                                vt1Directory = os.path.join(vt1Directory, d)
                                for d in os.listdir(vt1Directory):
                                    if "receiving inspection record" in d.lower():
                                        vt1Directory = os.path.join(vt1Directory, d)



                                        # GETTING FM05000102 FILES
                                        try:
                                            for d in os.listdir(vt1Directory):
                                                if "cronics" in d.lower():
                                                    directory = os.path.join(vt1Directory, d)

                                                    #Finding A Folder That Contains New Trend
                                                    for d in os.listdir(directory):
                                                        if 'new trend' in d.lower():
                                                            directory = os.path.join(directory, d)
                                                            print(f"Updated vt1Directory: {directory}")
                                                            break

                                                    os.chdir(directory)

                                                    files = glob.glob('*FM05000102*.xlsm')

                                                    for f in files:
                                                        print(f'File Readed {f}')
                                                        workbook = CalamineWorkbook.from_path(f)

                                                        fmData = workbook.get_sheet_by_name("format").to_python(skip_empty_area=True)
                                                        fmData = pd.DataFrame(fmData)
                                                        fmData = fmData.replace(r'\s+', '', regex=True)
                                                        
                                                        print(f"FM FINDED IN {self.readingYear} NEW TREND")
                                                        FM05000102Data.append(fmData)
                                        except:
                                            print("NO DATA FOUND IN CRONICS")
            except:
                pass

            if self.readingYear > 2021:
                self.readingYear -= 1
            else:
                # self.fileFinishedReading = True
                break

        #REPLACING BLANK VALUES WITH N/A
        for file in FM05000102Data:
            file.replace('', np.nan, inplace=True)

    def ReadDfbSnapFiles(self):
        self.readingYear = self.readingYearStored

        while True:
            try:
                if self.readingYear < 2025:
                    vt1Directory = (fr'\\192.168.2.19\{self.readingYear}$')
                else:
                    vt1Directory = (fr'\\192.168.2.19\production\{self.readingYear}')

                for d in os.listdir(vt1Directory):
                    if "online checksheet" in d.lower():
                        vt1Directory = os.path.join(vt1Directory, d)
                        for d in os.listdir(vt1Directory):
                            if "outjob" in d.lower():
                                vt1Directory = os.path.join(vt1Directory, d)
                                for d in os.listdir(vt1Directory):
                                    if "outjob material monitoring checksheet" in d.lower():
                                        vt1Directory = os.path.join(vt1Directory, d)
                                        os.chdir(vt1Directory)
                                        print(f"Updated vt1Directory: {vt1Directory}")

                                        # wb = load_workbook(filename='SNAP.xlsx', data_only=True)

                                        # print(f"SNAP FINDED IN {vt1Directory}")
                                        # DFBSNAPData.append(wb)



                                        #___________________________________________________
                                        #Finding All xlsm Files In The Current Directory
                                    

                                        files = glob.glob('*.xlsx') + glob.glob("*.xlsm")

                                        # print(f"Total Files In {self.readingYear} {len(files)}")
                                        for a in files:
                                            print(f"FILES SEEN {a}")
                                        
                                        # + glob.glob("*.xlsm")

                                        recentTime = 0

                                        #Checking Each Files In Files;
                                        for f in files:
                                            if 'SNAP' in f:
                                                #Checking If It Is Recent File
                                                fileTime = os.path.getmtime(f)
                                                if fileTime > recentTime:
                                                    recentTime = fileTime
                                                    fileName = f

                                        workbook = CalamineWorkbook.from_path(fileName)
                                        DFBSNAPData.append(workbook)
                                        #_______________________________________________________
            except Exception as error:
                print(error)

            if self.readingYear > 2024:
                self.readingYear -= 1
            else:
                # self.fileFinishedReading = True
                break

    def ReadDfbFiles(self):
        self.readingYear = self.readingYearStored

        while True:
            try:
                vt1Directory = (fr'\\192.168.2.19\quality control\{str(self.readingYear)}')

                for d in os.listdir(vt1Directory):
                    if "supplier" in d.lower():
                        vt1Directory = os.path.join(vt1Directory, d)
                        for d in os.listdir(vt1Directory):
                            if "inspection standard" in d.lower():
                                vt1Directory = os.path.join(vt1Directory, d)
                                for d in os.listdir(vt1Directory):
                                    if "receiving inspection record" in d.lower():
                                        vt1Directory = os.path.join(vt1Directory, d)

                                        #GETTING DF06600600 FILES
                                        try:
                                            for d in os.listdir(vt1Directory):
                                                if "takaishi" in d.lower():
                                                    directory = os.path.join(vt1Directory, d)

                                                    #Finding A Folder That Contains New Trend
                                                    for d in os.listdir(directory):
                                                        if 'new trend' in d.lower():
                                                            directory = os.path.join(directory, d)
                                                            print(f"Updated vt1Directory: {directory}")
                                                            break

                                                    os.chdir(directory)

                                                    files = glob.glob('*DF06600600*.xlsm')

                                                    for f in files:
                                                        print(f'File Readed {f}')
                                                        workbook = CalamineWorkbook.from_path(f)

                                                        dfbData = workbook.get_sheet_by_name("format").to_python(skip_empty_area=True)
                                                        dfbData = pd.DataFrame(dfbData)
                                                        dfbData = dfbData.replace(r'\s+', '', regex=True)
                                                        
                                                        print(f"DFB FINDED IN {self.readingYear} NEW TREND")
                                                        DF06600600Data.append(dfbData)
                                        except:
                                            print("NO DATA FOUND IN TAKAISHI")
            except:
                pass

            if self.readingYear > 2021:
                self.readingYear -= 1
            else:
                # self.fileFinishedReading = True
                break
        
        #REPLACING BLANK VALUES WITH N/A
        for file in DF06600600Data:
            file.replace('', np.nan, inplace=True)

    def ReadTensile(self):
        self.readingYear = self.readingYearStored

        while True:
            try:
                vt1Directory = (fr'\\192.168.2.19\quality control\{str(self.readingYear)}')

                for d in os.listdir(vt1Directory):
                    if "supplier" in d.lower():
                        vt1Directory = os.path.join(vt1Directory, d)
                        for d in os.listdir(vt1Directory):
                            if "inspection standard" in d.lower():
                                vt1Directory = os.path.join(vt1Directory, d)
                                for d in os.listdir(vt1Directory):
                                    if "receiving inspection record" in d.lower():
                                        vt1Directory = os.path.join(vt1Directory, d)

                                        #GETTING DF06600600 FILES
                                        try:
                                            for d in os.listdir(vt1Directory):
                                                if "tensile" in d.lower():
                                                    directory = os.path.join(vt1Directory, d)

                                                    print(f"Updated vt1Directory: {directory}")

                                                    os.chdir(directory)

                                                    files = glob.glob('*DF06600600*.xlsx')

                                                    for f in files:
                                                        print(f'File Readed {f}')
                                                        workbook = CalamineWorkbook.from_path(f)

                                                        tensileData = workbook.get_sheet_by_name("Rate_Result_List").to_python(skip_empty_area=True)
                                                        tensileData = pd.DataFrame(tensileData)
                                                        tensileData = tensileData.replace(r'\s+', '', regex=True)
                                                        
                                                        print(f"TENSILE FINDED IN {self.readingYear}")
                                                        TENSILEData.append(tensileData)
                                        except:
                                            print("NO DATA FOUND IN TENSILE")
            except:
                pass

            if self.readingYear > 2021:
                self.readingYear -= 1
            else:
                # self.fileFinishedReading = True
                break
        
        #REPLACING BLANK VALUES WITH N/A
        for file in TENSILEData:
            file.replace('', np.nan, inplace=True)


    def ReadRdbCheckSheetFiles(self):
        self.readingYear = self.readingYearStored

        while True:
            try:
                if self.readingYear < 2025:
                    vt1Directory = (fr'\\192.168.2.19\{self.readingYear}$')
                else:
                    vt1Directory = (fr'\\192.168.2.19\production\{self.readingYear}')

                for d in os.listdir(vt1Directory):
                    if "online checksheet" in d.lower():
                        vt1Directory = os.path.join(vt1Directory, d)
                        for d in os.listdir(vt1Directory):
                            if "outjob" in d.lower():
                                vt1Directory = os.path.join(vt1Directory, d)
                                for d in os.listdir(vt1Directory):
                                    if "rod checksheet" in d.lower():
                                        vt1Directory = os.path.join(vt1Directory, d)

                                        os.chdir(vt1Directory)
                                        print(f"Updated vt1Directory: {vt1Directory}")

                                        #Finding All xlsm Files In The Current Directory
                                        files = glob.glob('*.xlsx')

                                        recentTime = 0

                                        #Checking Each Files In Files;
                                        for f in files:
                                            if 'RDB5200200' in f:
                                                #Checking If It Is Recent File
                                                fileTime = os.path.getmtime(f)
                                                if fileTime > recentTime:
                                                    recentTime = fileTime
                                                    fileName = f

                                        workbook = CalamineWorkbook.from_path(fileName)
                                        RDB5200200CheckSheet.append(workbook)
                            
            except:
                pass

            if self.readingYear > 2024:
                self.readingYear -= 1
            else:
                # self.fileFinishedReading = True
                break

        

    def ReadRdbFiles(self):
        self.readingYear = self.readingYearStored

        while True:
            try:
                vt1Directory = (fr'\\192.168.2.19\quality control\{str(self.readingYear)}')

                for d in os.listdir(vt1Directory):
                    if "supplier" in d.lower():
                        vt1Directory = os.path.join(vt1Directory, d)
                        for d in os.listdir(vt1Directory):
                            if "inspection standard" in d.lower():
                                vt1Directory = os.path.join(vt1Directory, d)
                                for d in os.listdir(vt1Directory):
                                    if "receiving inspection record" in d.lower():
                                        vt1Directory = os.path.join(vt1Directory, d)

                                        #GETTING RD05200200 FILES
                                        try:
                                            for d in os.listdir(vt1Directory):
                                                if "sbros" in d.lower():
                                                    directory = os.path.join(vt1Directory, d)

                                                    #Finding A Folder That Contains New Trend
                                                    for d in os.listdir(directory):
                                                        if 'new trend' in d.lower():
                                                            directory = os.path.join(directory, d)
                                                            print(f"Updated vt1Directory: {directory}")
                                                            break

                                                    os.chdir(directory)

                                                    files = glob.glob('*RD05200200*.xlsm')

                                                    for f in files:
                                                        print(f'File Readed {f}')
                                                        workbook = CalamineWorkbook.from_path(f)

                                                        rdbData = workbook.get_sheet_by_name("format").to_python(skip_empty_area=True)
                                                        rdbData = pd.DataFrame(rdbData)
                                                        rdbData = rdbData.replace(r'\s+', '', regex=True)
                                                        
                                                        # print(f"EM2P FINDED IN {self.readingYear} NEW TREND")
                                                        RD05200200Data.append(rdbData)
                                        except:
                                            print("NO DATA FOUND IN SBROS")

                                        #GETTING RDB4200801 FILES
                                        try:
                                            for d in os.listdir(vt1Directory):
                                                if "ningbo" in d.lower():
                                                    directory = os.path.join(vt1Directory, d)
            
                                                    #Finding A Folder That Contains New Trend
                                                    for d in os.listdir(directory):
                                                        if 'new trend' in d.lower():
                                                            directory = os.path.join(directory, d)
                                                            print(f"Updated vt1Directory: {directory}")
                                                            break

                                                    os.chdir(directory)

                                                    files = glob.glob('*RDB4200801*.xlsm')

                                                    for f in files:
                                                        print(f'File Readed {f}')
                                                        workbook = CalamineWorkbook.from_path(f)

                                                        rdbData = workbook.get_sheet_by_name("format").to_python(skip_empty_area=True)
                                                        rdbData = pd.DataFrame(rdbData)
                                                        rdbData = rdbData.replace(r'\s+', '', regex=True)
                                                        
                                                        # print(f"EM2P FINDED IN {self.readingYear} NEW TREND")
                                                        RDB4200801Data.append(rdbData)

                                        except:
                                            print("NO DATA FOUND IN NINGBO")
            except:
                pass

            if self.readingYear > 2021:
                self.readingYear -= 1
            else:
                # self.fileFinishedReading = True
                break

        #REPLACING BLANK VALUES WITH N/A
        for file in RD05200200Data:
            file.replace('', np.nan, inplace=True)
        for file in RDB4200801Data:
            file.replace('', np.nan, inplace=True)



    def ReadCsbFiles(self):
        self.readingYear = self.readingYearStored

        while True:
            try:
                vt1Directory = (fr'\\192.168.2.19\quality control\{str(self.readingYear)}')
                
                for d in os.listdir(vt1Directory):
                    if "supplier" in d.lower():
                        vt1Directory = os.path.join(vt1Directory, d)
                        for d in os.listdir(vt1Directory):
                            if "inspection standard" in d.lower():
                                vt1Directory = os.path.join(vt1Directory, d)
                                for d in os.listdir(vt1Directory):
                                    if "receiving inspection record" in d.lower():
                                        vt1Directory = os.path.join(vt1Directory, d)

                                        #GETTING CSB6400802 FILES
                                        try:
                                            for d in os.listdir(vt1Directory):
                                                if "cronics" in d.lower():
                                                    directory = os.path.join(vt1Directory, d)

                                                    #Finding A Folder That Contains New Trend
                                                    for d in os.listdir(directory):
                                                        if 'new trend' in d.lower():
                                                            directory = os.path.join(directory, d)
                                                            print(f"Updated vt1Directory: {directory}")
                                                            break

                                                    os.chdir(directory)

                                                    files = glob.glob('*CSB6400802*.xlsm')

                                                    for f in files:
                                                        print(f'File Readed {f}')
                                                        workbook = CalamineWorkbook.from_path(f)

                                                        csbData = workbook.get_sheet_by_name("format").to_python(skip_empty_area=True)
                                                        csbData = pd.DataFrame(csbData)
                                                        csbData = csbData.replace(r'\s+', '', regex=True)
                                                        
                                                        print(f"CSB FINDED IN {self.readingYear} NEW TREND")
                                                        CSB6400802Data.append(csbData)
                                        except:
                                            print("NO DATA FOUND IN CRONICS")

            except:
                pass

            if self.readingYear > 2021:
                self.readingYear -= 1
            else:
                # self.fileFinishedReading = True
                break

        #REPLACING BLANK VALUES WITH N/A
        for file in CSB6400802Data:
            file.replace('', np.nan, inplace=True)

    def ReadHPIQAQCFiles(self):
        self.readingYear = self.readingYearStored

        while True:
            try:
                vt1Directory = (fr'\\192.168.2.19\quality control\{str(self.readingYear)}')

                for d in os.listdir(vt1Directory):
                    if "supplier" in d.lower():
                        vt1Directory = os.path.join(vt1Directory, d)
                        for d in os.listdir(vt1Directory):
                            if "monitoring" in d.lower():
                                vt1Directory = os.path.join(vt1Directory, d)

                os.chdir(vt1Directory)

                xlsxFiles = glob.glob('HPI*.xlsx')
                xlsFiles = glob.glob('HPI*.xls')

                files = []

                # files = xlsxFiles + xlsFiles
                for file in xlsxFiles:
                    files.append(file)
                for file in xlsFiles:
                    files.append(file)

                #Checking Each Files In Files;
                for f in files:
                    if 'HPI-QA'.lower() in f.lower() or "HPI-QC".lower() in f.lower():
                        
                        workbook = CalamineWorkbook.from_path(f)

                        #Reading Possible Sheets
                        try:
                            qaQcData = workbook.get_sheet_by_name("HPI-QC01-01").to_python(skip_empty_area=True)
                            qaQcData = pd.DataFrame(qaQcData[1:], columns=qaQcData[2])
                        except:
                            qaQcData = workbook.get_sheet_by_name("SUMMARY").to_python(skip_empty_area=True)
                            qaQcData = pd.DataFrame(qaQcData[1:], columns=qaQcData[0])

                        HPIQAQCData.append(qaQcData)

                        
                    
            except:
                pass

            if self.readingYear > 2021:
                self.readingYear -= 1
            else:
                # self.fileFinishedReading = True
                break

    def ReadAllFiles(self):
        self.ReadEm2pFiles()
        self.ReadEm3pFiles()
        self.ReadFmFiles()
        self.ReadDfbSnapFiles()
        self.ReadDfbFiles()
        self.ReadTensile()
        self.ReadRdbCheckSheetFiles()
        self.ReadRdbFiles()
        self.ReadCsbFiles()

        pass

#%%
# filesreader = filesReader()
# filesreader.readingYearStored = 2025
# filesreader.ReadEm2pFiles()

# EM0580106PData

# print(len(EM0580106PData))
# print(len(EM0660046PData))
# print(len(EM0660044PData))

# %%
# filesreader = filesReader()
# filesreader.readingYearStored = 2025
# filesreader.ReadEm3pFiles()

# print(len(EM0580107PData))
# print(len(EM0660047PData))
# print(len(EM0660045PData))

#%%
# filesreader = filesReader()
# filesreader.readingYearStored = 2025
# filesreader.ReadFmFiles()

# print(len(FM05000102Data))
# %%
# filesreader = filesReader()
# filesreader.readingYearStored = 2025
# filesreader.ReadCsbFiles()

# print(len(CSB6400802Data))
#%%
# filesreader = filesReader()
# filesreader.readingYearStored = 2025
# filesreader.ReadDfbSnapFiles()
# filesreader.ReadDfbFiles()

# print(len(DFBSNAPData))
# print(len(DF06600600Data))


# %%
# filesreader = filesReader()
# filesreader.readingYearStored = 2025
# filesreader.ReadTensile()

# print(len(TENSILEData))


# %%
# filesreader = filesReader()
# filesreader.readingYearStored = 2025
# filesreader.ReadRdbCheckSheetFiles()
# filesreader.ReadRdbFiles()


#%%
# filesreader = filesReader()
# filesreader.readingYearStored = 2025
# filesreader.ReadHPIQAQCFiles()
# HPIQAQCData
# %%
