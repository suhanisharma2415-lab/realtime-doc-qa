import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

DOCUMENT_TEXT = ""

class DocumentHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory and event.src_path.endswith(".txt"):
            self.read_file(event.src_path)

    def on_modified(self, event):
        if not event.is_directory and event.src_path.endswith(".txt"):
            self.read_file(event.src_path)

    def read_file(self, path):
        global DOCUMENT_TEXT
        try:
            with open(path, "r", encoding="utf-8") as file:
                DOCUMENT_TEXT = file.read().lower()
                print("\n📄 Document updated successfully")
        except Exception as e:
            print(f"Error reading file: {e}")

def answer_question(question):
    question = question.lower()
    if question in DOCUMENT_TEXT:
        return " Answer found in document."
    else:
        return "Answer not found in document."

if __name__ == "__main__":
    folder_to_watch = "./documents"

    event_handler = DocumentHandler()
    observer = Observer()
    observer.schedule(event_handler, folder_to_watch, recursive=False)
    observer.start()

    print("Watching documents folder in real time...")
    print("You can ask questions now (type 'exit' to quit)")

    try:
        while True:
            user_question = input("\nYour question: ")
            if user_question.lower() == "exit":
                break
            print(answer_question(user_question))
    except KeyboardInterrupt:
        observer.stop()

    observer.stop()
    observer.join()