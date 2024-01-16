class Battery:
    def __init__(self, energy):
        self.energy = energy

    def get_energy(self):
        return self.energy

    def set_energy(self, energy):
        self.energy = energy

    def decrease_energy(self):
        self.energy -= 2
        if (self.energy <= 0):
            self.energy = 0
            


class FlashLamp(Battery):
    def __init__(self, energy, status):
        super().__init__(energy)
        self.status = status

    def infor_lamp(self):
        print("enery:", self.energy, "status:", self.status)

    def check_turn_on(self):
        if (self.get_energy() <= 0):
            return False
        return self.status

# # Create an instance of Battery
# battery = Battery(10)

# # Print initial energy of the battery
# print("Initial battery energy:", battery.get_energy())

# # Decrease energy by 2
# battery.decrease_energy()

# # Print energy after decreasing
# print("Battery energy after decreasing:", battery.get_energy())

# # Set new energy value
# battery.set_energy(15)

# # Print energy after setting a new value
# print("Battery energy after setting new value:", battery.get_energy())

# # Create an instance of FlashLamp using the Battery instance
# flashlamp = FlashLamp(10, True)

# # Print initial information of the FlashLamp
# flashlamp.infor_lamp()

# # Check if the FlashLamp is turned on
# print("Is FlashLamp turned on?", flashlamp.check_turn_on())

# # Decrease energy of the FlashLamp by 2
# flashlamp.decrease_energy()

# # Print information after decreasing energy
# flashlamp.infor_lamp()
