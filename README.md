# Folder-Organizer

# 📁 VGT Organizer - Automatic & Manual File Organizer

## 🚀 Overview

I'm tired of the mess of files in my video editing folder! So I solved it with Python! This project that offers a dual solution to this common problem. It can perform a one-time cleanup of an entire directory or actively monitor a folder in real-time, automatically moving new files to their correct subdirectories.

This project was built to showcase practical automation and file manipulation skills in Python, with a strong focus on robust, real-world error handling.

## ✨ Features

- **Dual Operation Modes:**
    - **`button.py` (Manual Mode):** A script that runs once to perform a complete cleanup of an existing directory.
    - `watcher.py` (Watcher Mode): A service that runs in the background, monitoring a directory and organizing files the moment they are created.
- **Intelligent Audio Sorting:** Uses file metadata to differentiate between short **Sound Effects (SFX)** and long **Music** files, instead of relying only on extensions.
- **Keyword-Based Video Sorting:** Identifies and separates "Green Screen" videos into a dedicated folder by checking their filenames.
- **Robust & Resilient:**
    - **Retry Logic:** Handles `PermissionError` (file is still in use) by waiting and retrying the move operation multiple times.
    - **Debouncing:** Prevents issues with duplicate file system events by implementing a short-term memory to process each file only once.
    - **Safe by Default:** Will not overwrite existing files in the destination.

## 🛠️ Technologies Used

- Python 3.x
- **`pathlib`:** For modern, object-oriented file system path manipulation.
- **`shutil`:** For high-level file operations (moving files).
- **`mutagen`:** For reading audio file metadata (duration).
- **`watchdog`:** For monitoring real-time file system events.

## ⚙️ How to Use

### Prerequisites

- Python 3.7+
- Basic command-line knowledge.

### Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/veetgt/Folder-Organizer.git](https://github.com/veetgt/Folder-Organizer.git)
    cd Folder-Organizer
    ```
2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    # On Windows:
    .\venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```
3.  **Install dependencies from `requirements.txt`:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Configure the Target Folder:**
    Open the `.py` script you want to use and modify the `TARGET_PATH` variable to point to the directory you wish to organize.

### Running the Scripts

#### Manual Mode

To organize all existing files in the target folder at once, run:
```bash
python organizer.py
