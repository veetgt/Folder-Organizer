from pathlib import Path
import shutil
from mutagen import File

def organizer(messy_folder_path, sfx_folder_path, music_folder_path, video_folder_path, greenscreen_folder_path, images_folder_path, psd_folder_path):
    
    messy_folder_path = Path(messy_folder_path)
    sfx_folder_path = Path(sfx_folder_path)
    music_folder_path = Path(music_folder_path) 
    video_folder_path = Path(video_folder_path)
    greenscreen_folder_path = Path(greenscreen_folder_path)
    images_folder_path = Path(images_folder_path)
    psd_folder_path = Path(psd_folder_path)

    SFX_MAX_DURATION_SECONDS = 60
    FILE_TYPES = {
        "Audio": [".mp3", ".ogg", ".wav"],
        "Videos": [".mp4", ".m4a", ".webm"],
        "Green Screen": [".mp4", ".webm"],
        "Images": [".png", ".jpg", ".jpeg", ".gif", ".webp"],
        "PSD": [".psd"]
    } 

    for item in messy_folder_path.iterdir():
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
            finalDestination = images_folder_path

        elif destinationPath == "PSD":
            finalDestination = psd_folder_path

        elif destinationPath == "Audio":
            try:
                audioFile = File(item) 
                duration = float(audioFile.info.length) 
                if duration <= SFX_MAX_DURATION_SECONDS:
                    finalDestination = sfx_folder_path
                else:
                    finalDestination = music_folder_path
            except Exception as e:
                print(f"Could not read metadata from '{item.name}'. Moving to Music by default.")
                finalDestination = music_folder_path

        fileNameLower = fileName.lower()
        if destinationPath == "Videos" and ("greenscreen" in fileNameLower or "green screen" in fileNameLower or "fundo verde" in fileNameLower):
            finalDestination = greenscreen_folder_path
        else:
            if destinationPath == "Videos":
                finalDestination = video_folder_path

        finalDestination.mkdir(exist_ok=True)
        destinationFile = finalDestination / item.name
        if not destinationFile.exists():
            print(f"Moving '{item.name}' to '{finalDestination}' folder...")
            shutil.move(str(item), str(finalDestination))
        else:    
            print(f"Arquivo '{item.name}' ja existe em '{finalDestination}'. Pulando.")