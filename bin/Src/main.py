#importing
import pandas as pd 
import yaml
import tkinter as tk
from tkinter import *
from tkinter import ttk
import matplotlib as plt
#TODO:add OS
#SettingsFile=open("settings.yml",'r')
ProjectFile=open("project.yml",'r')
#Functions
def makeDataframe():
     print("Making a dataframe")
     file={'col1':[1,2],'colo2:':[3,4]}
     Dataframe=pd.DataFrame(data=file)
     print(Dataframe)
#app initilization
root = tk.Tk()
root.title("Data Viewer")
tabControl = ttk.Notebook(root)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)
tabControl.add(tab1, text='settings')
tabControl.add(tab2, text='app')
tabControl.add(tab3, text='info')
tabControl.pack(expand=1, fill="both")
#ttk.Label(tab1, text=yaml.safe_load(SettingsFile)).grid(column=0, row=0, padx=30, pady=30)
#ttk.Label(tab3, text=yaml.safe_load(ProjectFile)).grid(column=0, row=0, padx=30, pady=30)
ttk.Label(tab2,text="filename")
#.grid(column=0, row=0, padx=30, pady=30)
ttk.Entry(tab2).grid(column=0,row=0,padx=30,pady=30)

ttk.Button(tab2, text="Submit").grid(column=0,row=0,padx=30,pady=30)
#TODO:@SmurfyDurfy start writing docs for a help page..
root.mainloop() 

# app
#makeDataframe()
#app run



root.mainloop()



