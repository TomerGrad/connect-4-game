"""
Here will be Dragons
"""
import tkinter as tk
from tkinter.messagebox import askyesno
from turtle import RawTurtle, TurtleScreen
from connect4 import create_board, turn, victory

class Connet4Board(TurtleScreen):
    def __init__(self):
        """
        Here will be puppies
        """
        self.canvas = tk.Canvas(cnf={'width':420, 'height':420})
        super(Connet4Board, self).__init__(self.canvas)
        
        self.slots_positions = [[(x, y) for x in range(-180, 240, 60)] for y in range(120, -210, -60)]
        self.columns = [x for x in range(-180, 240, 60)]
        self.colors = ['red', 'gold']
        self.current_play = 0
        self.player = Player(self, 'red')
        self.player.goto(-180, 180)

        self.bgcolor("blue")
        self.tracer(False)
        self.painter = RawTurtle(self, visible=False)
        self.painter.color("white")
        self.painter.setheading(270)
        self.draw_board()
        self.init_board()

        self.canvas.master.title("Connect4Game")
        self.canvas.pack()

    def draw_board(self):
        """
        here will be puppies
        """
        for x in range(-150, 240, 60):
            self.painter.up()
            self.painter.goto(x, 180)
            self.painter.down()
            self.painter.fd(420)
        self.painter.up()
        self.painter.goto(-210, 210)
        self.painter.down()
        self.painter.begin_fill()
        self.painter.goto(-210, 150)
        self.painter.goto(210, 150)
        self.painter.goto(210, 210)
        self.painter.goto(-210, 210)
        self.painter.end_fill()
        self.update()

    def init_board(self):
        self.painter.color('white')
        for row in self.slots_positions:
            for (x, y) in row:
                self.painter.up()
                self.painter.goto(x, y)
                self.painter.down()
                self.painter.dot(45)
        self.backend = create_board()
        self.player.setx(-180)
        self.player.switch_color('red')

    def move_right(self):
        self.player.move_right()
        self.update()

    def move_left(self):
        self.player.move_left()
        self.update()

    def switch_player(self):
        self.current_play = not self.current_play
        self.player.switch_color(self.colors[self.current_play])
        self.update()

    def slot(self):
        column = self.columns.index(self.player.pos()[0])
        try:
            row, column = turn(self.colors[self.current_play], column, self.backend)
            self.player.goto(self.slots_positions[row][column])
            self.player.dot(45)
            self.player.sety(180)
            if victory(self.backend, (row, column), self.player.c):
                self.player.hideturtle()
                self.painter.up()
                self.painter.goto(-180, 150)
                self.painter.pencolor('black')
                self.painter.write(f"{self.player} is The Winer", font=('David', 24, 'bold'))
                self.update()
                another = askyesno("Play Again", "Do you want to play again?")
                if another:
                    self.painter.undo()
                    self.init_board()
                    self.player.showturtle()
                else:
                    exit()
            else:
                self.switch_player()
        except KeyError:
            pass


class Player(RawTurtle):
    """
    Here will be bunnies
    """
    def __init__(self, screen: Connet4Board, color: str):
        super(Player, self).__init__(screen)
        self.screen = screen
        self.c = color
        self.color(color)
        self.shape('circle')
        self.shapesize(2)
        self.up()

    def __repr__(self):
        return self.c.capitalize() + " player"

    def move_right(self):
        """
        move the colored dot which represents the player to the right.
        if the player already in the rightest position, circle it to the leftest.
        """
        position = self.pos()[0]
        columns = self.screen.columns
        index = columns.index(position)
        if index == len(columns) - 1:
            self.setx(columns[0])
        else:
            self.setx(columns[index+1])

    def move_left(self):
        """
        move the colored dot which represents the player to the left.
        if the player already in the leftest position, circle it to the rightest.
        """
        position = self.pos()[0]
        columns = self.screen.columns
        index = columns.index(position)
        self.setx(columns[index-1])

    def switch_color(self, color: str):
        """
        change the color of the player to color
        :param color: str name of the required color.
        """
        self.c = color
        self.color(color)


board: list = [[' ',' ',' ',' ',' ',' ',' '],
               [' ',' ',' ',' ',' ',' ',' '],
               [' ',' ',' ',' ',' ',' ',' '],
               [' ',' ',' ',' ',' ',' ',' '],
               [' ',' ',' ',' ',' ',' ',' '],
               [' ',' ',' ',' ',' ',' ',' ']]

c = Connet4Board()
c.listen()
c.onkeypress(c.move_right, 'Right')
c.onkeypress(c.move_left, 'Left')
c.onkeypress(c.slot, 'Return')
c.mainloop()

