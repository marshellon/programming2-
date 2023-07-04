import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from drawer import Drawer

class DataFileHandler(FileSystemEventHandler):
    def __init__(self):
        super().__init__()

    def on_created(self, event):
        if not event.is_directory:
            filename = event.src_path
            self.process_file(filename)

    def process_file(self, filename):
        # part of the code that processes the filepath
        filename = filename.replace('\\', '/' )      
        print(f"new loading data: {filename}")
        Drawer(filename) # This is the juice
        time.sleep(20) # Sleeping to let the drawer finish the data before deleting the troep :)


class DataFileMonitor:
    def __init__(self, directory):
        self.directory = directory
        self.event_handler = DataFileHandler()
        self.observer = Observer()

    def start(self):
        self.observer.schedule(self.event_handler, self.directory, recursive=False)
        self.observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.observer.stop()
        self.observer.join()


# running the program
if __name__ == "__main__":
    directory_to_monitor = "C:/Users/marsh/Desktop/programming2/week 2.7/data"
    monitor = DataFileMonitor(directory_to_monitor)
    monitor.start()
