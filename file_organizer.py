
from pathlib import Path
import shutil

# Test folder inside your project directory
SOURCE_FOLDER = Path(__file__).parent / "sample_files"

# File categories and their extensions
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".csv"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Python Files": [".py"],
    "ZIP Files": [".zip", ".rar", ".7z"],
}


def get_category(extension):
    for category, extensions in FILE_TYPES.items():
        if extension.lower() in extensions:
            return category
    return "Others"


def organize_files():
    if not SOURCE_FOLDER.exists():
        SOURCE_FOLDER.mkdir(parents=True)
        print(f"Created test folder: {SOURCE_FOLDER}")
        print("Add some sample files to this folder and run again.")
        return

    files = [
        item for item in SOURCE_FOLDER.iterdir()
        if item.is_file()
    ]

    if not files:
        print("No files found in the test folder.")
        return

    moved = 0
    skipped = 0

    for file_path in files:
        category = get_category(file_path.suffix)
        destination_folder = SOURCE_FOLDER / category
        destination_folder.mkdir(exist_ok=True)

        destination = destination_folder / file_path.name

        # Avoid overwriting an existing file
        if destination.exists():
            print(f"Skipped duplicate: {file_path.name}")
            skipped += 1
            continue

        try:
            shutil.move(str(file_path), str(destination))
            print(f"Moved: {file_path.name} -> {category}")
            moved += 1
        except OSError as error:
            print(f"Could not move {file_path.name}: {error}")
            skipped += 1

    print("\n--- Organization Complete ---")
    print(f"Files moved: {moved}")
    print(f"Files skipped: {skipped}")


if __name__ == "__main__":
    organize_files()
