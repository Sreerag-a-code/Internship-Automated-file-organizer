from pathlib import Path
import shutil

# Define the file categories and the extensions that belong to each category.
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx", ".odt"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".wmv", ".flv"],
    "Archives": [".zip", ".tar", ".gz", ".rar", ".7z", ".bz2"],
    "Scripts": [".py", ".js", ".sh", ".bat", ".ps1"],
    "Applications": [".exe", ".msi", ".app", ".dmg"],
}


def get_folder_path() -> Path:
    """Ask the user for a folder path and return a valid Path object."""
    while True:
        user_input = input("Enter the full folder path to organize: ").strip()

        # Remove surrounding quotes in case the user pastes a path with quotes.
        if (user_input.startswith('"') and user_input.endswith('"')) or (
            user_input.startswith("'") and user_input.endswith("'")
        ):
            user_input = user_input[1:-1].strip()

        folder_path = Path(user_input)

        if not folder_path.exists():
            print("That path does not exist. Please enter a valid folder path.")
            continue

        if not folder_path.is_dir():
            print("The path is not a folder. Please enter a folder path, not a file path.")
            continue

        return folder_path


def get_category(file_path: Path) -> str:
    """Return the category name for a file based on its extension."""
    extension = file_path.suffix.lower()

    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return category

    return "Others"


def create_folder(destination: Path) -> None:
    """Create a destination folder if it does not already exist."""
    if not destination.exists():
        destination.mkdir(parents=True, exist_ok=True)
        print(f"Created folder: {destination.name}")


def resolve_duplicate_name(destination: Path) -> Path:
    """If a file already exists, return a new path with _1, _2, ... appended."""
    counter = 1
    new_destination = destination

    while new_destination.exists():
        new_name = f"{destination.stem}_{counter}{destination.suffix}"
        new_destination = destination.with_name(new_name)
        counter += 1

    return new_destination


def organize_files(folder_path: Path) -> None:
    """Move files in the folder into category folders."""
    files_moved = 0
    files_skipped = 0
    skipped_items = []

    for item in folder_path.iterdir():
        if item.is_dir():
            files_skipped += 1
            skipped_items.append(item.name)
            continue

        category = get_category(item)
        category_folder = folder_path / category
        create_folder(category_folder)

        destination = category_folder / item.name
        destination = resolve_duplicate_name(destination)

        shutil.move(str(item), str(destination))
        print(f"Moved: {item.name} -> {category}/{destination.name}")
        files_moved += 1

    print("\nOrganization complete.")
    print(f"Files moved: {files_moved}")
    print(f"Items skipped (folders only): {files_skipped}")

    if skipped_items:
        print("Skipped directories:")
        for skipped in skipped_items:
            print(f" - {skipped}")


def main() -> None:
    """Main program entry point."""
    print("Automated File Organizer")
    print("This program moves files into folders based on their types.")
    print("Built with Python's pathlib and shutil modules.\n")

    folder_path = get_folder_path()
    organize_files(folder_path)


if __name__ == "__main__":
    main()
