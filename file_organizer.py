import os
import shutil
from pathlib import Path

#list of all the supported types
file_types = {
    "Images": [".png", ".jpg", ".jpeg", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Music": [".mp3", ".wav", ".flac"],
    "Archives": [".zip", ".rar", ".7z"],
    "Code": [".py", ".js", ".html", ".css", ".cpp", ".java"]
}

#Get the target folder
def get_target_folder():
    default = str(Path.home() / "Downloads")
    user_input = input(f"Enter folder to organize (or press Enter for default: {default}): ").strip()
    return user_input if user_input else default

#Main code does the organizing
def organize_folder(folder):
    if not os.path.exists(folder):
        print("❌ Folder not found!")
        return

    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        if os.path.isfile(file_path):
            file_ext = os.path.splitext(filename)[1].lower()
            moved = False
            for folder_name, extensions in file_types.items():
                if file_ext in extensions:
                    dest_folder = os.path.join(folder, folder_name)
                    os.makedirs(dest_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(dest_folder, filename))
                    moved = True
                    break
            if not moved:
                other_folder = os.path.join(folder, "Others")
                os.makedirs(other_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(other_folder, filename))

#Running
if __name__ == "__main__":
    target_folder = get_target_folder()
    if os.path.exists(target_folder):
        organize_folder(target_folder)
        print("✅ Done! Folder organized.")
    else:
        print("❌ Folder not found!")
