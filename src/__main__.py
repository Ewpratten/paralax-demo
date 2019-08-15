from tracker import Tracker
import time

class Main(object):

    def __init__(self):
        self.tracker = Tracker()

    def run(self):
        self.tracker.start()

        while True:
            # print(self.tracker.get_last_datapoint())
            time.sleep(1)

# Python wrapper stuff
if __name__ == "__main__":
    main_class = Main()

    main_class.run()
