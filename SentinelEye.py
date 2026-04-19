import time 
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import sys

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print(f"[+] File modified on {event.src_path}")
    
    def on_deleted(self, event):
        print(f"[+] File Deleted from {event.src_path}")
    
    def on_created(self, event):
        print(f"[+] File created on {event.src_path}")
    
    def on_moved(self, event):
        print(f"[+] File moved from {event.src_path}")
    
    def on_opened(self, event):
        print(f"[+] File opened ! {event.src_path}")
    
    def on_closed(self, event):
        print(f"[+] File closed ! {event.src_path}")
    
    def on_closed_no_write(self, event):
        print(f"[+] File Closed without any change {event.src_path}")
    
    def on_any_event(self, event):
        print(f"[!] Event {event}")


if __name__ == "__main__":

    path = "."

    event_handler = MyHandler()
    observer  = Observer()
    observer.schedule(event_handler,path,recursive=False)
    observer.start()
    print(f"[+] Monitoring started on: {path}...")
    try:
        while True:
            time.sleep(1)
    except:
        observer.stop()
    observer.join()