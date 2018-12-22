#! /usr/bin/env python3

import os

cwd = os.getcwd()

folder_directory = os.listdir(cwd)


for index in folder_directory:
    print (index)