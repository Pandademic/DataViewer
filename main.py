#importing
#import statistics
#import random
#import os
#import sys
from typing import Text
import pandas as pd 
#import numpy as np
from appJar import gui
#import matplotlib as plt
#Hashed as they are unused
import yaml
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
app = gui("Data Viewer","600x600")
# app
makeDataframe()
#app run
app.go()









#TODO:fix app icon

# TODO: document all new dependencies
# app settings
app = gui("Data Viewer", "600x600")
# app
app.addDirectoryEntry("load a file")
filename = app.getEntry("file")
file = open(str(filename), "w")

# functions

# app run
app.go()


# TODO:fix app icon
