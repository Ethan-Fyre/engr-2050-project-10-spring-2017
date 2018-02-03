# ENGR2050__jasayles.py
# Ethan Sayles
# April 13, 2017
import numpy as np
import sys

#Class to read or write data from files
class ReadWrite:
    def __init__(self, readfile, writefile):         #The file names of the file being read from and to.
        self.readfile = readfile
        self.writefile = writefile
        self.x,  self.y = [],  []
    def read(self):
        file = open(self.readfile, 'r+')             #Function to read data from a file.
        for line in file:
            pari = line.split("\t")
            self.x.append(float(pari[0]))
            self.y.append(float(pari[1]))
        file.close()
    def write(self):                                        #Function to write data to a file
        func = lambda y: (y**2 - y**(.5))
        func2 = lambda x: (np.e ** (-x) * np.cos(np.pi * x))
        self.read()
        new_x = [func2(i) for i in self.x]
        new_y = [func(i) for i in self.y]
        file = open(self.writefile,  "w+")
        for i in range(len(new_y)):
            file.write("%4.1f\t%6.4f\t%6.4f\n" %(self.x[i],  new_x[i], new_y[i]))
            print(("%4.1f\t%6.4f\t%6.4f\n" %(self.x[i],  new_x[i], new_y[i])))
        file.close()

#Conditional to check for test cases
if __name__ == '__main__':
    if len(sys.argv) == 1:
        infile = "ENGR2050_qz2-2_1.dat"
        outfile = "ENGR2050_qz2_jasayles.dat"
    else:
        infile = sys.argv[1]
        outfile = sys.argv[1]
    changer = ReadWrite(infile, outfile)
    changer.write()
    

        
    

    
