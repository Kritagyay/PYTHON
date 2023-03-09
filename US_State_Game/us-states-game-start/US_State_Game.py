import turtle
import pandas

data=pandas.read_csv("50_states.csv")


s=turtle.Screen()
s.title("US STATE GAME ")
image="blank_states_img.gif"

s.addshape(image)
turtle.shape(image)

state_list=data["state"].to_list()


total_states=50
guess_states=[]
while len(guess_states)<50:
    answer = s.textinput(title=f"{len(guess_states)}/{total_states} GUESS THEE STATE",
                         prompt="What's the state name?").title()
    if answer =="Exit":
        missing_state=[states for states in state_list if states not in guess_states]
        data_file=pandas.DataFrame(missing_state)
        data_file.to_csv("State_to_learn.csv")
        break

    if answer in state_list:
        guess_states.append(answer)
        answer_state=data[data.state== answer]
        tim = turtle.Turtle()
        tim.hideturtle()
        tim.pu()
        tim.goto(int(answer_state.x),int(answer_state.y))
        tim.write(answer)
