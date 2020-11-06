from singleton import SingletonMeta
from observer import Subject, Observer
from stack_movies import Available_movies, Returned_movies, Rented_movies


class Waiting_list(metaclass=SingletonMeta):
    """
    Waiting List
    """
    __metaclass__ = Observer
    # lista = LifoQueue(maxsize=200000)
    # list = []

    def __init__(self):
        self.list = []

    def add_to_list(self, order):
        print("Nuevo en la lista" + order.member.name)
        self.list.append(order)  # list of orders which has status unatended

    def update(self, devueltos: Subject, Movie_tape) -> None:
        # se notifica caso la pelicula entrante alguien este esperando
        print(len(self.list))
        first_waiting = self.request_movie(Movie_tape.movie)
        print("Llega " + Movie_tape.id)
        print("ESTABA ESPERANDO  " + first_waiting.member.name)
        if first_waiting is not None:
            picked_movie = Returned_movies().get_by_movie(Movie_tape.movie)
            # print(borrado)
            self.list.remove(first_waiting)  # no is not waiting
            first_waiting.accept_movie(picked_movie)
            print("Se dio la pelicula " + picked_movie.id +
                  " al usuario " + first_waiting.member.name)
            Returned_movies().delete_from_list(picked_movie)

    def request_movie(self, movie):
        for order in self.list:
            print("BUSCA " + order.date)
            if order.movie == movie:
                return order
        return None
