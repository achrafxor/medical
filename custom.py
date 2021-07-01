
#from ansible.module_utils.basic import *

import difflib
import sys
import re

def checkdiffInValues(d1,d2):
  print("function")
  obj1={}
  obj2={}
  indexed=False
  
  #obj[x.split()[0]]= x.split()[1] 
  difference={"file1":[],"file2":[]}
  for key1,value1 in d1.items():
    for key2,value2 in d2.items():
      if(key1==key2 and value1 != value2 and indexed==False):
       obj1[key1]=value1
       obj2[key2]=value2
       difference['file1'].append(obj1)
       difference['file2'].append(obj2)
       obj1={}
       obj2={}
     
  for item in difference['file1']: 
     print(item)
  
  print(difference)     

       





def checkDifferenceInKeys(d1,d2):
    difference={"file1":[],"file2":[]}
    exist=False
    print ("function")
    print (difference)
    #difference["file1"].append("x")

    #loop and difference that exist in file1 and dosent exist in file2
    for key in d1:
     for key2 in d2:
      if (key==key2):
       exist=True 
     if (exist==False):
       difference['file1'].append(key)
     exist=False
   #end loop 

  #loop and differencr that exist in file2 and dosent exist in file1
    for key2 in d2:
     for key in d1:
      if (key2==key):
       exist=True 
     if (exist==False):
       difference['file2'].append(key2)
     exist=False
#end loop

    print(difference)
    print("exist only in file1")
    print("----------------------------------------------------------")
    for value in difference["file1"]:
        print (value)
    
    print("----------------------------------------------------------")

    print("exist only in file2")
    print("----------------------------------------------------------")
    for value in difference["file2"]:
        print (value)
      
    print("----------------------------------------------------------")
          
 
    



def main():
    #regex x=re.search("^x.*:$",text)
 obj= {}
 file1dict={}
 file2dict={}
 file1Plus = []
 file2Plus = []
 existingOnlyInFile1=[]
 existingOnlyInFile2=[]
 file_1 = sys.argv[1]
 file_2 = sys.argv[2]
 #module = AnsibleModule(
 #   argument_spec=dict(
 #      file1 = dict(required=True, type='str'),
 #      file2 = dict(required=True, type='str'),
 #   )
 #)
 with open(file_1) as f1:
  f1_reader=f1.readlines()
 with open(file_2) as f2:
  f2_reader=f2.readlines()
  
 for x in f1_reader:
  obj[x.split()[0]]= x.split()[1] 
  file1dict.update(obj)
 obj={}
 
 for x in f2_reader:
  obj[x.split()[0]]= x.split()[1] 
  file2dict.update(obj)

 
 #checkDifferenceInKeys(file1dict,file2dict)
 checkdiffInValues(file1dict,file2dict)

if __name__== '__main__':
 main()
  
