import os

FILE_NAME = "notes.txt"

def check_and_create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w") as f:
            pass  # Create empty file

def get_notes():
    with open(FILE_NAME, "r") as f:
        return [note.strip() for note in f.readlines()]

def display_notes():
    notes = get_notes()
    if notes:
        print("\n--- Notes ---")
        for i, note in enumerate(notes, 1):
            print(f"{i}. {note}")
    else:
        print("\nNo notes found.")

def add_new_note():
    note = input("Enter a new note: ").strip()
    if note:
        with open(FILE_NAME, "a") as f:
            f.write(note + "\n")
        print("✅ Note added successfully.")
    else:
        print("⚠️ Cannot add an empty note.")

def search_notes():
    keyword = input("Enter a keyword to search: ").strip().lower()
    notes = get_notes()
    results = [f"{i+1}. {note}" for i, note in enumerate(notes) if keyword in note.lower()]
    
    if results:
        print("\n--- Search Results ---")
        print("\n".join(results))
    else:
        print("🔍 No matching notes found.")

def delete_note():
    notes = get_notes()
    display_notes()
    try:
        index_to_delete = int(input("Enter the note number to delete: "))
        if 1 <= index_to_delete <= len(notes):
            deleted_note = notes.pop(index_to_delete - 1)
            with open(FILE_NAME, "w") as f:
                for note in notes:
                    f.write(note + "\n")
            print(f"🗑️ Note deleted: {deleted_note}")
        else:
            print("⚠️ Invalid note number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

def show_menu():
    print("\n=== 📒 Notes Application ===")
    print("1. Read notes")
    print("2. Add a new note")
    print("3. Search notes")
    print("4. Delete a note")
    print("5. Exit")

def run_program():
    check_and_create_file()
    
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ").strip()

        match choice:
            case "1":
                display_notes()
            case "2":
                add_new_note()
            case "3":
                search_notes()
            case "4":
                delete_note()
            case "5":
                print("📤 Exiting the program...")
                break
            case _:
                print("⚠️ Invalid choice! Please enter a number between 1 and 5.")

if __name__ == "__main__":
    run_program()
