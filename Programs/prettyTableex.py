# #By creating a new object called "tom" we're able to use the imported turtle class object as a blueprint
# import turtle
# tom = turtle.Turtle()
# print(tom)
#
# #Alternative form of the above as we are specifiying which class we're trying to call from the module we imported
# from turtle import Turtle, Screen
# tim = Turtle()
# print(tim)
#
# #Changed the shape of our tim object to a turtle this info can be found on the turtle graphics library
# tim.shape("turtle")
# tim.color("blue", "red")
# tim.forward(100)
#
#
# #This section is showing how attributes can be accessed by our newly made objects in this case we are accesses the the screen attribute of the turtle module which would display a screen, but in our example we're just getting the height and width of the screen itself and printing it
# my_screen= Screen()
# print(my_screen.canvwidth)
# print(my_screen.canvwidth)
# my_screen.exitonclick()
#
#
from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Charamander", "Squirtle"])
table.add_column("Type", ["Electric", "Fire", "Water"])
table.align = 'l'
print(table)