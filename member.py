from actor import Actor
"""
Class Member
"""


class Member:
    def __init__(self, name, adress, phone, id):
        self.id = id
        self.name = name
        self.adress = adress
        self.phone = phone


class preferences:
    actors = []

    def __init__(self, Member):
        self.list = list
        self.member = Member
        # self.actor = list

    def add_to_list(self, Actor):
        self.actors.append(Actor)

    def delete_from_list(self, Movie_tape):
        self.actors.remove(Movie_tape)
