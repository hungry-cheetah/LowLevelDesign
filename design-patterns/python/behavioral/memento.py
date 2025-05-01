# A TextEditor (Originator) creates and restores snapshots of its content using a History (Caretaker).

# 📌 Explanation
# ✅ Encapsulation Maintained → The internal state is saved without exposing class details.
# ✅ Undo Support → The History (Caretaker) stores multiple states for rollback.
# ✅ Snapshot Management → The Memento (TextMemento) holds immutable copies of text.
# ✅ Easy Restoration → The TextEditor (Originator) can revert to any previous state.

# 📌 Real-World Use Cases
# Undo/Redo in applications (Text Editors, Photoshop, IDEs)
# State Management in Games (Saving and loading checkpoints)


# Memento Class
class TextMemento:
    """Stores the state of the TextEditor"""
    def __init__(self, text):
        self._text = text

    def get_saved_text(self):
        return self._text

# Originator Class
class TextEditor:
    """Text Editor that can create and restore snapshots"""
    def __init__(self):
        self._text = ""

    def type(self, new_text):
        """Appends new text"""
        self._text += new_text

    def save(self):
        """Saves the current state"""
        return TextMemento(self._text)

    def restore(self, memento):
        """Restores a saved state"""
        self._text = memento.get_saved_text()

    def show_text(self):
        """Displays the current text"""
        print(f"📄 Current Text: {self._text}")

# Caretaker Class
class History:
    """Manages multiple mementos for undo functionality"""
    def __init__(self):
        self._history = []

    def save_state(self, memento):
        """Stores a memento"""
        self._history.append(memento)

    def undo(self):
        """Restores the last saved state"""
        if self._history:
            return self._history.pop()
        return None

# Client Code
if __name__ == "__main__":
    editor = TextEditor()
    history = History()

    # User types text
    editor.type("Hello, ")
    editor.show_text()  # 📄 Current Text: Hello,

    # Save state
    history.save_state(editor.save())

    # More typing
    editor.type("world!")
    editor.show_text()  # 📄 Current Text: Hello, world!

    # Save another state
    history.save_state(editor.save())

    # More typing
    editor.type(" How are you?")
    editor.show_text()  # 📄 Current Text: Hello, world! How are you?

    # Undo the last action
    last_state = history.undo()
    if last_state:
        editor.restore(last_state)
    editor.show_text()  # 📄 Current Text: Hello, world!

    # Undo again
    last_state = history.undo()
    if last_state:
        editor.restore(last_state)
    editor.show_text()  # 📄 Current Text: Hello,

