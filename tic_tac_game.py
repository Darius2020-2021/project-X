from tkinter import *
from random import choice
#création de la fenetre 

#l'ajout des fonctions pour les boutons
def bouton_recom():
    window = Tk()
    window.geometry("675x700")
    window.minsize(450,650)
    window.title("TIC TAC")
    window.config(background="#d7dbdd")
#creation de la frame
    frame = Frame(window, bg="#d7dbdd" , bd=2, relief=SUNKEN)
    acte = False
    while acte == False:
        def action1():
            bouton1.config(text="  X  ")
            aleatoire1.config(text=" O ")
        def action2():
            bouton2.config(text="  X  ")
            aleatoire2.config(text=" O ")
        def action3():
            bouton3.config(text="  X  ")
            aleatoire3.config(text=" O ")
        def action4():
            bouton4.config(text="  X  ")
            aleatoire4.config(text=" O ")
        def action7():
            bouton5.config(text="  X  ")
            aleatoire5.config(text=" O ")
        def action8():
            bouton6.config(text="  X  ")
            aleatoire6.config(text=" O ")
        def action9():
            bouton7.config(text="  X  ")
            aleatoire7.config(text=" O ")
        def action10():
            bouton8.config(text="  X  ")
            aleatoire8.config(text=" O ")
        def action13():
            bouton9.config(text="  X  ")
            aleatoire9.config(text=" O ")
        def action14():
            bouton10.config(text="  X  ")
            aleatoire10.config(text=" O ")
        def action15():
            bouton11.config(text="  X  ")
            aleatoire11.config(text=" O ")
        def action16():
            bouton12.config(text="  X  ")
            aleatoire12.config(text=" O ")
        def action19():
            bouton13.config(text="  X  ")
            aleatoire13.config(text=" O ")
        def action20():
            bouton14.config(text="  X  ")
            aleatoire14.config(text=" O ")
        def action21():
            bouton15.config(text="  X  ")
            aleatoire15.config(text=" O ")
        def action22():
            bouton16.config(text="  X  ")
            aleatoire16.config(text=" O ")
#creation de boutons pour le game
        bouton1 = Button(frame, text="      ", font=("Tahoma", 55),
                  bg="#34495e", fg="#c0392b", command=action1)
        bouton2= Button(frame, text="      ", font=("Tahoma",55),
                  bg="#34495e",fg="#c0392b", command=action2)
        bouton3 = Button(frame, text="      ", font=("Tahoma", 55),
                  bg="#34495e", fg="#c0392b", command=action3 )
        bouton4= Button(frame, text="      ", font=("Tahoma",55),
                  bg="#34495e",fg="#c0392b", command=action4)
        bouton5 = Button(frame, text="      ", font=("Tahoma", 55),
                  bg="#34495e", fg="#c0392b", command=action7 )
        bouton6= Button(frame, text="      ", font=("Tahoma",55),
                  bg="#34495e",fg="#c0392b", command=action8)
        bouton7 = Button(frame, text="      ", font=("Tahoma", 55),
                  bg="#34495e", fg="#c0392b", command=action9 )
        bouton8= Button(frame, text="      ", font=("Tahoma",55),
                  bg="#34495e",fg="#c0392b", command=action10)
        bouton9= Button(frame, text="     ", font=("Tahoma",55),
                  bg="#34495e",fg="#c0392b", command=action13)
        bouton10= Button(frame, text="     ", font=("Tahoma",55),
                  bg="#34495e",fg="#c0392b", command=action14)
        bouton11 = Button(frame, text="     ", font=("Tahoma", 55),
                  bg="#34495e", fg="#c0392b", command=action15 )
        bouton12= Button(frame, text="     ", font=("Tahoma",55),
                  bg="#34495e",fg="#c0392b", command=action16)
        bouton13 = Button(frame, text="     ", font=("Tahoma", 55),
                  bg="#34495e", fg="#c0392b",command=action19)
        bouton14= Button(frame, text="     ", font=("Tahoma",55),
                  bg="#34495e",fg="#c0392b", command=action20)
        bouton15= Button(frame, text="     ", font=("Tahoma",55),
                  bg="#34495e",fg="#c0392b", command=action21)
        bouton16 = Button(frame, text="     ", font=("Tahoma", 55),
                  bg="#34495e", fg="#c0392b", command=action22 )
#la progra pour l'IA
        les_boutons1 =[bouton2,bouton3,
        bouton4,bouton5,bouton6,bouton7,bouton8,bouton9,
        bouton10, bouton11,bouton12,bouton13,bouton14,bouton15,
        bouton16]
        aleatoire1= choice(les_boutons1)
        les_boutons2 =[bouton6,bouton3, bouton1,
        bouton4,bouton5,bouton7,bouton8,bouton9,
        bouton10, bouton11,bouton12,bouton13,bouton14,bouton15,
        bouton16]    
        aleatoire2= choice(les_boutons2)
        les_boutons3 =[bouton7, bouton4,bouton2,
        bouton5,bouton6,bouton8,bouton9,
        bouton10, bouton11,bouton12,bouton13,bouton14,bouton15,
        bouton16]
        aleatoire3= choice(les_boutons3)
        les_boutons4 =[bouton3,bouton8,bouton2,bouton3,
        bouton5,bouton6,bouton7,bouton8,bouton9,
        bouton10, bouton11,bouton12,bouton13,bouton14,bouton15,
        bouton16]
        aleatoire4= choice(les_boutons4)
        les_boutons5 =[bouton1,bouton2,bouton3,bouton4,bouton6,bouton7,bouton8,bouton9,bouton10,bouton11,
        bouton12,bouton13,bouton14,bouton15,bouton16]
        aleatoire5= choice(les_boutons5)
        les_boutons6 =[bouton1,bouton2,bouton3,bouton4,
        bouton5,bouton7,bouton8,bouton9,bouton10,bouton11,
        bouton12,bouton13,bouton14,bouton15,bouton16]
        aleatoire6= choice(les_boutons6)
        les_boutons7 =[bouton1,bouton2,bouton3,bouton4,
        bouton5,bouton6,bouton8,bouton9,bouton10,bouton11,
        bouton12,bouton13,bouton14,bouton15,bouton16]
        aleatoire7= choice(les_boutons7)
        les_boutons8 =[bouton1,bouton2,bouton3,bouton4,
        bouton5,bouton6,bouton7,bouton9,bouton10,bouton11,
        bouton12,bouton13,bouton14,bouton15,bouton16]
        aleatoire8= choice(les_boutons8)
        les_boutons9 =[bouton1,bouton2,bouton3,bouton4,
        bouton5,bouton6,bouton7,bouton8,bouton10,bouton11,
        bouton12,bouton13,bouton14,bouton15,bouton16]
        aleatoire9= choice(les_boutons9)
        les_boutons10 =[bouton1,bouton2,bouton3,bouton4,
        bouton5,bouton6,bouton7,bouton8,bouton9,bouton11,
        bouton12,bouton13,bouton14,bouton15,bouton16]
        aleatoire10= choice(les_boutons10)
        les_boutons11 =[bouton1,bouton2,bouton3,bouton4,
        bouton5,bouton6,bouton7,bouton8,bouton9,bouton10,
        bouton12,bouton13,bouton14,bouton15,bouton16]
        aleatoire11= choice(les_boutons11)
        les_boutons12 =[bouton1,bouton2,bouton3,bouton4,
        bouton5,bouton6,bouton7,bouton8,bouton9,bouton10,bouton11,bouton13,bouton14,bouton15,bouton16]
        aleatoire12= choice(les_boutons12)
        les_boutons13 =[bouton1,bouton2,bouton3,bouton4,
        bouton5,bouton6,bouton7,bouton8,bouton9,bouton10,bouton11,
        bouton12,bouton14,bouton15,bouton16]
        aleatoire13= choice(les_boutons13)
        les_boutons14=[bouton1,bouton2,bouton3,bouton4,
        bouton5,bouton6,bouton7,bouton8,bouton9,bouton10,bouton11,
        bouton12,bouton13,bouton15,bouton16]
        aleatoire14= choice(les_boutons14)
        les_boutons15 =[bouton1,bouton2,bouton3,bouton4,
        bouton5,bouton6,bouton7,bouton8,bouton9,bouton10,bouton11,
        bouton12,bouton13,bouton14,bouton16]
        aleatoire15= choice(les_boutons15)
        les_boutons16 =[bouton1,bouton2,bouton3,bouton4,
        bouton5,bouton6,bouton7,bouton8,bouton9,bouton10,bouton11,
        bouton12,bouton13,bouton14,bouton15]
        aleatoire16= choice(les_boutons16)
#La fenetre pour le messsage
        if bouton1.config(text="  X  ") and bouton5.config(text="  X  ") and bouton9.config(text="  X  ") and bouton13.config(text="  X  "):
            acte= False
            fen_message = Toplevel()
            msg= Message(fen_message, text="vous avez gaggner")
            bouton_recom = Button(fen_message, text="recommencer", command="reboot")
            bouton_quitter = Button(fen_message, text="quitter", command="quit")
#leurs implementations sur l'interface graphique
        frame.pack(expand=YES)
        bouton1.grid(row=0,column=0)
        bouton2.grid(row=1,column=0)
        bouton3.grid(row=2,column=0)
        bouton4.grid(row=3,column=0)
        bouton5.grid(row=0,column=1)
        bouton6.grid(row=1,column=1)
        bouton7.grid(row=2,column=1)
        bouton8.grid(row=3,column=1)
        bouton9.grid(row=0,column=2)
        bouton10.grid(row=1,column=2)
        bouton11.grid(row=2,column=2)
        bouton12.grid(row=3,column=2)
        bouton13.grid(row=0,column=3)
        bouton14.grid(row=1,column=3)
        bouton15.grid(row=2,column=3)
        bouton16.grid(row=3,column=3)
