import os
import shutil

fromDIR='C:/Users/User/Downloads'
toDIR='C:/Users/User/Downloads/Example'
listofFiles=os.listdir(fromDIR)
#print(listofFiles)

for i in listofFiles:
    name, extention=os.path.splitext(i)
    if extention == "":
        continue
    if extention in ['.txt','.doc','.docx','.pdf']:
        path1=fromDIR+'/'+i
        path2=toDIR+"/"+"Document_Files"
        path3=toDIR+"/"+"Document_Files"+"/"+i
        if os.path.exists(path2):
            print("Moving" + i + '.....')
            
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("Moving" + i + ".....")
            shutil.move(path1, path3)


