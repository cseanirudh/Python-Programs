# extend

from array import *
stu_roll = array('i',[101,102,103,104,105])
new_stu_roll = array('i',[107,108,109,110])
n = len(stu_roll)
i = 0
while(i<n):
    print(stu_roll[i])
    i += 1

print("Array After Extendd")
stu_roll.extend(new_stu_roll)
n = len(stu_roll)
i = 0
while(i<n):
    print(stu_roll[i])
    i+=1
