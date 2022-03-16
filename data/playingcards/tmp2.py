import urllib.request
import os
import io
import time
import linecache

pathHere = os.path.abspath(os.path.dirname(__file__))

urls = open("imgurls.py", "r")
urlList = urls.readlines()
pngList = []
iter = 0

for x in urlList:
    iter += 1
    print(f"{str(iter)} -- Good")

urls.close()
lineList = [] 

for x in urlList:
    webUrl = urllib.request.urlopen(x)
    print ("result code: " + str(webUrl.getcode()))
    htmlFile = open("html.txt","wb")
    data = webUrl.read()
    htmlFile.write(data)
    time.sleep(1)
    htmlFile.close()
    htmlRead = open("html.txt", "r")
    lines = htmlRead.readlines()
    line = lines[351]
    lineList.append(line)
    print(line)
    htmlRead.close()
    
with open("final.txt","w") as w:
    w.writelines(lineList)