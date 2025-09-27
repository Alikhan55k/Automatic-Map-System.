from turtle import Turtle,Screen
import pandas
from Day25_Scoreboard import Scoreboard
screen = Screen()
turtle = Turtle()
score = 0
image= "US_States/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.title("Us States")
data=pandas.read_csv("US_States/50_states.csv")
states_list=data["state"].to_list()

for rep in range(0,len(data)):
    scoreboard = Scoreboard(score)
    Ans= False
    state=screen.textinput("state","Write name of a state: ")
    for a in states_list:
        if a==state:
            Ans=True
    if Ans:
        row=data[data["state"]==state]
        x= row["x"]
        y= row["y"]
        turtle2=Turtle()
        turtle2.penup()
        turtle2.hideturtle()
        turtle2.goto(int(x), int(y))
        turtle2.write(state, align="center", font=("Arial", 15, "normal"))
        score += 1


    elif state=="":
        break
    scoreboard.increase(score)


screen.exitonclick()
