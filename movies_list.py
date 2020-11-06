from movie_tape import Movie_tape
"""
Movies List
"""


class Movies_list:
    list = []

    def __init__(self):
        self.list = []

    def add_to_list(self, Movie_tape):
        if Movie_tape not in self.list and (Movie_tape.movie.title + Movie_tape.id not in self.get_movies()):
            self.list.append(Movie_tape)
        else:
            raise TypeError("Movie tape already included")

    def delete_from_list(self, Movie_tape):
        return self.list.remove(Movie_tape)

    # def delete_movie_tape(self, Movie_tape):
    #     return list.remove(Movie_tape)

    def get_by_movie(self, movie):
        for object in self.list:
            if object.movie == movie:
                return object
        return None

    def delete_by_space(self, number):
        self.list.pop(number)

    def get_movies(self):
        list_movies = []
        for object in self.list:
            list_movies.append(object.movie.title + object.id)
        return list_movies

    def stock_of_movie(self, movie):
        list = []
        for object in self.list:
            if object.movie == movie:
                list.append(object)
        return list
