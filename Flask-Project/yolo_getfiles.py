#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from scipy.io import loadmat
import numpy as np
import re
import numpy as np
import time
import math
import pandas as pd
import os
import time

import matplotlib.pylab as pylab
import matplotlib.pyplot as plt
from matplotlib.pyplot import imshow
from matplotlib.ticker import MaxNLocator

import pickle

from yolo_printfiles import startdetection


# In[ ]:


def getListOfFiles(dirName):
    # create a list of files and sub directories
    #names in the given directory
    listOfFile = os.listdir(dirName)
    allFiles = list()
    listOfFile.sort()
    #iterate over all the entries
    for entry in listOfFile:
        #create full path
        fullPath = os.path.join(dirName, entry)
        #If entry is a directory then get the list of files in this directory
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
    #yolo_printfiles.printfiles(allFiles)
    return allFiles

def printfilelist(dirName='/media/mynewdrive/data/Retail_AI/3DPeS/small_video_set_1'):
    file_list = getListOfFiles(dirName)
    time = startdetection(file_list)
    return time

printfilelist()

