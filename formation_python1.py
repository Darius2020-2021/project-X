#la place de ciné
age = int(input("quel est votre âge ? "))
argent= int(input("combien d'argent avez vous ?"))
place_mineur= 7
place_majeur= 12
prix_pop_corn= 5
prix_mineur = argent-place_mineur
prix_majeur = argent-place_majeur
prix_mineur_pop = prix_mineur-prix_pop_corn
prix_majeur_pop = prix_majeur-prix_pop_corn
if age < 18 :
    print("votre place de ciné est de " +str(place_mineur)+ " euro")
    pop_corn= input("souhaitez vous du popcorn ?")
    if pop_corn == "oui":
      print("ça vous fera "+ str(prix_pop_corn) + " euro")
      print("ça vous fera donc en tout " + str(prix_mineur_pop) + " euro bonne soirée")
    else:
      print("ok ça vous fera donc en tout " + str(prix_mineur) + " euro bonne soirée")
else:
    print("votre place de ciné est de " + str(place_majeur)+ " euro")
    pop_corn= input("souhaitez vous du popcorn ?")
    if pop_corn == "oui":
      print("ça vous fera "+ str(prix_pop_corn) + " euro")
      print("ça vous fera donc en tout " + str(prix_majeur_pop) + " euro bonne soirée")
    else:
      print("ok ça vous fera donc en tout " + str(prix_majeur) + " euro bonne soirée")
