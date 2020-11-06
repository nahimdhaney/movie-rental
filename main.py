from order import Order
from stack_movies import Rented_movies, Available_movies, Returned_movies
from movie_tape import Movie_tape
from movie import Movie
from member import Member
from waiting_list import Waiting_list
# instance = Order(name="nahim")
# print(instance.name)
rente_mov = Available_movies()
nahim = Member("Nahim", "Av. Luis Saavedra Suarez", "74673131", "1")
esperador = Member("Esperador 1", "Av. Luis Saavedra Suarez", "74673131", "1")
movie = Movie("Avatar", "George Br.")
cinta = Movie_tape("id-1", movie)
cinta2 = Movie_tape("id-2", movie)
rente_mov2 = Available_movies()
rente_mov.add_to_list(cinta)
rente_mov.add_to_list(cinta2)
print("rente_mov -" + rente_mov.list[0].id)
Order(nahim, "2020/11/06", movie)
prestado = Order(nahim, "2020/11/06", movie)
Order(esperador, "2020/11/06", movie)
# Order(nahim, "2020/11/06", movie)
returned = Returned_movies()
waiting_list = Waiting_list()
returned.attach(waiting_list)
len(waiting_list.list)
returned.add_to_list(prestado.tape)
