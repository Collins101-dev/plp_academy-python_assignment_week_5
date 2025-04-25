class Smartphone:
    def __init__(self, brand, model, storage, battery_capacity):
        #Constructor to initialize the smartphone attributes.
        self.brand = brand
        self.model = model
        self.storage = storage  # in GB
        self.battery_capacity = battery_capacity  # in mAh
        self.__is_powered_on = False  # Encapsulated attribute

    def power_on(self):
        #Method to power on the smartphone.
        if not self.__is_powered_on:
            self.__is_powered_on = True
            print(f"{self.brand} {self.model} is now powered on.")
        else:
            print(f"{self.brand} {self.model} is already on.")

    def power_off(self):
        #Method to power off the smartphone.
        if self.__is_powered_on:
            self.__is_powered_on = False
            print(f"{self.brand} {self.model} is now powered off.")
        else:
            print(f"{self.brand} {self.model} is already off.")

    def __str__(self):
        #String representation of the smartphone.
        return f"{self.brand} {self.model} with {self.storage}GB storage and {self.battery_capacity}mAh battery."


# Inheritance: GamingSmartphone inherits from Smartphone
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage, battery_capacity, gpu, cooling_system):
        #Constructor to initialize gaming smartphone attributes.
        super().__init__(brand, model, storage, battery_capacity)
        self.gpu = gpu
        self.cooling_system = cooling_system

    def play_game(self, game_name):
        #Method to simulate playing a game.
        print(f"Playing {game_name} on {self.brand} {self.model} with {self.gpu} GPU and {self.cooling_system} cooling system.")

    def __str__(self):
        #String representation of the gaming smartphone.
        return super().__str__() + f" It features a {self.gpu} GPU and {self.cooling_system} cooling system."


# Example usage
if __name__ == "__main__":
    # Create a regular smartphone
    phone = Smartphone("Samsung", "Galaxy S21", 128, 4000)
    print(phone)
    phone.power_on()
    phone.power_off()

    # Create a gaming smartphone
    gaming_phone = GamingSmartphone("Asus", "ROG Phone 5", 256, 6000, "Adreno 660", "Vapor Chamber")
    print(gaming_phone)
    gaming_phone.power_on()
    gaming_phone.play_game("Genshin Impact")
    gaming_phone.power_off()