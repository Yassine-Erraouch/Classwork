import csv

# a list of films containing dictionaries in the following format
#  {"Titre": "Inception", "Genre": "Science-fiction", "Année": 2010, "Recettes": 829.89, "Note": 8.8}
films = [
    {"Titre": "Inception", "Genre": "Science-fiction", "Année": 2010, "Recettes": 829.89, "Note": 8.8},
    {"Titre": "Interstellar", "Genre": "Science-fiction", "Année": 2014, "Recettes": 473.8, "Note": 7.4},
    {"Titre": "The Dark Knight", "Genre": "Super-heros", "Année": 2008, "Recettes": 1004.9, "Note": 9.0},
    {"Titre": "The Shawshank Redemption", "Genre": "Drame", "Année": 1994, "Recettes": 50.7, "Note": 9.2},
    {"Titre": "The Godfather", "Genre": "Drame", "Année": 1972, "Recettes": 245.0, "Note": 9.2},
    {"Titre": "12 Angry Men", "Genre": "Drame", "Année": 1957, "Recettes": 2.5, "Note": 9.0},
    {"Titre": "Schindler's List", "Genre": "Drame", "Année": 1993, "Recettes": 321.2, "Note": 8.9},
    {"Titre": "The Lord of the Rings: The Return of the King", "Genre": "Fantasy", "Année": 2003, "Recettes": 1119.9, "Note": 8.9},
    {"Titre": "Pulp Fiction", "Genre": "Thriller", "Année": 1994, "Recettes": 213.9, "Note": 8.8},
    {"Titre": "The Good, the Bad and the Ugly", "Genre": "Western", "Année": 1966, "Recettes": 25.1, "Note": 8.8}
]

#-------------------------------functions-------------------------------------------


#function to calculate the average rating for the movies
def calculer_recettes_moyennes(films):
    total_recettes = 0
    for film in films:
        total_recettes += film["Recettes"]
    return total_recettes / len(films)


#function to count the movies based on their genre
def films_par_genre(films):
    genre_count = {}
    for film in films:
        genre = film["Genre"]
        if genre in genre_count:
            genre_count[genre] += 1
        else:
            genre_count[genre] = 1
    return genre_count

#function to categorize the movies based on their revenue 
def enrichir_donnees_films(films):
    for film in films:
        if film['Recettes'] < 100:
            film['Cat-recettes'] = 'faible'
        elif film['Recettes'] < 500:
            film['Cat-recettes'] = 'Modérée'
        else:
            film['Cat-recettes'] = 'Élevée'
        print(film)

#function to filter the movies by a specified criteria defined by a lambda function

def filtrer_par_critere(films, critere):
    return list(filter(critere, films))

#the lambda functions for filtrer_par_critere

After2000 = lambda film: film["Année"] > 2000
Before2000 = lambda film: film["Année"] < 2000
above500M = lambda film: film["Recettes"] > 500
above8rating = lambda film: film["Note"] > 8

#function to save the filtered list of movies to a CSV file compatible with Power BI containing the columns : titre, genre, année, recettes (en M$), note moyenne, catégorie de recettes
def sauvegarder_csv(films, fileName):
    enrichir_donnees_films(films)
    with open(fileName, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Titre", "Genre", "Année", "Recettes","Note moyenne", "Note", "Cat-recettes"])
        for film in films:
            writer.writerow([film["Titre"], film["Genre"], film["Année"], film["Recettes"], film["Note"], film["Cat-recettes"]])


#---------------------------------------Menu------------------------------------------

while True:
    print('-'*20)
    print("1.Calculate the average revenue for the movies")
    print("2.Count the movies based on their genre")
    print("3.Enrichir the data of the movies")
    print("4.Filter the movies by a specified criteria")
    print("5.Save the filtered list of movies to a CSV file compatible with Power BI")
    print("0.Quit")
    choice = input("Enter your choice: ")
    if choice == '1':
        print(f"The average revenue for the movies is: {calculer_recettes_moyennes(films)} M$")
    elif choice == "2":
        print(films_par_genre(films))
    elif choice == "3":
        enrichir_donnees_films(films)
    elif choice == "4":
        while True:
            print('-'*20)
            print("1.Show movies after 2000")
            print("2.Show movies before 2000")
            print("3.Show movies with revenue above 500M$")
            print("4.Show movies with rating above 8")
            print("0.Quit")
            critere = input("Enter your choice: ")
            if critere == '1':
                print(filtrer_par_critere(films, After2000))
            elif critere == "2":
                print(filtrer_par_critere(films, Before2000))
            elif critere == "3":
                print(filtrer_par_critere(films, above500M))
            elif critere == "4":
                print(filtrer_par_critere(films, above8rating))
            elif critere == "0":
                break
            else:
                print("Invalid choice")
    
    elif choice == "5":
        sauvegarder_csv(films, "movies.csv")
    elif choice == "0":
        break
    else:
        print("Invalid choice")