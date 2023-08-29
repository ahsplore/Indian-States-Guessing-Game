import turtle
import pandas

screen = turtle.Screen()
screen.title("Indian States Game")
image = "india_map.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("Indian_States_Coordinates .csv")
states = data.State.to_list()
num = 0
while num < 30:
    ans = screen.textinput(title=f" {num}/29 Guess the State", prompt="Enter State:").title()
    if ans in states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.pencolor("black")
        state_loc = data[data.State == ans]
        t.goto(int(state_loc.x), int(state_loc.y))
        t.write(ans)
        num += 1

# screen.exitonclick()
