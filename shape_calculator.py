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