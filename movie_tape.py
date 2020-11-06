"""
Class Movie tape
"""

from movie import Movie


class Movie_tape:
    def __init__(self, id, movie):
        self.id = id
        if not isinstance(movie, Movie):
            raise TypeError("Debe ser un una Pelicula")
        self.movie = movie
