from tkinter import Tk, Label, ttk, PhotoImage
import os

root= Tk()
root.title("Loading Page")
#image=PhotoImage(file="loading.gif")


height=430
width=530
x=(root.winfo_screenwidth()//2)-(width//2)
y=(root.winfo_screenheight()//2)-(height//2)
root.geometry("{}x{}+{}+{}".format(width,height,x,y))
#root.overrideredirect(True)

root.config(background="#2f6c68")

label = Label(root, text="Home page", font=("Arial", 24), fg="white", bg="#2f6c68")
label.place(x=160, y=70)

#bg_label=Label(root, image=image)
#bg_label.place(x=0, y=0, relwidth=1, relheight=1)


progressbar = ttk.Progressbar(root, mode="determinate", orient="horizontal", length=300)
progressbar.place(x=100, y=200)

i=0


def top():
    root.withdraw()
    os.system("python main.py")
    root.destroy()
def load():
    global i
    if i<=10:
        txt="loading "+str(10*i)+"%"
        label.configure(text=txt)
        label.after(600, load)
        #progressbar.configure(value=10*i)
        progressbar['value'] = 10*i
        i+=10
    else:
        top()

load()
#root.resizable(False,False)
root.mainloop()