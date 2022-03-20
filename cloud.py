import dropbox
import os
src = input('enter source file : ')
dest = input('enter destination file: ')

class TransferData:
    def __init__(self, accessToken):
        self.accessToken = accessToken
    def upload(self, src, dest):
        dbx = dropbox.Dropbox(self.accessToken)
        #r=read b=binary
        files = os.listdir(src)
        for i in files:
            print(i)
            with open(src+'/'+i,'rb') as file:
                dbx.files_upload(file.read(),dest)
                
        
new = TransferData('sl.BD-Olib_VyKb6_0dgZr3aPzxvlDc3jB1qkX0GUXyJ2xqAuqROzUxvYUSaqto2En48D8JTBphRgrDAgmHZg5Vz4L73YROmF2HH9B8y2ewU665Thau1Briur6Yx8-ZEke51dtsfyE')
new.upload(src, dest)
print('data has been transferred')