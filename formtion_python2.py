choix = int(input("choisisez un nombre pour le juste prix entre 1 et 1000 "))
prix = 500
if choix == prix:
    print("félicitation vous avez reussi")
while choix != prix:
    essaye= int(input("c'est pas ça veillz reesayer: "))
    if essaye == prix:
        print("félicitation vous avez reussi")
        break
    else:
        print("continuer vous y etes presque")
