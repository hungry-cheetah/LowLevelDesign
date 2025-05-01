# 🔹 Why Use Flyweight Pattern?
# ✅ Reduces Memory Usage → Instead of creating duplicates, we reuse objects.
# ✅ Improves Performance → Less memory allocation means faster execution.
# ✅ Best for Large-Scale Applications → Example: Text Editors, Games, UI Components.

# 🔹 Where Can We Use Flyweight Pattern?
# 🔹 Text Editors → Reusing character objects to store formatting efficiently.
# 🔹 Games → Sharing identical textures for multiple trees, enemies, or bullets.
# 🔹 UI Frameworks → Reusing button styles instead of creating new ones.
# 🔹 Database Connection Pools → Avoid creating duplicate database connections.

# 🔹 Summary
# Flyweight Pattern is used to share objects instead of creating duplicates.
# Stores objects in a dictionary and reuses them when needed.
# Reduces memory usage, improves performance, and is useful in large applications.


class CharacterFlyweight:
    """Flyweight class: Stores shared properties of characters"""
    _characters = {}

    def __new__(cls, char, font="Arial", size=12, bold=False):
        key = (char, font, size, bold)
        if key not in cls._characters:
            cls._characters[key] = super(CharacterFlyweight, cls).__new__(cls)
            cls._characters[key].char = char
            cls._characters[key].font = font
            cls._characters[key].size = size
            cls._characters[key].bold = bold
        return cls._characters[key]

    def display(self, position):
        return f"'{self.char}' at {position} [Font: {self.font}, Size: {self.size}, Bold: {self.bold}]"


# Client: Uses the flyweight objects
class TextEditor:
    def __init__(self):
        self.characters = []

    def add_character(self, char, position, font="Arial", size=12, bold=False):
        character = CharacterFlyweight(char, font, size, bold)  # Flyweight object
        self.characters.append((character, position))

    def display_text(self):
        for character, position in self.characters:
            print(character.display(position))


# Test Flyweight Pattern
editor = TextEditor()
editor.add_character("H", (0, 0))
editor.add_character("e", (0, 1))
editor.add_character("l", (0, 2))
editor.add_character("l", (0, 3))  # 'l' is reused instead of creating a new object
editor.add_character("o", (0, 4))
editor.add_character("!", (0, 5))

print("\nDisplaying text:\n")
editor.display_text()

# Checking memory optimization
print("\nTotal unique objects created:", len(CharacterFlyweight._characters))
