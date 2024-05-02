import os
import fileinput
import yaml
import pandas as pd

def generic_files_rename(tenantid,i):
    dest="folder/sachi-"+ i +".yaml"
    newname="folder/"+ tenantid + "-"+i +".yaml"
    try:
        os.rename(dest,newname) # changing file name
        file = fileinput.FileInput(newname,inplace=True) # 
        for line in file:
            a=line.replace("npa",tenantid)
            print(a,end='')
        fileinput.close()
    except FileNotFoundError:
        print ("files are not present", dest)
    except FileExistsError:
        print ("file already exists there",dest,sep=":")
tenant=input('ENTER THE TENANT ID: ')
for i in ['con','rep','top','rbac']:
    generic_files_rename(tenant,i)

#os.rename("folder","generic")

'''

print(os.listdir(os.getcwd()))

ftype=["top","con","rbac","rep"]

for i in ftype:
    generic_files_rename("ritu",i)

def writer():
    f=open("folder/ritu-con.txt","r")
    a=f.read()
    c=a.replace("sachin","ritu")
    f2=open("folder/ritu-con.txt","w")
    f.close()
    f2.write(c)
    f2.close()

'''