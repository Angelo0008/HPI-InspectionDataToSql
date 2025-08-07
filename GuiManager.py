from Imports import *
import ExecutableManager

root = None
frame1 = None
message = None
compileButton = None
logWindow = None

def showGui():
    global root
    global frame1

    #Fixing Blur
    windll.shcore.SetProcessDpiAwareness(1)

    root = tk.Tk()
    root.title('FC1 Compiler')
    root.geometry('600x650+50+50')
    root.resizable(False, False)

    #Frames
    frame1 = tk.Frame(root)
    frame1.pack()

    # place a label on the root window
    message = tk.Label(frame1, text="Inspection Data To DataBase", font=("Arial", 12, "bold"))
    message.grid(column=0, row=0)

    InstantiateProceedButton()
    InstantiateLogWindow()

    root.mainloop()

def InstantiateProceedButton():
    global frame1

    global compileButton

    # button
    compileButton = tk.Button(frame1, text='PROCEED', font=("Arial", 12), command = ExecutableManager.StartProgram, width=15, height=1)
    compileButton.grid(column=0, row=1, ipadx=5, ipady=5, pady=10)
    compileButton.config(bg="lightgreen", fg="black")

def InstantiateLogWindow():
    global frame1

    global logWindow

    logWindow = st.ScrolledText(frame1, width = 60, height = 8, font = ("Times New Roman", 10))
    logWindow.grid(column = 0, row=2, pady = 10)

    # Making the text read only
    logWindow.configure(state ='disabled')

def InsertInLogWindow(message):
    global logWindow

    logWindow.configure(state ='normal')
    # Inserting Text which is read only
    logWindow.insert(tk.INSERT, f"{message}\n")
    logWindow.configure(state ='disabled')

def ClearLogWindow():
    global logWindows

    logWindow.configure(state='normal')
    logWindow.delete('1.0', tk.END)
    logWindow.configure(state='disabled')

def Loading():
    global compileButton

    compileButton.config(text= "LOADING...")
    compileButton.config(state= "disabled")

def FinishedLoading():
    global compileButton

    compileButton.config(text= "COMPILE")
    compileButton.config(state= "normal")