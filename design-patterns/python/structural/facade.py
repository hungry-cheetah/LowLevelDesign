# The Facade Pattern is a structural design pattern that provides a simplified interface to a 
# complex system of classes, libraries, or frameworks. 
# It hides the complexities of the system and provides a single, unified interface.

# When to Use the Facade Pattern?
# To provide a simpler interface for a complex subsystem.
# To decouple client code from the subsystem, making changes easier.
# To improve code readability and maintainability.

# Key Benefits of Facade Pattern
# ✅ Simplifies Complex Systems: Hides the complexity of multiple classes behind a single interface.
# ✅ Reduces Coupling: The client interacts with the facade instead of directly depending on multiple classes.
# ✅ Improves Maintainability: Changes to the subsystem do not affect client code.


 # Subsystem Components
class DVDPlayer:
    def on(self):
        print("DVD Player is ON")

    def play(self, movie):
        print(f"Playing '{movie}'")

    def off(self):
        print("DVD Player is OFF")


class Projector:
    def on(self):
        print("Projector is ON")

    def set_input(self, input_source):
        print(f"Projector input set to {input_source}")

    def off(self):
        print("Projector is OFF")


class SoundSystem:
    def on(self):
        print("Sound System is ON")

    def set_volume(self, level):
        print(f"Volume set to {level}")

    def off(self):
        print("Sound System is OFF")


class Lights:
    def dim(self, level):
        print(f"Lights dimmed to {level}%")

# Facade Class
class HomeTheaterFacade:
    def __init__(self, dvd_player, projector, sound_system, lights):
        self.dvd_player = dvd_player
        self.projector = projector
        self.sound_system = sound_system
        self.lights = lights

    def watch_movie(self, movie):
        print("\n--- Starting Movie Night ---")
        self.lights.dim(30)
        self.projector.on()
        self.projector.set_input("DVD Player")
        self.sound_system.on()
        self.sound_system.set_volume(10)
        self.dvd_player.on()
        self.dvd_player.play(movie)
        print("--- Enjoy Your Movie! ---\n")

    def end_movie(self):
        print("\n--- Stopping Movie Night ---")
        self.dvd_player.off()
        self.sound_system.off()
        self.projector.off()
        self.lights.dim(100)
        print("--- Movie Night Ended ---\n")


# Client Code
if __name__ == "__main__":
    # Create subsystem components
    dvd = DVDPlayer()
    projector = Projector()
    sound = SoundSystem()
    lights = Lights()

    # Create Facade
    home_theater = HomeTheaterFacade(dvd, projector, sound, lights)

    # Use Facade to watch a movie
    home_theater.watch_movie("Inception")

    # Use Facade to stop the movie
    home_theater.end_movie()
