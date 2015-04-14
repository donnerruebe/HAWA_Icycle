import os


    
def listFiles(dir="/static/js/",ext=[".js"],name=""):
    root = "."+dir
    pattern = name
    ext_filter = ext  
    path=os.path.join(root,"")
    res=list()
    for r,d,f in os.walk(path):
        for file in f:
            if file[-3:] in ext_filter and pattern in file:
                #print (os.path.join(dir,file))
                res.append(os.path.join(dir,file))
    return res