# The Command Pattern is a behavioral design pattern that:

# Encapsulates a request (action) as an object.
# Decouples the sender (who requests an action) from the receiver (who executes it).
# Allows undo/redo functionality.
# It's useful when: ✔ You want to parameterize objects with operations.
# ✔ You need to queue requests or log actions.
# ✔ You want to support undo/redo operations.

from abc import ABC, abstractmethod


class Command(ABC):
    """Command Interface"""
    
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

class CommandExecutor:
    def __init__(self):
        self.history = []

    def execute(self, command):
        command.execute()
        self.history.append(command)

    def undo(self):
        if self.history:
            print("Undoing last command...")
            command = self.history.pop()
            command.undo()
        else:
            print("Nothing to undo!")

# Concrete Command for Undo/Redo
class TextEditor:
    def __init__(self):
        self.text = ""

    def write(self, new_text):
        self.text += new_text
        # print(f"Text: {self.text}")

    def erase(self, length):
        self.text = self.text[:-length]
        # print(f"Text after undo: {self.text}")

    def display(self):
        print(f"Text: {self.text}")

class WriteCommand(Command):
    def __init__(self, editor, text):
        self.editor = editor
        self.text = text

    def execute(self):
        self.editor.write(self.text)

    def undo(self):
        self.editor.erase(len(self.text))

# Client Code
editor = TextEditor()
cmd1 = WriteCommand(editor, "Hello ")
cmd2 = WriteCommand(
    , "World!")

executor = CommandExecutor()

executor.execute(cmd1)  # Output: Text: Hello
executor.execute(cmd2)  # Output: Text: Hello World!
editor.display()

executor.undo()  # Undo last action -> Output: Text after undo: Hello
editor.display()

# history.undo()  # Undo again -> Output: Text after undo: (empty)
# history.undo()  # Nothing left to undo
