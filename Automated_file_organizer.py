import os
import shutil

# File categories
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z"]
}

folder_path = input("C:\\TestFolder")
if not folder_path:
    print("You did not enter a folder path.")
    exit()
print("Selected folder:", folder_path)
print("Files found:", os.listdir(folder_path))

if not os.path.exists(folder_path):
    print("Folder does not exist!")
    exit()

moved_count = 0

with open("log.txt", "a") as log:

    for file in os.listdir(folder_path):

        file_path = os.path.join(folder_path, file)

        if not os.path.isfile(file_path):
            continue

        extension = os.path.splitext(file)[1].lower()

        category_found = False

        for category, extensions in FILE_TYPES.items():

            if extension in extensions:

                destination_folder = os.path.join(folder_path, category)

                os.makedirs(destination_folder, exist_ok=True)

                shutil.move(
                    file_path,
                    os.path.join(destination_folder, file)
                )

                log.write(f"{file} -> {category}\n")

                moved_count += 1
                category_found = True
                break

        if not category_found:

            others_folder = os.path.join(folder_path, "Others")

            os.makedirs(others_folder, exist_ok=True)

            shutil.move(
                file_path,
                os.path.join(others_folder, file)
            )

            log.write(f"{file} -> Others\n")

            moved_count += 1

print("\nOrganization Complete!")
print(f"Files moved: {moved_count}")
print("Log saved in log.txt")