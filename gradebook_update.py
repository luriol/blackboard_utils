# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 09:32:01 2022

@author: lluri
"""

import os
import sys
import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'
prfx = 'C:\\Users\\lluri\\'
prfx = 'C:\\Users\\TH0LXL1\\'
gdir = 'OneDrive - Northern Illinois University\\NIU\\Classes\\PHYS 273\\PHYS 273 Fall 2022\\Grades\\'
dd = prfx+gdir 
fname = 'grades_9_9_2022.txt'
frame1  = pd.read_csv(dd+fname,encoding='utf-16',sep='\t')
list(frame1)
fname2 = 'ts_data.csv'
frame2  = pd.read_csv(dd+fname2,encoding='utf-8',sep=',')
list(frame2)
idlist1 = frame1['Student ID']
idlist2 = frame2['ID_Number']
test2 = frame2['Test_1']
ec = 'Exam 1 [Total Pts: 150 Score] |2730988'
for tid,tval in zip(idlist2,test2):
    w = tid == idlist1 
    frame1[ec][w] = tval 
frame1.to_csv(dd+'modified_file.csv')

#difflib.get_close_matches(word, possibilities, n=3, cutoff=0.6)