'''
Why to use Bridge Pattern?
Decoupling: The RemoteControl class doesn't depend on TV or Radio directly.
Scalability: We can add more Device types (e.g., SmartSpeaker) or more RemoteControl types (e.g., VoiceRemote) independently.
Avoiding Class Explosion: Instead of creating multiple subclasses for each combination, we maintain separate hierarchies.
'''

from abc import ABC, abstractmethod

# Step 1: Abstract Device Class
class Device(ABC):
    """Abstract class for devices like TV and Radio."""

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

# Step 2: Concrete Device Implementations
class TV(Device):
    def turn_on(self):
        return "TV is now ON"
    
    def turn_off(self):
        return "TV is now OFF"

class Radio(Device):
    def turn_on(self):
        return "Radio is now ON"
    
    def turn_off(self):
        return "Radio is now OFF"

# Step 3: Abstract Remote Control (Bridge)
class RemoteControl(ABC):
    """Abstract class for different types of remotes."""
    
    def __init__(self, device: Device):
        self.device = device

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

# Step 4: Concrete Remote Implementations
class BasicRemoteControl(RemoteControl):
    """Basic remote with only ON/OFF functionality."""
    
    def turn_on(self):
        return self.device.turn_on()

    def turn_off(self):
        return self.device.turn_off()

class AdvancedRemoteControl(RemoteControl):
    """Advanced remote with additional mute functionality."""
    
    def turn_on(self):
        return self.device.turn_on()

    def turn_off(self):
        return self.device.turn_off()

    def mute(self):
        return "Muting the device"

# Step 5: Testing the Bridge Pattern
if __name__ == "__main__":
    tv = TV()
    radio = Radio()

    basic_remote = BasicRemoteControl(tv)
    advanced_remote = AdvancedRemoteControl(radio)

    print(basic_remote.turn_on())        # ✅ TV is now ON
    print(basic_remote.turn_off())       # ✅ TV is now OFF
    print(advanced_remote.turn_on())     # ✅ Radio is now ON
    print(advanced_remote.turn_off())    # ✅ Radio is now OFF
    print(advanced_remote.mute())        # ✅ Muting the device
