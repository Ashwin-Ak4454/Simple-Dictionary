import json
from difflib import get_close_matches
from tkinter import * 
from tkinter import messagebox

data = json.load(open("data.json"))

def dict():
    word = searchword.get()
    lcw = word.lower()
    lcyn = ""
    display.delete(1.0, END)
    if lcw in data:
        meaning = data[lcw]
        for item in meaning:
            display.insert(END, u'\u2022 ' + item + '\n')
    elif lcw.title() in data:
        meaning =  data[lcw.title()]
        for item in meaning:
            display.insert(END, u'\u2022' + item + '\n\n')
    elif lcw.upper() in data:
        meaning =  data[lcw.upper()]
        for item in meaning:
            display.insert(END, u'\u2022' + item + '\n\n')
    elif len(get_close_matches(lcw,data.keys(),cutoff=0.8))>0:
        close_match = get_close_matches(lcw,data.keys(),cutoff=0.8)[0]
        yn = messagebox.askyesno("Confirm", "Did you mean " + close_match + " instead?")
        if yn == True:
            searchword.delete(0, END)
            searchword.insert(END, close_match)
            meaning =  data[get_close_matches(lcw,data.keys(),cutoff=0.8)[0]]
            for item in meaning:
                display.insert(END, u'\u2022' + item + '\n\n')

root =Tk()

root.geometry("770x600+300+50")
root.title("Simple Dictionary By Ashwin Kumar")
root.configure(background="antiquewhite")
root.resizable(0,0)

title = Label(root, text = "SIMPLE DICTIONARY",font = ("Gabriola", 28, "bold"), fg = "red", bg = "antiquewhite")
title.place(x = 255, y = 0)

entrylabel = Label(root, text = "Your Word To Find The Meaning?",font = ("Gabriola", 25, "bold"), fg = "Brown", bg = "antiquewhite")
entrylabel.place(x = 200, y = 50)

searchword = Entry(root, font = ('Gabriola', 20), justify = CENTER, bd = 8, relief = RIDGE)
searchword.place(x = 270, y= 115)

searchbutton = Button(root, text = "Search", font = ("Gabriola", 25, "bold"), fg = "Brown", bg = "white", justify = CENTER, bd = 5, relief = GROOVE, cursor = "hand2", command = dict)
searchbutton.place(x = 335, y= 200)

displaylabel = Label(root, text = "Meaning of The Word",font = ("Gabriola", 25, "bold"), fg = "Brown", bg = "antiquewhite")
displaylabel.place(x = 260, y = 315)

display = Text(root, width = 65, height = 5, font = ('Gabriola', 20), bd = 8, relief = RIDGE)
display.place(x = 18, y = 320)

root.mainloop()

