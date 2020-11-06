"""
Class Order
"""
from member import Member
from stack_movies import Available_movies, Rented_movies, Returned_movies
from waiting_list import Waiting_list


class Order:

    def __init__(self, member, date, movie):
        self.member = member
        self.movie = movie
        self.status = 1
        self.date = date
        if len(Available_movies().stock_of_movie(movie)) == 0:
            print("NO DISPONIBLE")
            self.status = 2
            Waiting_list().add_to_list(self)
        else:
            print("Movie DISPONIBLE con cantidad " +
                  str(len(Available_movies().stock_of_movie(movie))))
            tape = Available_movies().get_by_movie(movie)  # Getting from Availables
            Available_movies().delete_from_list(tape)
            self.tape = tape

    def accept_movie(self, tape):
        Rented_movies().add_to_list(tape)  # Adding
        self.tape = tape
        self.status = 1
    # status 1 accepted | 2 waiting | 3 finished.
