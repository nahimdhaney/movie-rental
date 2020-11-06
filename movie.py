
"""
Class Movie
"""


class Movie:
    def __init__(self, title, director):
        self.title = title
        self.director = director

    def __str__(self):
        return self.title
