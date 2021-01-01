from tkinter import *
import webbrowser
window= Tk()
window.title("essaie")
window.attributes('-fullscren', 1)
window.iconbitmap("electronics.ico")
window.config(background="#5DADE2")
def action():
    webbrowser.open_new("http://youtube.com/apple")

frame = Frame(window, bg="#5DADE2")
frame1= Frame(window, bg="#5DADE2")
frame.pack()
frame1.pack(expand=YES)
texte = Label(frame, text="Bienvenue dans l'appli", 
font=("Tahoma", 20), bg="#5DADE2", fg="black")
texte.pack()
width = 150
height= 150
image = PhotoImage(file="electronics.png")
canvas = Canvas(frame1, width=width, height=height, bg="#5DADE2", bd = 0, highlightthickness=0)
canvas.create_image(height/2, width/2, image=image)
canvas.grid(row=0, column=0, sticky=W)
bouton = Button(frame1, text="appuyez ici", font=("tahoma", 20), bg="white",
fg="black", command= action)
entre = Entry(frame1, text="", font=("tahoma",20), 
              bg="#5DADE2", fg="white", selectborderwidth=5)
bouton.grid(row=2,column=1,sticky=W )
entre.grid(row=1, column=0, sticky=W)

window.mainloop()
