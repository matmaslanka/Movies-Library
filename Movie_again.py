movies = [
    {'name': 'Up',
     'director': 'Disney',
     'year': 2009},
    {'name': '1899',
     'director': 'German',
     'year': 2022}
]

user_choice = "r"

find_library = {'n': 'name', 'd': 'director', 'y': 'year'}


def add():
    movie_name = input('Type movie name: ')
    movie_director = input('Type direction name: ')
    movie_year = input('Type movie year: ')
    movies.append({"name": movie_name,
                   'director': movie_director,
                   'year': movie_year
                   })


def show():
    for movie in movies:
        print(f'Name: {movie["name"]} -- Director: {movie["director"]} -- Year: {movie["year"]}')


def search():
    find = input("How do you want to find the movie? ('n' by name, 'd' by director, 'y' by year): ")
    find_name = input(f'Please type {find_library[find]} of the move you want to find: ')
    i_found = 0

    for searching in movies:
        if str(searching[find_library[find]]) == str(find_name):
            print(f'I found {searching["name"]} -- {searching["director"]} -- {searching["year"]}')
            i_found += 1
    if i_found == 0:
        print('I found nothing')


while user_choice != "q":
    user_choice = input("What do you want do do? ('a' add movie, 'p' show list of movies, "
                        "'s' search for movie, 'q' quit) ")
    if user_choice == 'a':
        add()
    elif user_choice == 'p':
        show()
    elif user_choice == 's':
        search()
    elif user_choice == 'q':
        print('Bye bye!')
    else:
        print("Unknown command!")
