import os
import sys
import time
import psutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class ReloadHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith(".py") or event.src_path.endswith(".kv"):
            print("Zmieniono plik, restartuję aplikację...")

            # Zamknięcie starej instancji aplikacji
            for proc in psutil.process_iter():
                if "python" in proc.name().lower():
                    proc.terminate()

            # Uruchomienie nowej instancji
            os.execv(sys.executable, ['python', 'main.py'])

if __name__ == "__main__":
    path = os.getcwd()
    event_handler = ReloadHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()