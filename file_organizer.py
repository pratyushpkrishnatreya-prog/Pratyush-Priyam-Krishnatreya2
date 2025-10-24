import time
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

TRACKED_PATH = "/path/to/your/downloads/folder"

FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".rtf"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".flv"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "SetupFiles": [".exe", ".dmg", ".pkg"],
    "Spreadsheets": [".xlsx", ".xls", ".csv"],
}

class FileOrganizer(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(TRACKED_PATH):
            file_path = os.path.join(TRACKED_PATH, filename)
            if os.path.isdir(file_path) or filename == os.path.basename(__file__):
                continue

            file_extension = os.path.splitext(filename)[1].lower()

            moved = False
            for category, extensions in FILE_CATEGORIES.items():
                if file_extension in extensions:
                    destination_folder = os.path.join(TRACKED_PATH, category)
                    self.move_file(file_path, destination_folder)
                    moved = True
                    break
            
            if not moved and file_extension:
                destination_folder = os.path.join(TRACKED_PATH, "Others")
                self.move_file(file_path, destination_folder)

    def move_file(self, source_path, destination_folder):
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
        
        filename = os.path.basename(source_path)
        destination_path = os.path.join(destination_folder, filename)
        
        base, ext = os.path.splitext(filename)
        counter = 1
        while os.path.exists(destination_path):
            new_filename = f"{base}({counter}){ext}"
            destination_path = os.path.join(destination_folder, new_filename)
            counter += 1

        shutil.move(source_path, destination_path)


if __name__ == "__main__":
    event_handler = FileOrganizer()
    observer = Observer()
    observer.schedule(event_handler, TRACKED_PATH, recursive=False)
    observer.start()
    
    print(f"File organizer is now running and monitoring: {TRACKED_PATH}")
    print("Press Ctrl+C to stop.")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("\nFile organizer has been stopped.")
    observer.join()
