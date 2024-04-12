# The Python program defines two classes: Car and Rectangle. Let’s break down what each class does:
#
# Car Class:
# Attributes:
# make: Represents the car’s brand (user can choose).
# model: Represents the car’s model (input by the user).
# max_speed: Represents the car’s maximum speed (input by the user).
# current_speed: Represents the car’s current speed (initialized to 0).
# color: Represents the car’s color (initialized to “gray”).
# available_colors: A set of available colors (user can choose 5-7 colors).
# registered: Represents whether the car is registered (initialized to False).
# Methods:
# describe(): Prints information about the car (brand, model, color, and max speed).
# enroll(): Changes the registered attribute to True.
# paint(new_color): Updates the car’s color if the new color is available.
# accelerate(speed): Adjusts the car’s current speed based on input.
# brake(): Stops the car (sets current speed to 0).
# Example Usage:
# The program prompts the user to input the car model and maximum speed.
# It creates an instance of the Car class.
# The user can enroll the car, change its color, accelerate, and brake.
# Finally, it displays information about the car.
# Feel free to run this program and interactively input the car details!

class Car:
    def __init__(self, model, max_speed):
        self.make = ""  # You can choose the brand
        self.model = model
        self.max_speed = max_speed
        self.current_speed = 0
        self.color = "gray"  # All cars are gray by default
        self.available_colors = {"gray", "black", "white", "blue", "red"}  # Choose 5-7 colors
        self.registered = False

    def describe(self):
        print(f"Car: {self.make} {self.model}, Color: {self.color}, Max Speed: {self.max_speed} km/h")

    def enroll(self):
        self.registered = True

    def paint(self, new_color):
        if new_color in self.available_colors:
            self.color = new_color
            print(f"Car color changed to {new_color}.")
        else:
            print(f"Error: {new_color} is not an available color.")

    def accelerate(self, speed):
        if speed < 0:
            print("Error: Speed cannot be negative.")
        elif speed > self.max_speed:
            print(f"Warning: Speed exceeds maximum allowed. Accelerating to {self.max_speed} km/h.")
            self.current_speed = self.max_speed
        else:
            self.current_speed = speed

    def brake(self):
        self.current_speed = 0
        print("Car stopped.")

# Example usage:
if __name__ == "__main__":
    model = input("Enter the car model: ")
    max_speed = float(input("Enter the maximum speed (km/h): "))
    my_car = Car(model, max_speed)

    my_car.describe()
    my_car.enroll()

    new_color = input("Enter a new color for the car: ")
    my_car.paint(new_color)

    acceleration = float(input("Enter acceleration speed (km/h): "))
    my_car.accelerate(acceleration)

    my_car.brake()
    my_car.describe()