import itertools
import sys
import threading
import time


class Spinner:
    def __init__(self, message="Processing"):
        self.spinner = itertools.cycle(['-', '/', '|', '\\'])
        self.stop_running = False
        self.message = message

    def spin(self):
        while not self.stop_running:
            sys.stdout.write(f"\r{self.message} {next(self.spinner)}")
            sys.stdout.flush()
            time.sleep(0.1)

    def start(self):
        self.stop_running = False
        self.thread = threading.Thread(target=self.spin)
        self.thread.start()

    def stop(self):
        self.stop_running = True
        self.thread.join()
        sys.stdout.write("\r" + " " * len(self.message) + " \r")  # 清除行
        sys.stdout.flush()

    def __del__(self):
        self.stop()
