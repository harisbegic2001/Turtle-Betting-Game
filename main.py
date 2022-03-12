from  turtle import  Turtle, Screen
import random as r
is_race_on = False

colors = ["purple", "red", "blue", "orange"]
pozicija = 100
kornjace = []
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
print()
for i in range(len(colors)):
    kornjaca = Turtle(shape="turtle")
    kornjaca.color(colors[i])
    kornjaca.penup()
    kornjaca.goto(x=-240, y=pozicija)
    kornjaca.speed(r.randint(1,3))
    kornjace.append(kornjaca)
    pozicija-=50

if user_bet:
    is_race_on = True

while is_race_on:

    for i in kornjace:
        if i.xcor() > 230:
            is_race_on = False


            if i.pencolor() == user_bet:
                print(f"You won!! {i.pencolor()} won")

            else:
                print(f"You lost, {i.pencolor()} won")

        i.forward(r.randint(0,10))



screen.exitonclick()






















#def move_forward():
    #tim.forward(10)

#def move_backwards():
    #tim.back(10)

#def turn_left():
    #tim.left(10)

#def turn_right():
    #tim.right(10)

#def clear():
 #   tim.clear()
#screen = Screen()

#screen.listen()
#screen.onkeypress(key="w", fun=move_forward)
#screen.onkeypress(key="s", fun=move_backwards)
#screen.onkeypress(key="a", fun=turn_left)
#screen.onkeypress(key="d", fun=turn_right)
#screen.onkey(key="c", fun=clear)
#screen.exitonclick()