# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 16:36:38 2023

@author: Dell
"""
import pandas as pd
import yaml

p=pd.read_excel("generic/Book1.xlsx")
with open("generic/topic-overide.yaml","r") as f:
    k=(yaml.safe_load(f))
    t=pd.DataFrame(k)
    print(t.columns)
    f.close()

s=pd.concat((p,t))
with open("generic/topic-overide.yaml","w") as f:
    l=[]
    for i in range(s.shape[0]):
        v=dict(s.iloc[i])
        v['replica']=int(v['replica'])
        v['partition']=int(v['replica'])
        if v not in l : l.append(v)
    yaml.dump(l,f)

#l=[dict(s.iloc[i]) for i in range(s.shape[0])]