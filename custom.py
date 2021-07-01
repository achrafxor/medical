
from ansible.module_utils.basic import *
import difflib
import sys
import re

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def checkdiffInValues(d1,d2):
  print(bcolors.WARNING + "some values are different between two files" + bcolors.ENDC)

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
    # print(bcolors.FAIL)
     print(item)
    # print(bcolors.ENDC)
  
  print(difference)     

       





def checkDifferenceInKeys(d1,d2):
    difference={"file1":[],"file2":[]}
    exist=False
    print(bcolors.WARNING + "some variables are missing between two files" + bcolors.ENDC)
    
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

    #print(bcolors.FAIL)
    print("exist only in file1")
    print("----------------------------------------------------------")
    for value in difference["file1"]:
        print ("+ "+ value)
    
    print("----------------------------------------------------------")

    print("exist only in file2")
    print("----------------------------------------------------------")
    for value in difference["file2"]:
        print ("+ "+ value)
      
    print("----------------------------------------------------------")
          
    #print(bcolors.ENDC)
 
    



def main():
    
    #regex x=re.search("^x.*:$",text)
 module = AnsibleModule( 
    argument_spec=dict( 
        file1 =dict(required=True, type='str'),
        file2 =dict(required=True, type='str'),

    ) 
 )
 file1= module.params.get('file1')
 file2= module.params.get('file2')
 obj= {}
 file1dict={}
 file2dict={}
 file1Plus = []
 file2Plus = []
 existingOnlyInFile1=[]
 existingOnlyInFile2=[]
 #file_1 = sys.argv[1]
 #file_2 = sys.argv[2]
 #module = AnsibleModule(
 #   argument_spec=dict(
 #      file1 = dict(required=True, type='str'),
 #      file2 = dict(required=True, type='str'),
 #   )
 #)
 with open(file1) as f1:
  f1_reader=f1.readlines()
 with open(file2) as f2:
  f2_reader=f2.readlines()
  
 for x in f1_reader:
  obj[x.split()[0]]= x.split()[1] 
  file1dict.update(obj)
 obj={}
 
 for x in f2_reader:
  obj[x.split()[0]]= x.split()[1] 
  file2dict.update(obj)

 
 checkDifferenceInKeys(file1dict,file2dict)
 checkdiffInValues(file1dict,file2dict)

if __name__== '__main__':
 main()
  
