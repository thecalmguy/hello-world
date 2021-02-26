#!/usr/bin/env python
# coding: utf-8


#Install pandas and change the directory location to loction of att48_d.xls
import pandas as pd
text=pd.read_excel("C:\\Users\\Acer\\Downloads\\att48_d.xls",header=None)


min_dis=100000
for idx in range(48):
    count=0
    min1=[]
    rstart=idx
    listob=[rstart]
    text['copy']=text[rstart].sort_values(ignore_index=True)
    min1=min1+[text['copy'].loc[1]]
    index=text[text[rstart]==min1[0]].index[0]
    listob=listob+[index]
    for count in range(46):
        text['copy']=text[listob[count+1]].sort_values(ignore_index=True)
        arr=text[listob[count+1]].to_numpy()
        sv=[]
        for i in range(len(listob)):
            sv=sv+[arr[listob[i]]]
        text['TorF']=text['copy'].isin(sv)
        min_ind=text[text['TorF']==False].index.tolist()
        min1=min1+[text['copy'].loc[min_ind[0]]]
        index=text[text[listob[count+1]]==min1[count+1]].index[0]
        listob=listob+[index]
        count=count+1
    if sum(min1)<min_dis:
        min_dis=sum(min1)
print("Minimum distance=",min_dis)






