from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

def change(text="type",src="English",dest="Urdu"):
    text1=text
    src1=src
    dest1=dest
    trans=Translator()
    trans1=trans.translate(text,src=src1,dest=dest1)
    return trans1.text

def data():
    s=comb_sor.get()
    d=comb_dest.get()
    masg= Sor_txt.get(1.0,END)
    textget=change(text=masg,src=s,dest=d)
    dest_txt.delete(1.0,END)
    dest_txt.insert(END,textget)


root=Tk()
root.title("translator")
root.geometry ("500x700")
root.config(bg="blue")

Label_text=Label(root,text="Translator",font=("New Roman Times",40,"bold"),bg="blue")
Label_text.place(x=100,y=40,height=50,width=320)

frame=Frame(root).pack(side=BOTTOM)

Label_text=Label(root,text="Source Text",font=("New Roman Times",20,"bold"),fg="Black",bg="blue")
Label_text.place(x=100,y=100,height=20,width=300)

Sor_txt = Text(frame, font=("New Roman Times",20,"bold"),wrap=WORD)
Sor_txt.place(x=100,y=130,height=150,width=320)

list_text = list(LANGUAGES.values())

comb_sor = ttk.Combobox(frame,value=list_text)
comb_sor.place(x=100,y=300,height=40,width=100)

comb_sor.set("English")

Button_change= Button(frame,text="Tanslate",relief=RAISED,command=data)
Button_change.place(x=210,y=300,height=40,width=100)

comb_dest = ttk.Combobox(frame,value=list_text)
comb_dest.place(x=320,y=300,height=40,width=100)

comb_dest.set("English")

Label_txt=Label(root,text="Dest Text",font=("New Roman Times",20,"bold"),fg="Black",bg="blue")
Label_txt.place(x=100,y=360,height=20,width=300)

dest_txt = Text(frame, font=("New Roman Times",20,"bold"),wrap=WORD)
dest_txt.place(x=100,y=400,height=150,width=320)

root.mainloop()