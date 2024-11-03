import turtle
import pandas

screen = turtle.Screen()
screen.title("INDIA. States and Union Teritory Game")
image = "indian.gif"
screen.addshape(image)
turtle.shape(image)
screen.setup(width=600, height=600) 

# def get_mouse_click(x,y):
#     print(x,y)

# turtle.onscreenclick(get_mouse_click)
# turtle.mainloop()
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/37 States or UT Correct",
                                    prompt="What's another state's name?").title()
    
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        
        # Create a new turtle for each guessed state
        marker = turtle.Turtle()
        marker.hideturtle()
        marker.penup()
        
        # Get the coordinates of the state
        state_data = data[data.state == answer_state]
        x, y = state_data.x.item(), state_data.y.item()
        
        # Place a small dot on the state location
        marker.goto(x, y)
        marker.dot(5, "red")  # Create a red dot as the point
        
        # Write the state name next to the dot
        marker.write(answer_state, align="left", font=("Arial", 8, "normal"))
