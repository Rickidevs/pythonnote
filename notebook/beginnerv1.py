import os

# Check and create file if not exists
if not os.path.exists("notes.txt"):
    with open("notes.txt", "w") as f:
        pass  # Create empty file

def read_notes():
    with open("notes.txt", "r") as f:
        notes = f.readlines()
        if notes:
            print("\nNotes:")
            for i, note in enumerate(notes, 1):
                print(f"{i}. {note.strip()}")
        else:
            print("\nNo notes found.")

def write_note():
    note = input("Enter new note: ")
    with open("notes.txt", "a") as f:
        f.write(note + "\n")
    print("Note saved.")

def search_note():
    keyword = input("Enter keyword to search: ")
    with open("notes.txt", "r") as f:
        found = False
        for i, note in enumerate(f, 1):
            if keyword.lower() in note.lower():
                print(f"{i}. {note.strip()}")
                found = True
        if not found:
            print("No matching note found.")

def delete_note():
    read_notes()
    try:
        index = int(input("Enter note number to delete: "))
        with open("notes.txt", "r") as f:
            notes = f.readlines()
        if 1 <= index <= len(notes):
            deleted = notes.pop(index - 1)
            with open("notes.txt", "w") as f:
                f.writelines(notes)
            print(f"Note deleted: {deleted.strip()}")
        else:
            print("Invalid note number.")
    except ValueError:
        print("Please enter a valid number.")

# Main menu
while True:
    print("\n=== Note Program ===")
    print("1. Read notes")
    print("2. Write a new note")
    print("3. Search notes")
    print("4. Delete a note")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        read_notes()
    elif choice == "2":
        write_note()
    elif choice == "3":
        search_note()
    elif choice == "4":
        delete_note()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
