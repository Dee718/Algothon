#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 01:57:49 2019

@author: dee
"""


import quandl
import pandas as pd
import pyodbc
import os
import requests
import json
import numpy as np
from pathlib import Path


company_data_pd = pd.read_excel('company_country_list.xls') 

metric_table = np.loadtxt('metric_table.csv',delimiter = ',')
country_metric_table = np.load('metric_countries_table.npy')
def score(isin):
    company_idx = np.where(company_data_pd['isin'] == isin)[0]
    if company_idx.size == 0:
        return 0.
    ticker, name,country = company_data_pd.iloc[company_idx[0],[2,4,5]]
    idx = np.where(np.array(country_metric_table,dtype=object) == country)[0]
    if idx.size > 0:
        score = metric_table[idx, -1]
        return score
    else:
        return 0.

main_score_list = []
main_score_list_names = []
pathlist = Path('Supplier_Data2').glob('**/*.npy')
for path in pathlist:
    parent_dict = np.load(str(path), allow_pickle = True).item()
    if type(parent_dict) != str:
        print ('----',str(path).split('/')[1].split('.')[0],'----')
        score1 = 0.
        score2 = 0.
        for value, key in parent_dict.items():
            score_val = score(value)
            number_children1 = len(key.values())
            for value1, key1 in key.items():
                score_val1 = score(value1)
                score1 += (score_val1*1/number_children1)
                number_children2 = len(key1.values())
                for value2, key2 in key1.items():
                    score_val2 = score(value2)
                    score2 += (score_val2*(1/number_children1)*(1/number_children2))
        
        score_list = [score_val, score1, score2]
        print (score_list)
        print (np.sum(score_list))
        main_score_list.append(np.sum(score_list))
        main_score_list_names.append(str(path).split('/')[1].split('.')[0])


