from movies_list import Movies_list
from singleton import SingletonMeta
from observer import Subject, Observer
from random import randrange
from typing import List
from movie_tape import Movie_tape


class Rented_movies(Movies_list, metaclass=SingletonMeta):
    pass


class Available_movies(Movies_list, metaclass=SingletonMeta):
    pass


class Returned_movies(Movies_list, metaclass=SingletonMeta):
    # pass
    """
    The Subject owns some important state and notifies observers when the state
    changes.
    """

    _state: int = None
    """
    For the sake of simplicity, the Subject's state, essential to all
    subscribers, is stored in this variable.
    """

    _observers: List[Observer] = []
    """
    List of subscribers. In real life, the list of subscribers can be stored
    more comprehensively (categorized by event type, etc.).
    """

    def attach(self, observer: Observer) -> None:
        print("Subject: Attached an observer.")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    """
    The subscription management methods.
    """

    def notify(self, Movie_tape) -> None:
        """
        Trigger an update in each subscriber.
        """

        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update(self, Movie_tape)

    def add_to_list(self, Movie_tape) -> None:
        if Movie_tape not in self.list and (Movie_tape.movie.title + Movie_tape.id not in self.get_movies()):
            self.list.append(Movie_tape)
            # print("llega")
            self.notify(Movie_tape)
        else:
            raise TypeError("Movie tape already included")

    def some_business_logic(self) -> None:
        """
        Usually, the subscription logic is only a fraction of what a Subject can
        really do. Subjects commonly hold some important business logic, that
        triggers a notification method whenever something important is about to
        happen (or after it).
        """

        # print("\nSubject: I'm doing something important.")
        # self._state = randrange(0, 10)

        # print(f"Subject: My state has just changed to: {self._state}")
        # self.notify()
