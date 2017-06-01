class student:
    def __init__(self,name):
        self.name = name
        self.attend = 0
        self.marks = []
        print ("Welcome {} to University of Bridgeport".format(name))
        
    def addattend(self):
        self.attend += 1
    def addmarks(self,ma):
        self.marks.append(ma)
    def getavg(self):
        return  sum(self.marks)/len (self.marks)
        
