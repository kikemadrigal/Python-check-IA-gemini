#la librería tkinter viene preinstalada en python y no hay que instalarla
from tkinter import Tk, Label, Button, Text, Frame, Listbox, ttk
#from tkinter.filedialog import askopenfile
from tkinter.messagebox import showinfo
#PIL significa biblioteca de imagenes de Python
#usa PIL para manipular imagenes, colores, agregar texto, cambiar tamaño, etc
from PIL import Image, ImageTk
import os
from askGemini import ask
import requests
from io import BytesIO






def createWindow():
    window= Tk()
    window.title("Image Analysis")
    #window.geometry("500x500")
    height=600
    width=530
    x=(window.winfo_screenwidth()//2)-(width//2)
    y=(window.winfo_screenheight()//2)-(height//2)
    window.geometry("{}x{}+{}+{}".format(width,height,x,y))
    frame = Frame(window)
    frame.grid(row=3,column=2)

    directorio = "images/"
    try:
        os.stat(directorio)
    except:
        os.mkdir(directorio)
        for i in range(0,8):
            response = requests.get("https://murciadev.tipolisto.es/files/plants/planta"+str(i)+".jpg")
            img = Image.open(BytesIO(response.content))
            img.save(directorio+"/planta"+str(i)+".jpg")
 

    _Font = ("Arial", 14)
    listBox=Listbox(window, bg="#f7ffde")
    listBox.bind('<<ListboxSelect>>', lambda e: submit(listBox, labelImage))
    labelImage=Label(window, text="Select image")
    textRespose=Text(window, height=10)
    textRequest=Text(window, height=10)
    buttonReloadImages=Button(window,text="Reload images",padx=20, pady=20, command=lambda:reloadImages(listBox))
    buttonAskGemini=Button(window,text="Ask Gemini",padx=20, pady=20, command=lambda:askGemini(listBox, textRequest,textRespose, progressbar,window))
    progressbar = ttk.Progressbar(mode="determinate")
   
    

    reloadImages(listBox)
    listBox.select_set(1)
    listBox.selection_set( first = 1 )
    listBox.event_generate("<<ListboxSelect>>")
    submit(listBox, labelImage)


    #define un grid
    #Confiramos solo 2 columnas y le decimos que tengan el mismo peso
    #Confiramos solo 3 filas y le decimos que tengan el mismo peso
    window.columnconfigure(0, weight=1)
    window.columnconfigure(1, weight=1)
    window.rowconfigure(0, weight=1)
    window.rowconfigure(1, weight=1)
    window.rowconfigure(3, weight=1)


    #Colocando el widget
    listBox.grid(row=0, column=0, sticky="nsew")
    labelImage.grid(row=0, column=1, sticky="nsew",padx=10, pady=10)
    textRequest.grid(row=1, column=0, sticky="nsew")
    textRespose.grid(row=1, column=1, sticky="nsew")
    progressbar.grid(row=2, column=0, columnspan=2, sticky="nsew")
    buttonReloadImages.grid(row=3, column=0, sticky="nsew")
    buttonAskGemini.grid(row=3, column=1, sticky="nsew")

    textRequest.insert(1.0, "Dime el tipo de planta de la imagen")
    progressbar.configure(value=0)
  
    window.mainloop()

def submit(listBox:Listbox, labelImage:Label):
    currentSelection=listBox.curselection()
    if(currentSelection.__len__()==0):
        showinfo("Error", "Please select an image")
    else:
        path_image=listBox.get(currentSelection)
        image_original=Image.open("images/"+path_image)
        width, height = image_original.size
        ratio = width / height
        new_height = 300
        new_width = int(ratio * new_height)
        image_redimensionada = image_original.resize((new_width, new_height))
        image_tk=ImageTk.PhotoImage(image_redimensionada)
        labelImage.configure(image=image_tk)
        labelImage.image=image_tk

def askGemini(listBox:Listbox, textRequest:Text, textRespose:Text, progressbar:ttk.Progressbar, window:Tk):
    progressbar.configure(value=50)
    window.update()
    currentSelection=listBox.curselection()
    if(currentSelection.__len__()==0):
        showinfo("Error", "Please select an image")
        progressbar.configure(value=100)
    else:
        path_image=listBox.get(currentSelection)
        image_original=Image.open("images/"+path_image)
        consulta=textRequest.get("1.0", "end-1c")
        respuesta=ask(consulta, image_original)
        textRespose.delete("1.0", "end")
        textRespose.insert(1.0, respuesta)
        print(respuesta)
        progressbar.configure(value=100)
    progressbar.configure(value=0)
    

def reloadImages(listBox:Listbox):
    listBox.delete(0, "end")
    files=os.listdir("images")
    counter=0
    for file in files:
        listBox.insert(counter, file)
        counter+=1
 

createWindow()
