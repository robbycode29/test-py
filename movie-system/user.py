# import csv
import json

from movie import Movie

class User():
    def __init__(self, name, movies=[]):
        self.name = name
        self.movies = movies
    
    def __repr__(self):
        return "{}".format(self.name)

    def watched_movies(self):
        return [movie for movie in self.movies if movie.watched]

    def add_movie(self, movie):
        self.movies.append(movie)

    def delete_movie(self, movie):
        self.movies.remove(movie)

    # def save_to_file(self):
    #     with open(self.name + ".csv", "w") as f:
    #         userwriter = csv.writer(f)
    #         userwriter.writerow(["movie", "genre", "watched"])
    #         for movie in self.movies:
    #             userwriter.writerow([movie.name, movie.genre, movie.watched])

    # def load_user_from_file(self):
    #     with open(self.name + ".csv", "r") as f:
    #         userreader = csv.reader(f)
    #         for row in userreader:
    #             movie = Movie(row[0], row[1], row[2])
    #             self.movies.append(movie)

    def json(self):
        return {
                "name": self.name,
                "movies": [movie.json() for movie in self.movies]
        }
        
    
    @classmethod
    def from_json(cls, json_data):
        name = json_data["name"]
        movies = [Movie.from_json(movie) for movie in json_data["movies"]]
        return User(name, movies)

    def save_to_file_as_json(self):
        with open("./accounts/{}".format(self.name) + ".json", "w") as f:
            json.dump(self.json(), f)

    def load_user_from_file_as_json(self):
        with open("./accounts/{}".format(self.name) + ".json", "r") as f:
            data = json.load(f)
            self.name = data["name"]
            self.movies = [Movie.from_json(movie) for movie in data["movies"]]
            return self