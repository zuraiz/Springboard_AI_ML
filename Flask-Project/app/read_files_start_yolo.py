#!/usr/bin/env python
# coding: utf-8

import ntpath
import plot_from_txt
import os
import sys

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

import yolo_write_files
import pandas as pd


def get_list_of_files(dir_name):
    # create a list of files and sub directories
    # names in the given directory
    list_of_file = os.listdir(dir_name)
    all_files = list()
    list_of_file.sort()
    # iterate over all the entries
    for entry in list_of_file:
        # create full path
        full_path = os.path.join(dir_name, entry)
        # If entry is a directory then get the list of files in this directory
        if os.path.isdir(full_path):
            all_files = all_files + get_list_of_files(full_path)
        else:
            all_files.append(full_path)
    return all_files


def trigger_yolo(dir_name='project_files/small_video_set_1'):
    file_list = get_list_of_files(dir_name)
    yolo_write_files.start_detection(file_list, ntpath.basename(dir_name))
    file_path = plot_from_txt.get_image(dir_name)
    return file_path
