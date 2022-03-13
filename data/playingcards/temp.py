import os
import tkinter as tk
import PIL
from PIL import Image, ImageTk
from cards import Card
from deck import Deck
import requests
from io import BytesIO


pathHere = os.path.abspath(os.path.dirname(__file__))

class matchImages():
    def __init__(self):
        self.urls = []
        self.deck = Deck()
        self.img_dictionary = {}
        f = f"{pathHere}/cURL.txt"
        with open(f) as r:
            for line in r:
                self.urls.append(line)
        self.setupWindow()
        self.loadImage()


    def setupWindow(self):
        self.window = tk.Tk()
        self.window.geometry("800x640")
        
        self.cardLabel = tk.Label(self.window)
        self.cardLabel.pack(side = tk.TOP)
        
        self.imgname = tk.Entry(fg="red", width=50)
        self.imgname.pack()
                
        self.next_button = tk.Button(self.window, text ="Next", command=self.next)
        self.next_button.pack(side = tk.BOTTOM, padx=(0, 20), pady=(0, 20))

    
    
    def loadImage(self):
        self.tUrl = self.urls.pop()
        response = requests.get(self.tUrl)
        self.img = PIL.Image.open(BytesIO(response.content))
        resizedImg = self.img.resize((250,363), Image.ANTIALIAS)
        self.cimg = ImageTk.PhotoImage(resizedImg)
        self.cardLabel.config(image = self.cimg)
        self.cardLabel.image = self.cimg

        
    def next(self):
        if self.imgname.get() == "" or self.imgname.get() == None:
            self.errorBox()
            return
        self.nametext = self.imgname.get()
        self.img_dictionary[self.nametext] = self.tUrl
        
        if len(self.urls) <= 0:
            names = list(self.img_dictionary.keys())
            sites = list(self.img_dictionary.values())
            leng = len(self.img_dictionary)
            
            with open("imgdict.txt", "w") as ww:
                while True:
                    print(str(x))
                    n = names.pop()
                    s = sites.pop()
                    fstr = f"{n}  __  {s}/n"
                    ww.write(fstr)
                    
                    if len(names) and len(sites) <= 0:
                        return
                    
    
    def errorBox(self):
        msgbox.showinfo("Blank Name", "Must enter a name in the field.")


    def run(self):
        self.window.mainloop()



###############################################################################
m = matchImages()
m.run()





"""
img_urls = []

urls = open("cards_img_url.txt")

img_urls = urls.readlines()

urls.close()

with open("imgurls.py", "w") as w:
    w.writelines(img_urls)
"""