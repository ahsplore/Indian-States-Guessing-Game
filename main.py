import turtle
import pandas

screen = turtle.Screen()
screen.title("Indian States Game")
image = "india_map.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("Indian_States_Coordinates .csv")
states = data.State.to_list()
guessed_states = []

while len(guessed_states) < 30:
    ans = screen.textinput(title=f" {len(guessed_states)}/29 Guess the State", prompt="Enter State:").title()
    if ans=="Exit":
        missing_states = []
        for state in states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("States_To_Learn.csv")
        break
    if ans in states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.pencolor("black")
        state_loc = data[data.State == ans]
        t.goto(int(state_loc.x), int(state_loc.y))
        t.write(ans)

# screen.exitonclick()
