import os
# import __root__
def delete(path,type_of_files):
    l=[]

    for dirpath, dirnames, files in os.walk(path, topdown=False):
        for i in files:

            if i.split('.')[-1]==type_of_files:

                l.append(dirpath+'/'+i)

    count=0
    for i in l:
        count+=1
        os.remove(i)
    print(count,' number of ',type_of_files,' cleaned')
def empty_folder(path):
    paths=[]
    for path,dirname,files in os.walk(path,topdown=True):

        if len(files)==0:
            paths.append(path)
    count=0
    for folders in paths:
        count+=1
        os.removedirs(folders)
    print(count,' empty folders cleaned')

path=input('give the folder abs path')
type_of_files=input('type of files u wish to delete')
x=input('like to clean empty folders from above path (y/n)')
y=input('like to delete '+type_of_files+' from above path (y/n')
if x=='y':
    empty_folder(path)
if y=='y':
    delete(path,type_of_files)

print('YOUR PC IS NOW FASTER CHEERS!!!')
