
from ansible.module_utils.basic import *

import difflib
import sys
import re
def checkDifferenceInKeys(d2):
    difference={{"file1":[]},{"file2":[]}}
    print ("function")
    print (d2)
    
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
 print(file_1) 
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

 
 print ("file1",file1dict)
 print ("file2",file2dict)
 
checkDifferenceInKeys(d2)

if __name__== '__main__':
 main()
  
