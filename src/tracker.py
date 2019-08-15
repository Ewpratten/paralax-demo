import cv2
from threading import Thread


class Tracker:

    running = True
    last_datapoint = {
        "pos": (0, 0),
        "width": 0
    }

    def __init__(self, cam_id=0, casc_file="./classifier.xml"):
        self.cam = cv2.VideoCapture(cam_id)
        self.casc = cv2.CascadeClassifier(casc_file)

    def _threaded_runner(self):

        while self.running:
            _, frame = self.cam.read()

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = self.casc.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
                flags=cv2.CASCADE_SCALE_IMAGE
            )

            faces = sorted(faces, key=lambda x: x[2] * x[3])

            if faces:
                (x, y, w, h) = faces[0]

                self.last_datapoint = {
                    "pos": (x, y),
                    "width": w 
                }
            else:
                self.last_datapoint = {
                    "pos": (0,0),
                    "width": 0
                }

        self.cam.release()
        cv2.destroyAllWindows()

    def start(self):
        self.runner_thread = Thread(target=self._threaded_runner)
        self.running = True
        self.runner_thread.start()

    def stop(self):
        self.running = False

    def get_last_datapoint(self):
        return self.last_datapoint
