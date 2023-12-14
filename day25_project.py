import pandas
import turtle

screen =  turtle.Screen()
screen.title("U.S States Games")
image = "./us_states_files/blank_states_img.gif"
screen.setup(width = 800, height = 500)
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("./us_states_files/50_states.csv")
all_states = data.state.to_list()

guessed_states = []
data_length = len(data)

while len(guessed_states) < 50:
    user_answer_state = screen.textinput(title=f"{len(guessed_states)}/{data_length} States Correct", prompt= "What's another state's name?" )
    user_answer_state= user_answer_state.title()
    state_data = data[data.state == user_answer_state]
    if user_answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("./us_states_files/states_to_learn.csv")
        break
    if user_answer_state in all_states and user_answer_state not in guessed_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup() 
        t.goto(int(state_data.x),int(state_data.y))
        t.write(user_answer_state)
        guessed_states.append(user_answer_state)




# screen.exitonclick()


# def get_mouse_click_coor(x,y):
#     print(x,y)

# turtle.onscreenclick(get_mouse_click_coor)

# turtle.mainloop()