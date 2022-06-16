############################################# 
#      TURTLE EXAMPLE GRAPHICS DEMO         #
#                                           #
#             BY GREENFLY39                 #
#                                           #
#############################################

# IMPORTS TURTLE

import turtle

# IMPORTS ALL FUNCTIONS FROM TURTLE

from turtle import *

# DEFINES COLOURS

color('orange')

# BEGINS FILL

begin_fill()

# SETS WINDOW SIZE

sc = turtle.Screen()
sc.setup(512,384)
screen = turtle.Screen()
# ...
screen.cv._rootwindow.resizable(False, False)

# SETS WINDOW TITLE

turtle.title("Turtle Example Graphics Demo")

# BEGINS LOOP

while True:

    # MOVES PEN
    
    forward(100)
    left(65)
done()