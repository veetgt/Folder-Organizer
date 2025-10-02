from organizer_system import organizer
from pathlib import Path
import shutil
from mutagen import File
import watchdog.events
from watchdog.observers import Observer
import time

###

messy_folder_path       = "D:/veeticas"                     # source folder that you want to organize


sfx_folder_path         = "D:/veeticas/Sound Effects (SFX)" # sfx folder, if you have one
music_folder_path       = "D:/veeticas/Musics"              # music folder, if you have one
video_folder_path       = "D:/veeticas/Videos"              # videos folder, if you have one
greenscreen_folder_path = "D:/veeticas/green screen"        # green screen folder, if you have one
images_folder_path      = "D:/veeticas/Images"              # images folder, if you have one
psd_folder_path         = "D:/veeticas/PSD"                 # .psd folder, if you have one

# PRESS CTRL+C TO STOP THE PROGRAM

###

class FileOrganizerHandler(watchdog.events.FileSystemEventHandler):
    def on_created(self, event):
        SFX_MAX_DURATION_SECONDS = 60 
        item = Path(event.src_path)
        if not item.is_file():
            return
        
        MAX_ATTEMPTS = 5
        WAIT_SECONDS = 1
        for attempt in range(MAX_ATTEMPTS):
            try:
                time.sleep(WAIT_SECONDS)

                organizer(messy_folder_path, 
                        sfx_folder_path,
                        music_folder_path,
                        video_folder_path,
                        greenscreen_folder_path,
                        images_folder_path,
                        psd_folder_path)
                
            except PermissionError:
                print(f"Arquivo '{item.name}' ainda esta em uso. Tentando novamente em {WAIT_SECONDS} segundos...")
            except Exception as e:
                print(f"Erro inesperado ao processar '{item.name}': {e}")
                break 

if __name__ == "__main__":
    event_handler = FileOrganizerHandler()
    observer = Observer()
    observer.schedule(event_handler, str(messy_folder_path), recursive=False)
    observer.start()
    print(f"Auto-sort enabled in folder: {messy_folder_path}")
    print("Press Ctrl+C to stop.")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        # Ctrl+C to stop the program.
        print("Operation terminated by user.")
        observer.stop()
    observer.join()
