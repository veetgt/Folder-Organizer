from pathlib import Path
import shutil
from mutagen import File
import watchdog.events
from watchdog.observers import Observer
import time

veeticas_path = Path("D:/veeticas")

FILE_TYPES = {
   "Audio": [".mp3", ".ogg", ".wav"],
   "Videos": [".mp4", ".m4a", ".webm"],
   "Green Screen": [".mp4", ".webm"],
    "Images": [".png", ".jpg", ".jpeg", ".gif", ".webp"],
    "PSD": [".psd"]
}

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
                fileName =  item.name
                fileExtension = item.suffix.lower()
                destinationPath = None

                for category, extensions in FILE_TYPES.items():
                    if fileExtension in extensions:
                        destinationPath = category
                        break 
                if not destinationPath:
                    return

                if destinationPath == "Images":
                    finalDestination = "Images"

                if destinationPath == "PSD":
                    finalDestination = "PSD"

                if destinationPath == "Audio":
                    try:
                        audioFile = File(item) 
                        duration = float(audioFile.info.length) 
                        if duration <= SFX_MAX_DURATION_SECONDS:
                            finalDestination = "Sound Effects (SFX)"
                        else:
                            finalDestination = "Musics"
                    except Exception as e:
                        print(f"Could not read metadata from '{item.name}'. Moving to Music by default.")
                        finalDestination = "Musics"

                fileNameLower = fileName.lower()
                if destinationPath == "Videos" and ("greenscreen" in fileNameLower or "green screen" in fileNameLower or "fundo verde" in fileNameLower):
                    finalDestination = "Green Screen"
                else:
                    if destinationPath == "Videos":
                        finalDestination = "Videos"

                destinationFolder = veeticas_path / finalDestination
                destinationFolder.mkdir(exist_ok=True)
                destinationFile = destinationFolder / item.name
                if not destinationFile.exists():
                    print(f"Moving '{item.name}' to '{finalDestination}' folder...")
                    shutil.move(str(item), str(destinationFolder))
                else:    
                    print(f"Arquivo '{item.name}' ja existe em '{finalDestination}'. Pulando.")
            except PermissionError:
                print(f"Arquivo '{item.name}' ainda esta em uso. Tentando novamente em {WAIT_SECONDS} segundos...")
            except Exception as e:
                print(f"Erro inesperado ao processar '{item.name}': {e}")
                break 

if __name__ == "__main__":
    event_handler = FileOrganizerHandler()
    observer = Observer()
    observer.schedule(event_handler, str(veeticas_path), recursive=False)
    observer.start()
    print(f"Auto-sort enabled in folder: {veeticas_path}")
    print("Press Ctrl+C to stop.")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        # Ctrl+C to stop the program.
        print("Vigilancia encerrada pelo usuario.")
        observer.stop()
    observer.join()
