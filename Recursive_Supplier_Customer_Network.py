#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 11:36:46 2019

@author: ryanmurphy
"""

import numpy as np
import pandas as pd

#try:
#    pandas_data.keys()
#except NameError:
#    pandas_data = pd.read_csv('Quandl_Data.csv')
#    pandas_keys = pandas_data.keys()
#    data = np.array(pandas_data,dtype=str)
#    NAN = np.where(data[:,9] == 'nan')
#    data = np.delete(data,NAN,axis=0)  
#    NAN = np.where(data[:,4] == 'nan')
#    data = np.delete(data,NAN,axis=0) 


Index = 1#int(sys.argv[1])

data = np.load('Quandl_Data_NP.npy',allow_pickle=True)
pandas_keys = np.load('Keys.npy',allow_pickle=True)

NAN = np.where(data[:,15] == 'nan')
data = np.delete(data,NAN,axis=0) 

data_dic = {}
for i in range(len(pandas_keys)):
    data_dic[pandas_keys[i]] = data[:,i]
    
del data 
FTSE100_Companies = np.loadtxt('nikkei_225.csv',delimiter=',',dtype=object)
a
for a in range(0,2):
    
    COMPANY_NAME = FTSE100_Companies[a,0]
    COMPANY_TICKER = FTSE100_Companies[a,1]
    
    print(COMPANY_NAME)
    
    if len(np.where(data_dic['customer_isin'].astype(str) == COMPANY_TICKER)[0]) != 0:
        Customer_Names = np.unique(data_dic['customer_name'][np.where(data_dic['supplier_isin'].astype(str) == COMPANY_TICKER)].astype(str))
        customer_isin = np.unique(data_dic['customer_isin'][np.where(data_dic['supplier_isin'].astype(str) == COMPANY_TICKER)].astype(str))
        
        Supplier_Names = np.unique(data_dic['supplier_name'][np.where(data_dic['customer_isin'].astype(str) == COMPANY_TICKER)].astype(str))
        supplier_isin = np.unique(data_dic['supplier_isin'][np.where(data_dic['customer_isin'].astype(str) == COMPANY_TICKER)].astype(str))
        
        Supplier_Dict = {}  
        Revenue_Dict = {}
        dict_i = {}
        for i in range(len(supplier_isin)):
            print('i: ',i, ' / ', len(supplier_isin))
    
            supplier_isin_i = supplier_isin[i]
            Supplier_Names_i = np.unique(data_dic['supplier_name'][np.where(data_dic['customer_isin'].astype(str) == supplier_isin_i)].astype(str))
            supplier_isins_i = np.unique(data_dic['supplier_isin'][np.where(data_dic['customer_isin'].astype(str) == supplier_isin_i)].astype(str))
    
            print('j: ', len(supplier_isins_i))
            
            dict_j = {}
            for j in range(len(supplier_isins_i)):
                
                
                supplier_isin_j = supplier_isins_i[j]
                
                Supplier_Names_j = np.unique(data_dic['supplier_name'][np.where(data_dic['customer_isin'].astype(str) == supplier_isin_j)].astype(str))
                supplier_isins_j =  np.unique(data_dic['supplier_isin'][np.where(data_dic['customer_isin'].astype(str) == supplier_isin_j)].astype(str))
        
                if len(supplier_isins_j) == 0:
                    dict_j[supplier_isin_j] = {}
                else:
                    dict_j[supplier_isin_j] = supplier_isins_j
    
            dict_i[supplier_isin_i] = dict_j
        Supplier_Dict[COMPANY_TICKER] = dict_i  
    
        np.save('Supplier_Data2/'+COMPANY_NAME+'_Data.npy',Supplier_Dict)   
    else:
        np.save('Supplier_Data2/'+COMPANY_NAME+'_Data.npy',np.array([COMPANY_TICKER]))
        
for a in range(100):
    
    COMPANY_NAME = FTSE100_Companies[a,0]
    COMPANY_TICKER = FTSE100_Companies[a,1]
    
    print(COMPANY_NAME)
    
    if len(np.where(data_dic['supplier_isin'].astype(str) == COMPANY_TICKER)[0]) != 0:
        Customer_Names = np.unique(data_dic['customer_name'][np.where(data_dic['supplier_isin'].astype(str) == COMPANY_TICKER)].astype(str))
        customer_isin = np.unique(data_dic['customer_isin'][np.where(data_dic['supplier_isin'].astype(str) == COMPANY_TICKER)].astype(str))
        
        Supplier_Names = np.unique(data_dic['supplier_name'][np.where(data_dic['customer_isin'].astype(str) == COMPANY_TICKER)].astype(str))
        supplier_isin = np.unique(data_dic['supplier_isin'][np.where(data_dic['customer_isin'].astype(str) == COMPANY_TICKER)].astype(str))
        
        Supplier_Dict = {}  
        Revenue_Dict = {}
        dict_i = {}
        dict_i_r = {}
        for i in range(len(customer_isin)):
            print('i: ',i, ' / ', len(customer_isin))
            
#            supplier_isin_i = supplier_isin[i]
#            Supplier_Names_i = np.unique(data_dic['supplier_name'][np.where(data_dic['customer_isin'].astype(str) == supplier_isin_i)].astype(str))
#            supplier_isins_i = np.unique(data_dic['supplier_isin'][np.where(data_dic['customer_isin'].astype(str) == supplier_isin_i)].astype(str))
##    
            customer_isin_i = customer_isin[i]
            Customer_Names_i = np.unique(data_dic['customer_name'][np.where(data_dic['supplier_isin'].astype(str) == customer_isin_i)].astype(str))
            customer_isins_i = np.unique(data_dic['customer_isin'][np.where(data_dic['supplier_isin'].astype(str) == customer_isin_i)].astype(str))
            
            customer_rev_i = np.unique(data_dic['revenue_dependency'][np.where(data_dic['supplier_isin'].astype(str) == customer_isin_i)].astype(str))
    
            print('j: ', len(customer_isins_i))
            
            dict_j = {}
            dict_j_r = {}
            for j in range(len(customer_isins_i)):
                
#                supplier_isin_j = supplier_isins_i[j]
#                Supplier_Names_j = np.unique(data_dic['supplier_name'][np.where(data_dic['customer_isin'].astype(str) == supplier_isin_j)].astype(str))
#                supplier_isins_j =  np.unique(data_dic['supplier_isin'][np.where(data_dic['customer_isin'].astype(str) == supplier_isin_j)].astype(str))
#        
                customer_isin_j = customer_isins_i[j]
                Customer_Names_j = np.unique(data_dic['customer_name'][np.where(data_dic['supplier_isin'].astype(str) == customer_isin_j)].astype(str))
                customer_isins_j =  np.unique(data_dic['customer_isin'][np.where(data_dic['supplier_isin'].astype(str) == customer_isin_j)].astype(str))
                
                customer_rev_j =  np.unique(data_dic['revenue_dependency'][np.where(data_dic['supplier_isin'].astype(str) == customer_isin_j)].astype(str))
        
                if len(customer_isins_j) == 0:
                    dict_j[customer_isin_j] = {}
                    if len(customer_rev_j) == 0:
                        pass
                    else:
                        dict_j_r[customer_rev_j] = {}
                else:
                    dict_j[customer_isin_j] = customer_isins_j
                    dict_j_r[customer_rev_i[j]] = customer_rev_j
            
            dict_i[customer_isin_i] = dict_j
            if len(customer_rev_i) == 0:
                pass
            else:
                dict_i_r[customer_rev_i[j]] = dict_j_r
        Supplier_Dict[COMPANY_TICKER] = dict_i 
        Revenue_Dict[COMPANY_TICKER] = dict_i_r
    
        np.save('Customer_Data2/'+COMPANY_NAME+'_Data.npy',Supplier_Dict)   
        np.save('Customer_Data2/'+COMPANY_NAME+'_Data_Rev.npy',Revenue_Dict) 
    else:
        np.save('Customer_Data2/'+COMPANY_NAME+'_Data.npy',np.array([COMPANY_TICKER]))
        np.save('Customer_Data2/'+COMPANY_NAME+'_Data_Rev.npy',np.array([COMPANY_TICKER]))
