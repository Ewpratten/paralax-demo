from graphics import *


class Canvas(object):

    def __init__(self):
        self.win = GraphWin("My Circle", 800, 600)
        self.fg = Circle(Point(50, 50), 10)
        self.mg = Circle(Point(50, 50), 10)
        self.bg = Circle(Point(50, 50), 10)

    def setfg(self, x, y):

        self.fg = Circle(Point(x, y), 100)

    def setmg(self, x, y):

        self.mg = Circle(Point(x, y), 100)

    def setbg(self, x, y):

        self.bg = Circle(Point(x, y), 100)

    def draw(self):
        self.fg.draw(self.win)
        self.mg.draw(self.win)
        self.bg.draw(self.win)

    def clear(self):
        self.fg.undraw()
        self.mg.undraw()
        self.bg.undraw()
