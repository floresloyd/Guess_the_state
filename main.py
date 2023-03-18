import turtle
import pandas
from statename import StateName
# GUI
screen = turtle.Screen()
screen.title("Name The States!")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.setup(725, 490)
# Accessing CSV Data Using Pandas
data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
score = 0
guessed_states = []

while len(guessed_states) > 50:
    user_answer = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state?").title()
    if user_answer in states:
        guessed_states.append(user_answer)
        score += 1
        state_coordinates = data[data.state == user_answer]
        state_popup = StateName(user_answer, int(state_coordinates.x), int(state_coordinates.y))