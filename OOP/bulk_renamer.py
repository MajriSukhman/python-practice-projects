import os
# print(os.__all__)
class FileManager:
    def __init__(self):
        self.allFiles = os.listdir()
    
    @property
    def files(self):
        return self.allFiles
    
    def rename(self):
        extension = input("enter the file extension you want to rename eg. 'png' : ")
        curRenameIndex = 1
        for i in self.allFiles:
            if i.split('.')[-1] == extension:
                # print(f'changing {i} to {curRenameIndex}.{extension}')
                os.rename(i, f"{curRenameIndex}.{extension}")
                curRenameIndex += 1

folder = FileManager()
print(folder.files)
folder.rename()