from turtle import Turtle

score = 0
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(x=0,y=270)

    def update_score(self):
        self.clear()
        text= f"Score : {score}"
        self.write(text,align='center',font=("'Arial",13,'normal'))

    def increase_score(self):
        global score
        score+=1
        self.update_score()

    def game_over(self):

        self.goto(x=0,y=0)
        self.write(arg="GAME OVER",font=('arial',24,'bold'),align='center')