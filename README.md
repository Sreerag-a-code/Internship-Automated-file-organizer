# Automated File Organizer
Intern id-CITS2715

A beginner-friendly Python project that organizes files in a selected folder by file type. The program uses only Python built-in modules and moves files into category folders automatically.

## Objective

The goal is to create a simple tool that helps users keep their folders tidy. The script reads all files in a folder, detects each file type, creates category folders when needed, and moves files into the correct folder.

## Features

- Prompts the user for a folder path
- Validates that the folder exists
- Reads files in the selected folder
- Skips directories and only processes files
- Detects file extension and maps it to a category
- Supports these categories:
  - Images
  - Documents
  - Audio
  - Videos
  - Archives
  - Scripts
  - Applications
  - Others
- Automatically creates missing folders
- Handles duplicate file names by adding `_1`, `_2`, `_3`, etc.
- Prints clear messages during processing
- Displays a final summary

## Technologies Used

- Python 3
- `pathlib` (for working with file paths)
- `shutil` (for moving files)

## Project Structure

```
Automated File Organizer/
├── organizer.py
├── README.md
├── requirements.txt
└── .gitignore
```

## Setup Instructions

1. Open VS Code.
2. Open the project folder: `c:\Users\srana\OneDrive\Desktop\Auomated file`
3. Create the following files if they do not already exist:
   - `organizer.py`
   - `README.md`
   - `requirements.txt`
   - `.gitignore`
4. Copy the code from `organizer.py` into the file.
5. Save the files.

## How to Run

1. Open a terminal in VS Code.
2. Make sure you are in the project folder.
3. Run the script with:

```bash
python organizer.py
```

4. Type or paste the full folder path you want to organize.

## Sample Example

If your folder contains:

- `photo.jpg`
- `song.mp3`
- `report.pdf`
- `script.py`
- `archive.zip`

After running the program, the folder will contain:

- `Images/photo.jpg`
- `Audio/song.mp3`
- `Documents/report.pdf`
- `Scripts/script.py`
- `Archives/archive.zip`

## Expected Output

The program prints messages like:

- "Created folder: Images"
- "Moved: photo.jpg -> Images/photo.jpg"
- "Organization complete."
- "Files moved: 5"
- "Items skipped (folders only): 0"

## Future Scope

Possible improvements for the future:

- Add a graphical user interface (GUI)
- Allow organizing nested folders recursively
- Add a configuration file for custom categories
- Include progress display for large folders

## GitHub Friendly Notes

- This project uses only built-in Python modules.
- The code is written for beginners, with clear function names and comments.
- The repository is ready for version control and sharing.
