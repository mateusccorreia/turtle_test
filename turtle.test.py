import turtle

slowpoke = turtle.Turtle()
slowpoke.shape('turtle')

def make_square(the_turtle):

    for i in range (0,4):     
        slowpoke.forward(100)
        slowpoke.right(90)

make_square(slowpoke)

turtle.mainloop()
