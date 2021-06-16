#importing
from typing import Text
import pandas as pd 
import yaml
import tkinter as tk
from tkinter import *
from tkinter import ttk
SettingsFile=open("settings.yaml",'r')
ProjectFile=open("project.yml",'r')
with open("settings.yaml", 'r') as stream:
    try:
        print(yaml.safe_load(stream))

    except yaml.YAMLError as exc:
        print(exc)
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
tab3 = tkk.Frame(tabControl)
tabControl.add(tab1, text='settings')
tabControl.add(tab2, text='app')
tabControl.add(tab3, text='info')
tabControl.pack(expand=1, fill="both")
ttk.Label(tab1, text=yaml.load(SettingsFile)).grid(column=0, row=0, padx=30, pady=30)
ttk.Label(tab3, text=yaml.load(ProjectFile)).grid(column=0, row=0, padx=30, pady=30)
ttk.Label(tab2, text="Lets dive into the world of computers").grid(column=0, row=0, padx=30, pady=30)
root.mainloop() 

# app
makeDataframe()
#app run







