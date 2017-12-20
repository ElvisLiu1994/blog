import sys  
import os
def tab2spacefuc(inputfile,tabsize):  
    try:  
       fp = open(inputfile,"r+")  
    except Exception,info:  
        print info  
    inStr = '\t'  
    outStr = tabsize*' '  
    lines = fp.readlines()
    for i in range(len(lines)):  
        lines[i] = lines[i].replace(inStr,outStr) 
    fp.seek(0,0)  
    fp.writelines(lines)
    fp.close()  

if __name__ =="__main__":  
    for x in os.listdir("."):
        if os.path.isfile(x) and os.path.splitext(x)[1]=='.md':
            tab2spacefuc(x,4);
