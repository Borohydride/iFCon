import os

def sizeparse(raw: bytes):
    return int.from_bytes(raw, byteorder='little')

def sizepack(num: int):
    return num.to_bytes(4, byteorder='little')

class iFConFile:
    def __init__(self, file, mode = 'rb'):
        self.file = open(file, mode)
        self.mode = mode
        if self.mode == 'rb':
            self.f = open(file, 'rb')
            self.header = self.f.read(6)
            if self.header != b'iFFile':
                raise ValueError('Invalid iFConFile header')
            self.indexsize = sizeparse(self.f.read(4))
            self.index = {}
            self.filenumber = sizeparse(self.f.read(4))
            readcount = 4
            while readcount < self.indexsize:
                fileindex = sizeparse(self.f.read(4))
                filesize = sizeparse(self.f.read(4))
                filenamesize = sizeparse(self.f.read(4))
                filename = self.f.read(filenamesize).decode('utf-8')
                readcount += (12 + filenamesize)
                self.index[filename] = (fileindex,filesize)
        elif self.mode == 'wb':
            self.f = open(file, 'wb')
            self.header = b'iFFile'
            self.f.write(self.header)
            self.indexsize = 4
            self.filenumber = 0
            self.files = {}
            self.index = {}
            self.saved = True
            self.filesize = 0
        else:
            raise ValueError('Invalid mode')


    
    def getindex(self):
        return self.index

    def getfile(self, filename):
        if not self.mode == 'rb':
            raise ValueError('iFConFile must be opened in read binary mode')
        if filename in self.index:
            fileindex,filesize = self.index[filename]
            self.f.seek(fileindex + 6 + 4 + self.indexsize)
            return self.f.read(filesize)
        else:
            return FileNotFoundError(f'{filename} not found in iFConFile')
    
    def extract(self, filename, output):
        if not self.mode == 'rb':
            raise ValueError('iFConFile must be opened in read binary mode')
        if filename in self.index:
            fileindex,filesize = self.index[filename]
            self.f.seek(fileindex + 6 + 4 + self.indexsize)
            with open(output, 'wb') as f:
                f.write(self.f.read(filesize))
        else:
            raise FileNotFoundError(f'{filename} not found in iFConFile')
    
    def extractAll(self, outputdir):
        if not self.mode == 'rb':
            raise ValueError('iFConFile must be opened in read binary mode')
        for filename in self.index:
            fileindex,filesize = self.index[filename]
            self.f.seek(fileindex + 6 + 4 + self.indexsize)
            outputfile = os.path.join(outputdir, filename)
            if not os.path.exists(os.path.dirname(outputfile)):
                os.makedirs(os.path.dirname(outputfile))
            with open(outputfile, 'wb') as f:
                f.write(self.f.read(filesize))

    def _addfile(self, target, data: bytes):
        if not self.mode == 'wb':
            raise ValueError('iFConFile must be opened in write binary mode')
        if target in self.index:
            raise FileExistsError(f'{target} already exists in iFConFile')
        self.saved = False
        self.files[target] = data
        self.index[target] = (self.filesize, len(data))
        self.filesize += len(data)
        self.filenumber += 1
        self.indexsize += 12 + len(target.encode('utf-8'))

    def addfile(self, target, file):
        with open(file, 'rb') as f:
            data = f.read()
        self._addfile(target, data)

    def save(self):
        if not self.mode == 'wb':
            raise ValueError('iFConFile must be opened in write binary mode')
        if not self.saved:
            self.f.seek(6)
            self.f.write(sizepack(self.indexsize))
            self.f.write(sizepack(self.filenumber))
            for file,index in self.index.items():
                self.f.write(sizepack(index[0]))
                self.f.write(sizepack(index[1]))
                self.f.write(sizepack(len(file.encode('utf-8'))))
                self.f.write(file.encode('utf-8'))
            for file,data in self.files.items():
                self.f.write(data)
            self.saved = True

    def close(self):
        self.f.close()
        del self