import os
from typing import List


class NoteManager:
    def __init__(self, file_path: str = "notes.txt"):
        self.file_path = file_path
        self._ensure_file()

    def _ensure_file(self) -> None:
        if not os.path.exists(self.file_path):
            with open(self.file_path, "w") as f:
                pass

    def read_notes(self) -> List[str]:
        with open(self.file_path, "r") as f:
            return [line.strip() for line in f if line.strip()]

    def write_note(self, content: str) -> None:
        if content.strip():
            with open(self.file_path, "a") as f:
                f.write(content.strip() + "\n")
            print("✅ Note saved successfully.")
        else:
            print("⚠️ Empty note not saved.")

    def search_notes(self, keyword: str) -> List[str]:
        keyword = keyword.lower().strip()
        return [
            f"{idx + 1}. {note}"
            for idx, note in enumerate(self.read_notes())
            if keyword in note.lower()
        ]

    def delete_note(self, index: int) -> bool:
        notes = self.read_notes()
        if 1 <= index <= len(notes):
            removed_note = notes.pop(index - 1)
            with open(self.file_path, "w") as f:
                f.write("\n".join(notes) + ("\n" if notes else ""))
            print(f"🗑️ Note deleted: {removed_note}")
            return True
        else:
            print("⚠️ Invalid index. No note deleted.")
            return False

    def display_notes(self) -> None:
        notes = self.read_notes()
        if notes:
            print("\n--- Notes ---")
            for i, note in enumerate(notes, 1):
                print(f"{i}. {note}")
        else:
            print("No notes available.")


class NotesApp:
    def __init__(self):
        self.manager = NoteManager()

    def display_menu(self) -> None:
        print("\n=== 📒 Notes Application ===")
        print("1. View all notes")
        print("2. Add a new note")
        print("3. Search notes")
        print("4. Delete a note")
        print("5. Exit")

    def run(self) -> None:
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-5): ").strip()

            if choice == "1":
                self.manager.display_notes()

            elif choice == "2":
                note = input("Enter your note: ")
                self.manager.write_note(note)

            elif choice == "3":
                keyword = input("Enter keyword to search: ")
                results = self.manager.search_notes(keyword)
                if results:
                    print("\n--- Search Results ---")
                    print("\n".join(results))
                else:
                    print("🔍 No matching notes found.")

            elif choice == "4":
                try:
                    index = int(input("Enter note number to delete: "))
                    self.manager.delete_note(index)
                except ValueError:
                    print("⚠️ Invalid input. Please enter a number.")

            elif choice == "5":
                print("📤 Exiting program...")
                break

            else:
                print("⚠️ Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    app = NotesApp()
    app.run()
