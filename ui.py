import tkinter as tk
from tkinter import Frame, messagebox as msg
from tkinter import scrolledtext
import customtkinter as ctk
from tkinter import filedialog as fdg
import color_utils
import pandas as pd
from identifier import Identifier


class App():

    def __init__(self):
        self.__root = ctk.CTk() # root
        self.__windowWidth = 1366
        self.__windowHeight = 768
        self.__windowGeo = "1366x768" # size of GUI in width x height format
        self.__exportPath = "./" # data export path, default = current file
        self.__frameList = [UserInterface(self), SettingInterface(self)] #create a list of interfaces that will be bind to the root

        self.__rootConfiguration() # configure the root window
    
    def __rootConfiguration(self):
        self.__root.geometry("{}x{}+250+150".format(self.__windowWidth,self.__windowHeight)) # set the size of window, set the position to the center
        self.__root.title("Spam Identifier") # give the gui a title
        self.__root.resizable(0,0) # resizable (0,0) indicate that 0 px from either width or height can be adjust, or simply means the windows cannot be resize
        self.__root.minsize(1024,768) # minimum size of the window, default setting in case of any error that cause the window size drop
        self.__root.protocol("WM_DELETE_WINDOW", self.__closeAppMsg)  # when closing the windows using "X" button on the top right corner, display a warning
        self.__root.iconbitmap("./icon.ico") # set the icon

    # warning message for closing the app
    def __closeAppMsg(self):
        closeMsg = msg.askyesno("Warning", "Any unexported data will be lost, are you sure you want to close the app?")
        if (closeMsg):
            self.__root.destroy()


    # remove the current frame that is displaying, replace with a new frame
    # helper functions
    def __setFrame(self, currentFrame, replacementFrame):

        self.__removeFrame(currentFrame)
        
        replacementFrame.pack(fill="both",expand=1)

    def __removeFrame(self, frame):
        frame.forget()

    # switch from UI frame to setting frame
    def uiToSetting(self):
        self.__setFrame(self.__frameList[0].getFrame(), self.__frameList[1].getFrame())
    # setting to UI
    def settingToUI(self):
        self.__setFrame(self.__frameList[1].getFrame(), self.__frameList[0].getFrame())
        self.__frameList[0].guiResize() # whenever we get out from setting page, we want to reconfigure the UI widget => bad approach, seeking for a better solution after the product is done

    # start the gui
    def runInterface(self):
        self.__frameList[0].getFrame().pack(fill="both", expand=1)
        self.__root.mainloop()


    # resize the window to a specific size
    def setWindowSize(self, resolution):
        sizeArr = resolution.split("x")
        self.__windowWidth = int(sizeArr[0])
        self.__windowHeight = int(sizeArr[1])
        self.__windowGeo = resolution

        self.__root.geometry(resolution)
        # self.__guiPositioning() # redo the position after reset the window size

    # set a new export path
    def setExportPath(self, newPath):
        self.__exportPath = newPath

    # get the size of the windows in String
    def getWindowGeo(self):
        return self.__windowGeo
    # get the width/height of window in decimal
    def getWindowWidth(self):
        return self.__windowWidth
    def getWindowHeight(self):
        return self.__windowHeight

    # get the export directory of the current configuration
    def getExportDirectory(self):
        return self.__exportPath

class UserInterface():

    def __init__(self, root):
        # frame
        self.__root = root
        self.__frame = ctk.CTkFrame()

        # ui widgets
        self.__sentenceInput = scrolledtext.ScrolledText(self.__frame,width=int(self.__root.getWindowWidth()*0.06),height=int(self.__root.getWindowHeight()*0.02), font=("arial", 18, 'normal'))
        
        #self.__sentenceInput = ctk.CTkTextbox(self.__frame, width=int(self.__root.getWindowWidth()) * 0.65, height=int(self.__root.getWindowHeight()) * 0.45, text_font=("arial", 18, 'normal'), fg_color=color_utils.white)
        
        self.__evaluateButton = ctk.CTkButton(self.__frame, text="Evaluate", command=self.__evaluateInput, text_font=("arial", 14, 'bold'), width=200, height=45, fg_color=color_utils.main_color)
        self.__title = ctk.CTkLabel(self.__frame, text="Enter a Message Below to Evaluate the Input", text_font=("Arial", int(self.__root.getWindowHeight()*0.025), "bold"))
        self.__clearButton = ctk.CTkButton(self.__frame, text="Clear", command=self.__clearWarning, text_font=("arial", 14, 'bold'), fg_color=color_utils.main_color, width=200, height=45)
        self.__historyButton = ctk.CTkButton(self.__frame,text="History", command=self.__openHistoryWindow, fg_color=color_utils.nullify_color, text_font=("Arial", 10, "bold"))
        self.__exportButton = ctk.CTkButton(self.__frame,text="Export", command=self.__exportFile, fg_color=color_utils.nullify_color, text_font=("Arial", 10, "bold"))
        self.__settingButton = ctk.CTkButton(self.__frame,text="Setting", command=self.__settingFunction, fg_color=color_utils.nullify_color, text_font=("Arial", 10, "bold"))
        
        # radio buttons for input evaluation model + label
        self.__modeDescription = ctk.CTkLabel(self.__frame, text="Evaluation Mode", text_font=("Arial", 14, "bold"))
        self.__modelVariable = tk.StringVar()
        self.__radioEmailModel = ctk.CTkRadioButton(self.__frame, text="Email", text_font=("arial", 14, 'bold'), variable=self.__modelVariable, value="Email")
        self.__radioTextMsgModel = ctk.CTkRadioButton(self.__frame, text="Text", text_font=("arial", 14, "bold"), variable=self.__modelVariable, value="Text Message")
       

        # history, input will be stored in a pandas data frame to access
        self.__history = pd.DataFrame(columns=["Message", "Result", "Type"])
 
        self.__gridConfigure()

        

        # initialize the identifier after finish setting up the scene
        self.__identifier = Identifier()


    # positioning the gui components
    def __gridConfigure(self):
        self.__frame.grid_rowconfigure(0, minsize=100) # frame.grid_configuration => set a different parameter for each individual grid for each row/column and give each of them a unique design
        self.__frame.grid_columnconfigure(1, weight=2) # weight = similar to flex in html
        self.__frame.grid_rowconfigure(3, minsize=100) # minsize = minimum amount of space will be taken in pixel
        self.__frame.grid_rowconfigure(5, weight=10)

        self.__title.grid_configure(row=0,column=1) # widget.grid_configuration => place the widget at a corresponding row/column
        self.__sentenceInput.grid_configure(row=1,column=1)
        self.__evaluateButton.grid_configure(row=3, column=1)
        self.__clearButton.grid_configure(row=4,column=1)
        
        self.__modeDescription.grid_configure(row=6, column=0)
        self.__radioTextMsgModel.grid_configure(row=7, column=0)
        self.__radioEmailModel.grid_configure(row=8, column=0)
        self.__radioTextMsgModel.select() # select the text message mode by default

        self.__historyButton.grid_configure(row=6,column=2, pady=5)
        self.__exportButton.grid_configure(row=7,column=2, pady=5)
        self.__settingButton.grid_configure(row=8, column=2, pady=5)
   


    # input clear warning
    def __clearWarning(self):
        clearMsg = msg.askyesno("Warning", "Do you want to clear your input?")
        if (clearMsg):
            self.__clearInput()

    # clear the current input
    def __clearInput(self):
        self.__sentenceInput.delete(1.0,tk.END)

    # verify the current input and clear the input once finish
    def __evaluateInput(self):
        evaluateMsg = msg.askyesno("Warning", "You are about to evaluate the input text message. To ensure the evluated result, make sure you check your input")
        # if true, evaluate the message => link to the machine learning algorithm
        if (evaluateMsg):
            inputMsg = self.__sentenceInput.get(1.0, tk.END).strip()
            if (len(inputMsg) == 0):
                msg.showerror("Error", "Cannot evaluate empty input")
            else:
                result = self.__identifier.evaluate(inputMsg, self.__modelVariable.get())
                self.__history.loc[len(self.__history)] = [inputMsg, result, self.__modelVariable.get()]
                msg.showinfo("Success", "Your input result is: {0}".format(result))
            
            #print(self.__sentenceInput.get(1.0,tk.END))
            self.__clearInput()


    # call the function from root, can be replace by directly pointing to root.uiToSetting rather than creating an extra function
    def __settingFunction(self):
        self.__root.uiToSetting()

    
    def guiResize(self):
        # gui widget
        # reposition the widget whenever the window size change

        self.__sentenceInput.configure(width=int(self.__root.getWindowWidth()*0.06),height=int(self.__root.getWindowHeight()*0.02))
        
        #for future update, if custom tkinter implement the textbox widget, we can use it
        #self.__sentenceInput.configure(width=int(self.__root.getWindowWidth()) * 0.65, height=int(self.__root.getWindowHeight()) * 0.45)
        
        self.__title.configure(text_font=("Arial", int(self.__root.getWindowHeight()*0.025), "bold"))

    def __exportFile(self):
        location = "" + self.__root.getExportDirectory() + "/export.csv"
        self.__history.to_csv(location, sep=chr(30), header=True, index=False)
        
        msg.showinfo("Success", "You have successfully export your result")

    def __openHistoryWindow(self):
        HistoryInterface(self.__history)



    def getFrame(self):
        return self.__frame

class HistoryInterface():

    def __init__(self, inputHistory):
        # main level
        self.__topLevel = ctk.CTkToplevel()
        self.__history = inputHistory

        # first frame
        self.__mainFrame = ctk.CTkFrame(self.__topLevel)
        self.__mainFrame.pack(fill="both", expand=1)

        # tkinter canvas
        self.__canvas = ctk.CTkCanvas(self.__mainFrame)
        self.__canvas.pack(side="left", fill="both", expand=1)

        # scroll bar that bind to the first frame
        self.__scrollBar = ctk.CTkScrollbar(self.__mainFrame, orientation="vertical", command=self.__canvas.yview)
        self.__scrollBar.pack(side="right", fill="y")

        # configure the canvas so it link the scroll bar
        self.__canvas.configure(yscrollcommand=self.__scrollBar.set)
        self.__canvas.bind("<Configure>", lambda e: self.__canvas.configure(scrollregion=self.__canvas.bbox("all")))

        # create a second frame
        self.__displayFrame = ctk.CTkFrame(self.__canvas)
        self.__displayFrame.pack(fill="both", expand=1)
        self.__canvas.create_window((0,0), window=self.__displayFrame, anchor="nw")


        # configure the root
        self.__topLevel.configure()

        
        # the title label for the data
        self.__MessageLabel =  ctk.CTkLabel(self.__displayFrame, text="Message", text_font=("Arial", 18, "bold"))
        self.__resultLabel = ctk.CTkLabel(self.__displayFrame, text="Result", text_font=("Arial", 18, "bold"))
        self.__typeLaebl = ctk.CTkLabel(self.__displayFrame, text="Type", text_font=("Arial", 18, "bold"))


        self.__topLevelConfiguration()
        self.__gridConfiguration()
        self.__printHistory()

    def __topLevelConfiguration(self):
        self.__topLevel.title("History")
        self.__topLevel.geometry("768x512+512+200")
        self.__topLevel.grab_set() # only let the user to access the current window
        self.__topLevel.protocol("WM_DELETE_WINDOW", self.__releaseWindow) # when the user close the history windows, it release the grab
        self.__topLevel.iconbitmap("./icon.ico")
        # setting the window to a fix size to prevent resizing
        # issue to be fixed: using resizable will cause the app stop working
        self.__topLevel.maxsize(768,512)
        self.__topLevel.minsize(768,512)

    # release the grab from the current window and close it
    def __releaseWindow(self):
        self.__topLevel.grab_release()
        self.__topLevel.destroy()

    def __gridConfiguration(self):

        self.__displayFrame.grid_columnconfigure(0, weight= 3,minsize=256)
        self.__displayFrame.grid_columnconfigure(1, weight=3, minsize=256)
        self.__displayFrame.grid_columnconfigure(2, weight=3, minsize=256)

        self.__MessageLabel.grid_configure(row=0,column=0)
        self.__resultLabel.grid_configure(row=0, column=1)
        self.__typeLaebl.grid_configure(row=0, column=2)

    # print all the result from the data frame
    def __printHistory(self):
        for i in range(len(self.__history)):
            ctk.CTkLabel(self.__displayFrame, text=self.__history.loc[i]["Message"], wraplength=256, text_font=("Arial", 12, "normal")).grid_configure(row=i+1,column=0, pady=20)
            ctk.CTkLabel(self.__displayFrame, text=self.__history.loc[i]["Result"], text_font=("Arial", 12, "normal")).grid_configure(row=i+1,column=1, pady=20)
            ctk.CTkLabel(self.__displayFrame, text=self.__history.loc[i]["Type"], text_font=("Arial", 12, "normal")).grid_configure(row=i+1, column=2, pady=20)


class SettingInterface():

    def __init__(self, root):
        self.__frame = ctk.CTkFrame()
    
        self.__root = root
        self.__unsaveChange = False
        self.__currentExportDirecotry = self.__root.getExportDirectory()

        ## window size setting
        self.__windowResizeMenu = ctk.CTkOptionMenu(self.__frame, values=["1024x768", "1366x768", "1600x900"], width=300, height=45, text_font=("Arial", 18), dropdown_text_font=("Arial", 18), fg_color=color_utils.main_color, command=self.__unsaveChangeTrigger)
        self.__windowResizeMenu.set(self.__root.getWindowGeo())
        self.__resolutionLabel = ctk.CTkLabel(self.__frame, text="Resolution", text_font=("Arial", 18))
        
        ## export directory setting
        self.__directoryLabel = ctk.CTkLabel(self.__frame, text="Export Directory", text_font=("Arial", 18))
        self.__directoryText = tk.StringVar(self.__frame, value=self.__root.getExportDirectory())
        self.__directory = ctk.CTkEntry(self.__frame, state="disabled", textvariable=self.__directoryText, text_font=("Arial", 18), width=600)
        self.__changeDirectoryButton = ctk.CTkButton(self.__frame, text="Change Directory", text_font=("Arial", 18), command = self.__changeExportDirectory,fg_color=color_utils.main_color)


        ## cancel/apply change
        self.__applyButton = ctk.CTkButton(self.__frame, text="Apply", command=self.__applyChange, text_font=("Arial", 18), height=45, state="disabled", fg_color=color_utils.nullify_color)
        self.__backButton = ctk.CTkButton(self.__frame, text="Back", command=self.__goBack, text_font=("Arial", 18), height=45, fg_color=color_utils.nullify_color)


        self.__gridConfiguration()

    # configurate the grid of the components/widgets
    # same definition as the gridConfiuration function for UIInterface
    def __gridConfiguration(self):

        self.__frame.grid_rowconfigure(0, minsize=100)   # empty row with minsize as spacing
        self.__frame.grid_columnconfigure(0, weight=4) 
        self.__frame.grid_columnconfigure(1, weight=6)
        self.__frame.grid_rowconfigure(1, minsize=100)
        self.__frame.grid_rowconfigure(3, minsize = 300)  



        self.__resolutionLabel.grid_configure(row = 0, column=0)
        self.__windowResizeMenu.grid_configure(row=0, column= 1)
        self.__directoryLabel.grid_configure(row = 1, column = 0)
        self.__directory.grid_configure(row = 1, column = 1)
        self.__changeDirectoryButton.grid_configure(row=2, column=1)
        

        self.__backButton.grid_configure(row = 3, column= 0)
        self.__applyButton.grid_configure(row = 3, column= 1)

    # back to the ui page, if there is unsave change, warn the user
    def __goBack(self):
        exitWarnning = True
        if (self.__unsaveChange):
            exitWarnning = msg.askyesno("Warning", "There is unsaved change, are you sure you want to go back?")
        if (exitWarnning):
                # if the user decided to exit without saving the change, restore the setting and return to the ui page
                self.__noChange()
                self.__root.settingToUI()

    # update the setting
    def __applyChange(self): 
        
        if (self.__applyButton.state == "normal"):
            self.__root.setExportPath(self.__directoryText.get())
            self.__root.setWindowSize(self.__windowResizeMenu.get())
            self.__currentExportDirecotry = self.__root.getExportDirectory()
            self.__directoryText.set(self.__currentExportDirecotry)
            self.__applyButtonReset()

    # call the file dialog and update a new export path if there is one
    def __changeExportDirectory(self):
        newPath = fdg.askdirectory()
        
        if ( not (len(newPath) == 0)):
            self.__directoryText.set(newPath)
            self.__unsaveChangeTrigger()

    # return the setting as before
    def __noChange(self):
        self.__applyButtonReset()
        self.__windowResizeMenu.set(self.__root.getWindowGeo())
        self.__directoryText.set(self.__currentExportDirecotry)

    def __applyButtonReset(self):
        self.__unsaveChange = False
        self.__applyButton.configure(state="disabled", fg_color=color_utils.nullify_color)


    # to link this trigger to the resolution menu command, it ask for multiple arguments even though it didn't get to use, so *arg is placed as place holder
    def __unsaveChangeTrigger(self, *arg):
        self.__unsaveChange = True
        self.__applyButton.configure(state="normal", fg_color=color_utils.main_color)


    def getFrame(self):
        return self.__frame
