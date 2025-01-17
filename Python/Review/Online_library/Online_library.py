from abc import ABC, abstractmethod
from datetime import datetime
import re
import json
# pattern for dates
date_pattern = r"\d{4}"
isbn_pattern = r"\d{10}(\d{3})*"
# custom errors

class CustomError(Exception): # error template
    def __init__(self, message, code):
        self.message = message
        self.code = code
        



class Document(ABC):
    def __init__(self, id=int, title=str, author=str, publication_year=int):
        self.id = id
        self.title= title
        self.author = author
        if publication_year > 1990:
            self.pub_year = publication_year
        else:
            raise CustomError("Publication year must be greater than 1990", "yearError")
        # pub_year_str = str(publication_year)
        # if re.match(date_pattern, pub_year_str):
        #     pub_year_date = datetime.strptime(pub_year_str, "%Y")
        #     if pub_year_date < datetime(1990, 1, 1):
        #         raise CustomError("Date Cannot be before 1990", "002")
        # else:
        #     raise CustomError("Date Format is not valid", "001")
        
    
    def edit_details(self, title=None, author=None, publication_year=None):
        self.title= title
        self.author = author
        self.pub_year = publication_year
        print("Document information has been modified successfully!")
        
    def show_details(self):
        return f"Document information: \n id: {self.id}\t Title: {self.title}\t Author: {self.author}\t Publication year: {self.pub_year}"     
    def __str__(self):
        return f"Document information: \n id: {self.id}\t Title: {self.title}\t Author: {self.author}\t Publication year: {self.pub_year}"
    
    
class Book(Document):
    def __init__(self, id, title, author, publication_year, isbn=int, number_of_pages=int):
        super().__init__(id, title, author, publication_year)
        if re.match(isbn_pattern, str(isbn)):
            self.isbn = isbn
            self.pages = number_of_pages
        else:
            raise CustomError("ISBN code is not valid", "101")
            
            
    
    def show_details(self):
        return f"(ISBN:{self.isbn}, Number of pages: {self.pages})"
    
    def __str__(self):
        return super().__str__() + f"\t ISBN: {self.isbn}\t Pages:{self.pages}"
    

class Magazine(Document):
    def __init__(self, id, title, author, publication_year, number=int, frequency=str):
        super().__init__(id, title, author, publication_year)
        if frequency.lower() in ["monthly", "weekly", "bi-weekly", "bi-monthly"]:
            self.number = number
            self.frequency= frequency
        else:
            raise CustomError("Frequency is Invalid", "00F1")

    def show_details(self):
        return f"(Magazine number: {self.number}, Frequency: {self.frequency})"

    def __str__(self):
        return super().__str__() + f"\tNumber: {self.number}, Frequency: {self.frequency}"

class CD(Document):
    def __init__(self,id, title, author, publication_year, genre=str, duration=float):
        super().__init__(id, title, author, publication_year)
        music_genres = ["pop", "rock", "jazz", "classical", "hip hop", "electronic", "r&b", "country", "reggae", "blues"]
        if genre.lower() not in music_genres:
            raise  CustomError("The genre you entered is unknown", "00g1")
        else:
            self.genre = genre
            self.duration = duration
            
    
    def __str__(self):
       return super().__str__()+ f"\tGenre: {self.genre}\t Duration:{self.duration}"
    

class Library:
    def __init__(self):
        self.doc_list= list()
    
    def add_document(self, document):
        if document not in self.doc_list:
            self.doc_list.append(document)
            print("Document added to the library successfully!")
        else:
            return f"This document is already in the library."
        
    def remove_document(self, id):
        for document in self.doc_list:
            if document.id == id:
                self.doc_list.remove(document)
                return f"Document removed Successfully!"
            
        return f"Document does not exist in the library."

    def update_document(self, id, title=None, author=None, publication_year=None):
        for document in self.doc_list:
            if document.id == id: 
                document.title, document.author, document.pub_year = title, author, publication_year
                return f"Document updated successfully!"
            else:
                return f"Document does not exist in the library."
                
    
    def display_all_documents(self):
        print(f"{'ID':<5}{'Title':<20}{'Author':<20}{'Publication Year':<15}{'Type':<10}{'Details':<50}")
        print("-" * 120)
        for document in self.doc_list:
           print(f'{document}')
            
    def filter_documents(self, criteria, value):
        pass
        # matches = []
        # if criteria.lower() == "author":
        #     for document in self.doc_list:
        #         if document.author.lower() == value.lower():
        #             matches.append(document)
        # elif criteria.lower() == "year":
        #     for document in self.doc_list:
        #         if document.pub_year == value:
        #             matches.append(document)
        # else:
        #     raise CustomError("You can only filter by author name or publication year")
        # return matches
        
    def save_library_to_json(self, filename):
        with open(filename, "w") as file:
            json.dump(self.doc_list, file)
        print(f"Library saved to {filename} successfully!")
        
        

if __name__ == "__main__":
    book1 = Book(1, "Python Crash Course", "Eric Matthes", 2019, 1234567890, 500)
    magazine1 = Magazine(2, "Python Magazine", "Somebody", 2020, 1, "Monthly")
    cd1 = CD(3, "The Dark Side of the Moon", "Pink Floyd", 1992, "Rock", 45)
    library = Library()
    library.add_document(book1)
    library.add_document(magazine1)
    library.add_document(cd1)
    library.display_all_documents()
    library.update_document(1, title="Python Crash Course 2nd Edition", publication_year=2020)
    library.display_all_documents()
    library.remove_document(2)
    library.display_all_documents()
    library.filter_documents("author", "Eric Matthes")
    library.save_library_to_json("library.json")
