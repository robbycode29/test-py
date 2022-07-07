class Movie():

    def __init__(self, name, genre, watched=False):
        self.name = name
        self.genre = genre
        self.watched = watched

    def __repr__(self):
        return "Movie {}, {}, wathced: {} ".format(self.name, self.genre, self.watched)

    def watched(self):
        self.watched = True
    
    def json(self):
        return {
            "name": self.name,
            "genre": self.genre,
            "watched": self.watched
        }

    @classmethod
    def from_json(cls, json_data):
        # name = json_data["name"]
        # genre = json_data["genre"]
        # watched = json_data["watched"]
        return Movie(**json_data)