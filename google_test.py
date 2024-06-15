from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

def change(text="type", src="English", dest="Hindi"):
    try:
            trans = Translator()
            trans1 = trans.translate(text, src=src, dest=dest)
            return trans1.text

    except Exception as e:
        print(f"Error: {e}")
        return "Translation Error"

def data():
    s = comb1_sor.get()
    d = comb1_dest.get()
    masg = Sor_txt.get(1.0, END).strip()
    textget = change(text=masg, src=s, dest=d)
    dest_txt.delete(1.0, END)
    dest_txt.insert(END, textget)

root = Tk()
root.title("Translator")
root.geometry("500x700")
root.config(bg='Red')

lab_txt = Label(root, text="Translator", font=("Time New Roman", 40, "bold"))
lab_txt.place(x=100, y=40, height=50, width=300)

frame = Frame(root).pack(side=BOTTOM)

lab_txt = Label(root, text="Source Text", font=("Time New Roman", 15, "bold"), fg="Black")
lab_txt.place(x=100, y=100, height=20, width=300)

Sor_txt = Text(frame, font=("Time New Roman", 12, "bold"), wrap=WORD)
Sor_txt.place(x=10, y=130, height=150, width=480)

list_text = list(LANGUAGES.values())

comb1_sor = ttk.Combobox(frame, value=list_text)
comb1_sor.place(x=10, y=300, height=40, width=150)
comb1_sor.set("english")

button_change = Button(frame, text="Translate", relief=RAISED, command=data)
button_change.place(x=170, y=300, height=40, width=150)

comb1_dest = ttk.Combobox(frame, value=list_text)
comb1_dest.place(x=330, y=300, height=40, width=150)
comb1_dest.set("english")

lab_txt = Label(root, text="Dest Text", font=("Time New Roman", 15, "bold"), fg="Black")
lab_txt.place(x=100, y=360, height=20, width=300)

dest_txt = Text(frame, font=("Time New Roman", 12, "bold"), wrap=WORD)
dest_txt.place(x=10, y=400, height=150, width=480)

root.mainloop()
