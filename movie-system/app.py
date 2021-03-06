import os
from movie import Movie
from user import User
import json



def db(user_list):
        return {
            "users": ["{}".format(user.name) for user in user_list]
}

def fetch_users():
    with open("./accounts/users.json", "r") as f:
        try:
            users = []
            data = json.load(f)
            accounts = data['users']
            for user in accounts:
                with open('./accounts/{}'.format(user) + ".json", "r") as f:
                    user_data = json.load(f)
                    users.append(User.from_json(user_data))
            return users
        except: 
            return []

def create_user(name):
    users.append(User(name))
    with open("./accounts/users.json", "w") as f:
        json.dump(db(users), f)
        user = users[-1]
    return user

def delete_user(user):
    users.remove(user)
    with open("./accounts/users.json", "w") as f:
        json.dump(db(users), f)
    path_to_accounts = "accounts"
    user_to_remove = str(user) + ".json"
    if os.path.exists(path_to_accounts):
        path_to_be_removed = os.path.join(path_to_accounts, user_to_remove)
        print(path_to_be_removed)
        try:
            # os.chmod(path_to_be_removed, 0o777)
            os.remove(path_to_be_removed)
        except Exception as e:
            print("Error:" + e)
        del user
        user = users[-1]
    else:
        print("No accounts found")

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


users = fetch_users()

if __name__ == '__main__':
    while True:
        choice = menu()
        if choice == "0":
            choice = user_select_menu()
            user = users[int(choice)]
        elif choice == "1":
            name = input("Name: ")
            user = create_user(name)
            user.save_to_file_as_json()
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
    print("Bye!")
    
