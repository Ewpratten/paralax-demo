import cv2
from threading import Thread


class Tracker:

    running = True
    last_datapoint = (0, 0)

    def __init__(self, cam_id=0):
        self.cam = cv2.VideoCapture(cam_id)

    def _threaded_runner(self):

        while self.running:

            pass

    def start(self):
        self.runner_thread = Thread(target=self._threaded_runner)
        self.running = True
        self.runner_thread.start()

    def stop(self):
        self.running = False

    def get_last_datapoint(self):
        return self.last_datapoint
