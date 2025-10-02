from organizer_system import organizer
from pathlib import Path

messy_folder_path       = "D:/veeticas"                     # source folder that you want to organize


sfx_folder_path         = "D:/veeticas/Sound Effects (SFX)" # sfx folder, if you have one
music_folder_path       = "D:/veeticas/Musics"              # music folder, if you have one
video_folder_path       = "D:/veeticas/Videos"              # videos folder, if you have one
greenscreen_folder_path = "D:/veeticas/green screen"        # green screen folder, if you have one
images_folder_path      = "D:/veeticas/Images"              # images folder, if you have one
psd_folder_path         = "D:/veeticas/PSD"                 # .psd folder, if you have one

if __name__ == "__main__":
    for item in Path(messy_folder_path).iterdir():
        if not item.is_file():
            continue
        fileName = item.name
        fileExtension = item.suffix.lower()
        destinationPath = None
        organizer(messy_folder_path, 
                        sfx_folder_path,
                        music_folder_path,
                        video_folder_path,
                        greenscreen_folder_path,
                        images_folder_path,
                        psd_folder_path)