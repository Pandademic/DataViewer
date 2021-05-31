# importing
#import numpy as np
#import pandas as pd
# FIXME:ERR:#8,#9
from appJar import gui
import statistics
import random
import os
import sys
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
