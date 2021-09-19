import os

names_list=['Michal','Shira','Sara','Yael','Yafa','Tamar','Rut','Elisheva','Rachel','Chagit']
file_name=input("Enter name for this file: ")+'.txt'
#file_path=f'D:\Dell Active Code\project\{file_name}'
file_path=f'D:\Dell Active Code\project\example2.txt'
with open(file_path,"wt") as f:
    for name in names_list:
        f.write(name+'\n')

with open(file_path,'rt') as f:
    while f.readline()!='':
        #delete '\n'
        print(f.readline()[:-1])

#execute example:
    # Shira
    # Yael
    # Tamar
    # Elisheva
    # Chagit

