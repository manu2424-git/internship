import os
import shutil
import re
import requests
from bs4 import BeautifulSoup

print("=" * 50)
print("      TASK AUTOMATION USING PYTHON")
print("=" * 50)
print("1. Move all .jpg files to another folder")
print("2. Extract email addresses from a text file")
print("3. Scrape webpage title and save it")
print("=" * 50)

choice = input("Enter your choice (1-3): ")

# -------------------------------------------------
# OPTION 1 - MOVE JPG FILES
# -------------------------------------------------
if choice == "1":
    source_folder = input("Enter source folder path: ")
    destination_folder = input("Enter destination folder path: ")

    os.makedirs(destination_folder, exist_ok=True)

    moved = 0

    for file in os.listdir(source_folder):
        if file.lower().endswith(".jpg"):
            source = os.path.join(source_folder, file)
            destination = os.path.join(destination_folder, file)
            shutil.move(source, destination)
            print(f"Moved: {file}")
            moved += 1

    print(f"\nTotal JPG files moved: {moved}")

# -------------------------------------------------
# OPTION 2 - EXTRACT EMAILS
# -------------------------------------------------
elif choice == "2":
    input_file = input("Enter input text file name: ")
    output_file = input("Enter output file name: ")

    with open(input_file, "r") as file:
        text = file.read()

    emails = re.findall(
        r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
        text
    )

    with open(output_file, "w") as file:
        for email in emails:
            file.write(email + "\n")

    print(f"\nFound {len(emails)} email(s).")
    print("Saved successfully to", output_file)

# -------------------------------------------------
# OPTION 3 - SCRAPE WEBPAGE TITLE
# -------------------------------------------------
elif choice == "3":
    url = input("Enter webpage URL: ")

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        title = soup.title.string.strip() if soup.title else "No Title Found"

        with open("webpage_title.txt", "w") as file:
            file.write(title)

        print("\nWebpage Title:")
        print(title)
        print("Saved to webpage_title.txt")

    except Exception as e:
        print("Error:", e)

# -------------------------------------------------
# INVALID CHOICE
# -------------------------------------------------
else:
    print("Invalid choice! Please run the program again.")