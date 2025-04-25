class Vehicle:
    # Base class for all vehicles.
    def move(self):
        # Base move method to be overridden by subclasses.
        raise NotImplementedError("Subclasses must implement this method.")


class Car(Vehicle):
    # Car class inheriting from Vehicle.
    def move(self):
        # Implementation of move for Car.
        print("Driving 🚗")


class Plane(Vehicle):
    # Plane class inheriting from Vehicle.
    def move(self):
        # Implementation of move for Plane.
        print("Flying ✈️")


class Boat(Vehicle):
    # Boat class inheriting from Vehicle.
    def move(self):
        # Implementation of move for Boat.
        print("Sailing 🚤")


# Example usage to demonstrate polymorphism
if __name__ == "__main__":
    # Create a list of vehicles
    vehicles = [Car(), Plane(), Boat()]

    # Iterate through the list and call the move() method
    for vehicle in vehicles:
        vehicle.move()