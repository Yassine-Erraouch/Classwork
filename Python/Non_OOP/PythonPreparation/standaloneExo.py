import csv
movies = [
    {"Title": "Interstellar", "Genre": "Science-fiction", "Year": 2014, "Revenue": 677.47, "Rating": 8.6},
    {"Title": "Pulp Fiction", "Genre": "Drama", "Year": 1994, "Revenue": 213.93, "Rating": 8.9},
    {"Title": "The Dark Knight", "Genre": "Action", "Year": 2008, "Revenue": 1004.94, "Rating": 9.0}
]


#lambda function to filter out movies with a rating below 8.8
movies_above_8 = lambda movie: movie["Rating"] > 8.8

def filter_by_rating(movies, movies_above_8):
    filtered_by_rating = list(filter(movies_above_8, movies))
    return filtered_by_rating

#find the movie with the highest revenue using the max() function:
highestRevenue = max(movies, key = lambda movie: movie["Revenue"])

#function to calculate the average rating of all the movies in the list
def average_rating(movies):
    totalRating = 0
    for movie in movies:
        totalRating += movie["Rating"]
    return totalRating / len(movies)

print(average_rating(movies))

#function that enriches the data

def categorize_revenue(movies):
    for movie in movies:
        if movie["Revenue"] <500:
            movie["Revenue Category"] = "Low"
        elif movie["Revenue"] <800:
            movie["Revenue Category"] = "Medium"
        else:
            movie["Revenue Category"] = "High"
    return movies
categorize_revenue(movies)

#save to csv
def saveCSV (movies, filename):
    with open(filename, 'w', newline="" , encoding='utf-8')as file:
        writer = csv.DictWriter(file, fieldnames=movies[0].keys())
        writer.writeheader()
        writer.writerows(movies)
    print('movies saved successfully') 



saveCSV(movies, "spanky")

#sort movies by year in ascending order:
def sortByYear(movies):
    sortedByYear = sorted(movies, key = lambda movie: movie['Year'])
    return sortedByYear

print(sortByYear(movies))
#sot movies by rating in descending order:
def sortByRating(movies):
    sortedByRating = sorted(movies, key= lambda movie: movie['Rating'], reverse=True)
    return sortedByRating

print(sortByRating(movies))



print(filter_by_rating(movies, movies_above_8))


#bonus
#filtered data will only contain even numbers (2,4,6)
#result will be the sum of filtered_data so 12
