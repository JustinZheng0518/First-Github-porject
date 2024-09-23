from turtle import Turtle, Screen
import random

total_golds = 100


def game():
    global total_golds
    color_list = ["red", "orange", "yellow", "green", "blue", "purple"]
    turtle1 = Turtle()
    turtle1.color(color_list[0])
    turtle1.penup()
    turtle1.shape("turtle")

    turtle2 = Turtle()
    turtle2.color(color_list[1])
    turtle2.penup()
    turtle2.shape("turtle")

    turtle3 = Turtle()
    turtle3.color(color_list[2])
    turtle3.penup()
    turtle3.shape("turtle")

    turtle4 = Turtle()
    turtle4.color(color_list[3])
    turtle4.penup()
    turtle4.shape("turtle")

    turtle5 = Turtle()
    turtle5.color(color_list[4])
    turtle5.penup()
    turtle5.shape("turtle")

    turtle6 = Turtle()
    turtle6.color(color_list[5])
    turtle6.penup()
    turtle6.shape("turtle")

    turtle_list = [turtle1, turtle2, turtle3, turtle4, turtle4, turtle5, turtle6]

    screen = Screen()
    screen.setup()

    screen.setup(width=500, height=300)

    turtle1.goto(x=-230, y=-75)
    turtle2.goto(x=-230, y=-45)
    turtle3.goto(x=-230, y=-15)
    turtle4.goto(x=-230, y=15)
    turtle5.goto(x=-230, y=45)
    turtle6.goto(x=-230, y=75)

    user_guess = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color")
    user_bet = screen.numinput(title="Make your bet", prompt="How many golds do you wanna bet on your chosen turtle",
                                                             minval=1, maxval=total_golds)

    while turtle1.xcor() <= 215 and turtle2.xcor() <= 215 and turtle3.xcor() <= 215 and turtle4.xcor() <= 215 and\
            turtle5.xcor() <= 215 and turtle6.xcor() <= 215:
        steps1 = random.randint(2, 8)
        steps2 = random.randint(2, 8)
        steps3 = random.randint(2, 8)
        steps4 = random.randint(2, 8)
        steps5 = random.randint(2, 8)
        steps6 = random.randint(2, 8)

        turtle1.forward(steps1)
        turtle2.forward(steps2)
        turtle3.forward(steps3)
        turtle4.forward(steps4)
        turtle5.forward(steps5)
        turtle6.forward(steps6)

    winner = "0"
    wining_pos = 0
    for candidate in turtle_list:
        if candidate.xcor() > wining_pos:
            winner = candidate.pencolor()
            wining_pos = candidate.xcor()

    if user_guess == winner:
        print(f"You win. The winner is the {winner} one")
        total_golds += user_bet
        print(total_golds)
    else:
        print(f"You lose. The winner is the {winner} one")
        total_golds -= user_bet
        print(total_golds)

    if total_golds <= 0:
        print("You are run out of golds. You lose.")
    elif total_golds >= 150:
        print("You have doubled your golds. You win.")


while 0 < total_golds < 150:
    game()
