import os,sys

def sizeparse(raw):
    return int.from_bytes(raw[::-1])

class iFConFile:
    def __init__(self,path):
        self.f = open(path,'rb')
        if not self.f.read(6) == b'iFFile':
            raise TypeError('This file is not iFCon File')
        indexsize = sizeparse(self.f.read(4))
        self.filenumber = sizeparse(self.f.read(4))
        readcount = 4
        self.index={}
        while readcount<indexsize:
            fileindex = sizeparse(self.f.read(4)) + 10 + indexsize
            filesize = sizeparse(self.f.read(4))
            filenamesize = sizeparse(self.f.read(4))
            filename = self.f.read(filenamesize).decode('utf-8')
            readcount += (12 + filenamesize)
            self.index[filename] = (fileindex,filesize)
    
    def extractAll(self,path):
        if not os.path.exists(path):
            os.makedirs(path)
        for file in self.index.items():
            filepath = os.path.join(path,file[0])
            if not os.path.exists(os.path.dirname(filepath)):
                os.makedirs(os.path.dirname(filepath))
            with open(filepath,'wb') as f:
                self.f.seek(file[1][0])
                print('Extracting: ' + file[0])
                f.write(self.f.read(file[1][1]))


iffile=iFConFile(sys.argv[1])
iffile.extractAll('.')