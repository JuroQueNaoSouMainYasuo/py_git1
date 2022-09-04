# create a rectangle class that has a setter for width and height and getter for area, perimeter and diagonal
# and a method that returns a string representation of the rectangle using '*' and a \n for new line
# and a get_amount_inside method that returns the number of times a smaller rectangle fits inside the larger rectangle
# also create a square class that inherits from rectangle and has a setter for side and getter for area, perimeter and diagonal
# if an instance of a Rectangle is represented as a string, it should look like: Rectangle(width=5, height=10)

class Rectangle():
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def __repr__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width: float) -> None:
        self.width = width

    def set_height(self, height: float) -> None:
        self.height = height

    def get_area(self) -> int:
        return self.width * self.height

    def get_perimeter(self) -> int:
        return 2 * (self.width + self.height)

    def get_diagonal(self) -> float:
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self) -> str:
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        return ("*" * self.width + "\n") * self.height

    def get_amount_inside(self, shape) -> int:
        return self.get_area() // shape.get_area()


class Square(Rectangle):
    def __init__(self, side: float) -> None:
        self.width = side
        self.height = side

    def set_side(self, side: float) -> None:
        self.width = side
        self.height = side

    def set_width(self, width: float) -> None:
        self.width = width
        self.height = width

    def set_height(self, height: float) -> None:
        self.height = height
        self.width = height

    def __repr__(self) -> str:
        return f"Square(side={self.width})"


if __name__ == "__main__":
    rect = Rectangle(10, 5)
    print(rect.get_area())
    rect.set_height(3)
    print(rect.get_perimeter())
    print(rect)
    print(rect.get_picture())

    sq = Square(9)
    print(sq.get_area())
    sq.set_side(4)
    print(sq.get_diagonal())
    print(sq)
    print(sq.get_picture())

    rect.set_height(8)
    rect.set_width(16)
    print(rect.get_amount_inside(sq))

    # output
    # 50
    # 26
    # Rectangle(width=10, height=3)
    # **********
    # **********
    # **********
    # 81
    # 5.656854249492381
    # Square(side=4)
    # ****
    # ****
    # ****
    # ****
    # 2
