# Mapping cities
import turtle

screen = turtle.Screen()

# this assures that the size of the screen will match the map image:
#screen.setup(1000, 600)

#Set coordinates for latitude and longitude:
#screen.setworldcoordinates(-740.5, 405, -738.7, 408)
# ... which is the same size as our image
# now set the background to our space image
#screen.bgpic("nycMap.jpg")


teddy = turtle.Turtle()
teddy.shape('circle')
teddy.color('red')
teddy.penup()


#Go to Hunter:
teddy.color("purple")
teddy.goto(-739.64,407.68)
teddy.stamp()

#Go to ESB
teddy.color('blue')
teddy.goto(-739.85664, 407.48441)
teddy.stamp()
