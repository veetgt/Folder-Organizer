from pathlib import Path
import shutil
from mutagen import File
from watchdog import events, observers
import time

veeticas_path = Path("D:/veeticas")



FILE_TYPES = {
    "Audio": [".mp3", ".ogg", ".wav"],
    "Videos": [".mp4", ".m4a", ".webm"],
    "Green Screen": [".mp4", ".webm"],
    "Images": [".png", ".jpg", ".jpeg", ".gif", ".webp"],
    "PSD": [".psd"]
}


SFX_MAX_DURATION_SECONDS = 60 

for item in veeticas_path.iterdir():
    if not item.is_file():
        continue
    fileName = item.name
    fileExtension = item.suffix.lower()
    destinationPath = None

    for category, extensions in FILE_TYPES.items():
        if fileExtension in extensions:
            destinationPath = category
            break 
    if not destinationPath:
        continue

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

