import numpy as np
import pandas as pd
import os

class DataAnalyse:

    def __init__(self):
        self.dir="D:\jiedq"
        self.files=[]
        self.num = 0
        self.result = "D:\ppd_result"

    def getFiles(self):
        pathDir = os.listdir(self.dir)
        for file in pathDir:
            self.files.append(file)
        print(self.files)

    def change2Txt(self):
        fileNum = self.files.__len__()
        for i in range(0,fileNum):
            filePath = self.dir+"\\"+ self.files.__getitem__(i)
            self.write2Txt(filePath)

    def write2Txt(self,filePath):
        fopen = open(filePath,"rb")
        with open(self.result+"\\number_"+str(self.num)+".txt","wb") as f:
            for eachLine in fopen:
                 if len(eachLine) > 20:
                     f.write(eachLine)
        self.num += 1

    #def plot(self):

    #def analyze(self):

    def run(self):
        self.getFiles()
        self.change2Txt()

if __name__ == '__main__':
    one = DataAnalyse()
    one.run()

