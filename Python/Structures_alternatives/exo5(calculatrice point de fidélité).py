def calculer_points(depense):
    points = 0

    if depense < 50:
        points = 0
    elif depense >= 50 and depense <= 100:
        points = (depense - 50) // 10 
    else:
        points = (depense - 100) // 5 

    return points

# Demande à l'utilisateur combien il a dépensé
while True:
    try:
        depense = float(input("Combien avez-vous dépensé dans le magasin ? "))
        break
    except:
        print('valeur invalide')
# Calcule les points de fidélité
points = calculer_points(depense)

# Affiche les points de fidélité
print(f"Vous avez obtenu {points} points de fidélité.")