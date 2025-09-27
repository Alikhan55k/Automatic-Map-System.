# yah tarika ham nay parha aik column ko leny ky liay itna bara code acha ni

# import csv
# file=open("C:/Users/IT LAND/Desktop/Ali/Python is my Love/weather/weather.csv",'r')
# data=csv.reader(file)
# temperatures=[]
# i=0
# for row in data:
#     if i!=0:
#         temperatures.append(int(row[1]))
#     i=i+1
# print(temperatures)



# is liay ham help lain gay Pandas ki this is super helpful laburary  for data analysis
# import pandas
# data=pandas.read_csv("C:/Users/IT LAND/Desktop/Ali/Python is my Love/squirrels/004 2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")
# gray_fur= data[data["Primary Fur Color"] == 'Gray']
# list_gray= gray_fur["Primary Fur Color"].to_list()
# print(len(list_gray))
# Cinnamon_fur= data[data["Primary Fur Color"] == 'Cinnamon']
# list_Cinnamon=Cinnamon_fur['Primary Fur Color'].to_list()
# print(len(list_Cinnamon))
# Black_fur= data[data["Primary Fur Color"] == 'Black']
# list_Black=Black_fur["Primary Fur Color"].to_list()
# print(len(list_Black))
# new_dict={
#     "fur":['Gray','Red','Black'],
#     "No":[len(list_gray),len(list_Cinnamon),len(list_Black)],
# }
# Squirrels_count=pandas.DataFrame(new_dict)
# Squirrels_count.to_excel("C:/Users/IT LAND/Desktop/Ali/Python is my Love/squirrels/Squirrels_count.xlsx")
from turtle import Turtle,Screen
import pandas
from Day25_Scoreboard import Scoreboard
screen = Screen()
turtle = Turtle()
score = 0
image= "C:/Users/IT LAND/Desktop/Ali/Python is my Love/US_States/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.title("Us States")
data=pandas.read_csv("C:/Users/IT LAND/Desktop/Ali/Python is my Love/US_States/50_states.csv")
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