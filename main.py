#importing
import pandas as pd 
import numpy as np
from appJar import gui
import statistics
import random
import os
import sys
import matplotlib as plt
import yaml
with open("settings.yaml", 'r') as stream:
    try:
        print(yaml.safe_load(stream))
    except yaml.YAMLError as exc:
        print(exc)
#Functions

#app initilization
app = gui("Data Viewer","600x600")
# app
app.addLabel("Enter The data viewer Directory Path:")
app.addDirectoryEntry("file")
filename = app.getEntry("file")
file = open(str(filename), "w")
app.addLabel("Enter the file you want to read:")
app.addFileEntry("f1")

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
