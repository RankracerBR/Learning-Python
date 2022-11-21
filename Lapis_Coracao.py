import turtle  #Desenhar

lapis = turtle.Turtle()

def curva():
    for i in range(200):
        lapis.right(1)
        lapis.forward(1)
def coracao():
     lapis.fillcolor('blue')
     lapis.begin_fill()
     lapis.left(140)
     lapis.forward(113)
     curva()
     lapis.left(120)
     curva()
     lapis.forward(113)
     lapis.end_fill()       
def texto():
    lapis.up()
    lapis.setpos(-68,95)
    lapis.down()
    lapis.color('yellow')
    lapis.write('Te amo :3')

coracao()
texto()
lapis.ht()