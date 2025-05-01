# The Observer Design Pattern defines a one-to-many dependency between objects so that
#  when one object (Subject) changes state, all its dependents (Observers) are notified automatically.


from abc import ABC, abstractmethod

# Observer Interface
class Observer(ABC):
    """Abstract Observer that gets notified when Subject changes"""

    @abstractmethod
    def update(self, temperature):
        pass

# Concrete Observer 1
class PhoneDisplay(Observer):
    """Observer that represents a phone display"""

    def __init__(self, name):
        self.name = name

    def update(self, temperature):
        print(f"📱 {self.name} Display: Updated Temperature -> {temperature}°C")

# Concrete Observer 2
class LEDPanel(Observer):
    """Observer that represents an LED display panel"""

    def update(self, temperature):
        print(f"💡 LED Panel: Updated Temperature -> {temperature}°C")

# Subject Interface
class Subject(ABC):
    """Abstract Subject that maintains a list of observers"""

    @abstractmethod
    def add_observer(self, observer):
        pass

    @abstractmethod
    def remove_observer(self, observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass

# Concrete Subject
class WeatherStation(Subject):
    """Subject that stores temperature and notifies observers"""

    def __init__(self):
        self._observers = []
        self._temperature = 0  # Initial temperature

    def add_observer(self, observer):
        """Attach an observer"""
        self._observers.append(observer)

    def remove_observer(self, observer):
        """Detach an observer"""
        self._observers.remove(observer)

    def set_temperature(self, new_temperature):
        """Change temperature and notify observers"""
        print(f"\n🌡️ Weather Station: Temperature changed to {new_temperature}°C")
        self._temperature = new_temperature
        self.notify_observers()

    def notify_observers(self):
        """Notify all observers about the change"""
        for observer in self._observers:
            observer.update(self._temperature)

# Client Code
if __name__ == "__main__":
    # Create Weather Station (Subject)
    weather_station = WeatherStation()

    # Create Observers (Displays)
    phone_display = PhoneDisplay("Alice's Phone")
    led_panel = LEDPanel()

    # Register Observers
    weather_station.add_observer(phone_display)
    weather_station.add_observer(led_panel)

    # Change Temperature - Observers will get updated
    weather_station.set_temperature(25)
    weather_station.set_temperature(30)

    # Remove an Observer
    weather_station.remove_observer(led_panel)

    # Change Temperature - Only PhoneDisplay gets updated
    weather_station.set_temperature(28)
