from movie import Movie
from user import User

# user.add_movie(Movie("Spiderman", "Action", True))
# user.add_movie(Movie("Avatar", "Action", False))
# user.add_movie(Movie("Titanic", "Drama", True))
# user.add_movie(Movie("The Matrix", "Action", True))


# user.save_to_file()

# user.load_user_from_file()
# print(user)
# print(user.movies)

# user.save_to_file_as_json()

# print(user.load_user_from_file_as_json())

users = []

def create_user(name):
    users.append(User(name))
    user = users[-1]
    return user

def delete_user(user):
    del user

def user_select_menu():
    for i, user in enumerate(users):
        print(i, user.name)
    choice = input("Your user choice: ")
    return choice
    

def menu():
    print("0. Select user:")
    print("1. Add user")
    print("2. Delete user")
    print("3. Add movie")
    print("4. Delete movie")
    print("5. Mark movie as watched")
    print("6. Print user")
    print("7. Print all movies")
    print("8. Print watched movies")
    print("9. Exit")
    choice = input("Your choice: ")
    return choice


if __name__ == '__main__':
    while True:
        choice = menu()
        if choice == "0":
            choice = user_select_menu()
            user = users[int(choice)]
        elif choice == "1":
            name = input("Name: ")
            user = create_user(name)
        elif choice == "2":
            delete_user(user)
        elif choice == "3":
            name = input("Name: ")
            genre = input("Genre: ")
            watched = input("Watched: ")
            user.add_movie(Movie(name, genre, watched))
        elif choice == "4":
            name = input("Name: ")
            user.delete_movie(Movie(name))
        elif choice == "5":
            name = input("Name: ")
            user.movies[name].watched()
        elif choice == "6":
            print(user)
        elif choice == "7":
            print(user.movies)
        elif choice == "8":
            print(user.watched_movies())
        elif choice == "9":
            break
        else:
            print("Invalid choice")
        user.save_to_file_as_json()
    print("Bye!")
    
