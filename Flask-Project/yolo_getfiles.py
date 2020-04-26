#!/usr/bin/env python
# coding: utf-8

import os
import ntpath

from yolo_printfiles_withsql import startdetection


def getListOfFiles(dirName):
    # create a list of files and sub directories
    # names in the given directory
    listOfFile = os.listdir(dirName)
    allFiles = list()
    listOfFile.sort()
    # iterate over all the entries
    for entry in listOfFile:
        # create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
    return allFiles


def printfilelist(dirName='/media/mynewdrive/data/Retail_AI/3DPeS/small_video_set_1'):
    file_list = getListOfFiles(dirName)
    print("Calling startdetection")
    time = startdetection(file_list,ntpath.basename(dirName))
    return time
