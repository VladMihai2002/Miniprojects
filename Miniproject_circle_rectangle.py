# The Python program defines two classes: Circle and Rectangle. Let’s break down what each class does:
#
# Circle Class:
# Attributes:
# radius: Represents the radius of the circle (input by the user).
# color: Represents the color of the circle (input by the user).
# Methods:
# describe_circle(): Prints the color and radius of the circle.
# area(): Calculates and returns the area of the circle.
# diameter(): Calculates and returns the diameter of the circle.
# circumference(): Calculates and returns the circumference of the circle.
# Rectangle Class:
# Attributes:
# length: Represents the length of the rectangle (input by the user).
# width: Represents the width of the rectangle (input by the user).
# color: Represents the color of the rectangle (input by the user).
# Methods:
# describe(): Prints information about the rectangle (color, length, and width).
# area(): Calculates and returns the area of the rectangle.
# perimeter(): Calculates and returns the perimeter of the rectangle.
# change_color(new_color): Updates the rectangle’s color with the new color provided by the user.
# Example Usage:
#
# The program prompts the user to input the radius and color for a circle.
# It calculates and displays the circle’s area, diameter, and circumference.
# Next, the user inputs the length, width, and color for a rectangle.
# The program calculates and displays the rectangle’s area and perimeter.
# The user can change the rectangle’s color by providing a new color.
# Feel free to run this program and interactively input the values for the circle and rectangle!

class Circle:
    def __init__(self):
        self.radius = float(input("Enter the radius of the circle: "))
        self.color = input("Enter the color of the circle: ")

    def describe_circle(self):
        print(f"Circle color: {self.color}, Radius: {self.radius:.2f}")

    def area(self):
        return 3.14159 * self.radius ** 2

    def diameter(self):
        return 2 * self.radius

    def circumference(self):
        return 2 * 3.14159 * self.radius


class Rectangle:
    def __init__(self):
        self.length = float(input("Enter the length of the rectangle: "))
        self.width = float(input("Enter the width of the rectangle: "))
        self.color = input("Enter the color of the rectangle: ")

    def describe(self):
        print(f"Rectangle color: {self.color}, Length: {self.length:.2f}, Width: {self.width:.2f}")

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def change_color(self, new_color):
        self.color = new_color

# Example usage:
if __name__ == "__main__":
    circle = Circle()
    circle.describe_circle()
    print("Circle area:", circle.area())
    print("Circle diameter:", circle.diameter())
    print("Circle circumference:", circle.circumference())

    rectangle = Rectangle()
    rectangle.describe()
    print("Rectangle area:", rectangle.area())
    print("Rectangle perimeter:", rectangle.perimeter())
    new_color = input("Enter a new color for the rectangle: ")
    rectangle.change_color(new_color)
    rectangle.describe()