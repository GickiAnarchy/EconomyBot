import os
import tkinter as tk
from PIL import Image, ImageTk
import cards
import deck
import requests
from io import BytesIO


class matchImages():
    def __init__(self):
        self.urls = []
        self.deck = Deck()
        self.img_dictionary = {}
        with open("cards_img_url.txt") as r:
            for line in r:
                self.urls.append(line)


    def setupWindow(self):
        self.window = tk.Tk()
        self.window.geometry("500×700")
        
        self.cardLabel = tk.Label(self.window)
        self.cardLabel.pack(side = tk.TOP)
        
        next_button = tk.Button(self.window, text ="Next", command=self.next)
        next_button.pack(side=tk.BOTTOM, padx=(0, 20), pady=(0, 20))
        
    
    
    def loadImage(self):
        
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        
        self.c1img = ImageTk.PhotoImage(Image.open(self.cd.imagePath()))
        resize_image = c1img.resize((200, 340) , Image.ANTIALIAS)
        img = ImageTk.PhotoImage(resize_image)

        
    def next(self):
        pass





"""
img_urls = []

urls = open("cards_img_url.txt")

img_urls = urls.readlines()

urls.close()

with open("imgurls.py", "w") as w:
    w.writelines(img_urls)
"""