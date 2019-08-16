from tracker import Tracker
from canvas import Canvas
from scipy.interpolate import interp1d
import time

fg_mul = 0.4
mg_mul = 0.2
bg_mul = 0.1

gapping = 100


class Main(object):

    def __init__(self):
        self.tracker = Tracker()
        self.canvas = Canvas()

    def run(self):
        self.tracker.start()

        while True:
            point = self.tracker.get_last_datapoint()

            self.canvas.setfg(point["pos"][0] * fg_mul + gapping,
                              point["pos"][1] * fg_mul + gapping)
            self.canvas.setmg(point["pos"][0] * mg_mul + gapping,
                              point["pos"][1] * mg_mul + gapping)
            self.canvas.setbg(point["pos"][0] * bg_mul + gapping,
                              point["pos"][1] * bg_mul + gapping)

            self.canvas.draw()
            time.sleep(0.05)

            self.canvas.clear()


# Python wrapper stuff
if __name__ == "__main__":
    main_class = Main()

    main_class.run()
