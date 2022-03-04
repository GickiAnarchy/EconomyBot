imgs = []
c = 0

def disImage(pic):
    image = Image.open(pic)
    resize_image = image.resize((300, 525) , Image.ANTIALIAS)
    img = ImageTk.PhotoImage(resize_image)
    imgs.append(img)
    return img

        
hl = HighLow()
window = tk.Tk()

paths = ["cardsPNG/spades_ace.png", "cardsPNG/hearts_ace.png", "cardsPNG/diamonds_ace.png", "cardsPNG/clubs_ace.png"]


for i in range(2):
    for j in range(2):
        frame = tk.Frame(master=window, relief=tk.RAISED, borderwidth=5)
        frame.grid(row=i, column=j)
        tk.Label(master = frame, image = disImage(paths[c])).pack()
        c += 1


window.mainloop()

