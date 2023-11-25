"""Shape Calculator Module"""
from __future__ import annotations
import math

class Rectangle:
    """ Rectangle calculator class"""
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    def __str__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width: int) -> None:
        """Set with of rectangle

        Args:
            width (int): Width
        """
        self.width = width

    def set_height(self, height: int) -> None:
        """Set height of rectangle

        Args:
            height (int): Height
        """
        self.height = height

    def get_area(self) -> int:
        """Get area of shape

        Returns:
            int: Area of shape
        """
        return self.width * self.height

    def get_perimeter(self) -> int:
        """Get perimeter of shape

        Returns:
            int: Perimeter of shape
        """
        return 2 * self.width + 2 * self.height

    def get_diagonal(self) -> float:
        """Get Diagonal length of shape

        Returns:
            float: Diagonal lenth of shape
        """
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self) -> str:
        """Get Picture (String representation) of shape when no side exeeds 50

        Returns:
            str: String representation of picture of shape
        """
        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        picture = ""

        i = self.height
        while i > 0:
            picture += "".rjust(self.width, "*") + "\n"
            i -= 1

        return picture

    def get_amount_inside(self, shape: Rectangle | Square) -> int:
        """Get Amount of given Shape fit in shape

        Args:
            shape (Rectangle | Square): Shape to fit

        Returns:
            int: Amount of given Shape it in shape
        """
        count_width = math.floor(self.width / shape.width)
        count_height = math.floor(self.height / shape.height)

        return count_width * count_height


class Square(Rectangle):
    """Square calculator class"""
    def __init__(self, side: int) -> None:
        super().__init__(side, side)

    def __str__(self) -> str:
        return f"Square(side={self.width})"

    def set_side(self, side: int) -> None:
        """Set side of square

        Args:
            side (int): Side of square
        """
        self.width = side
        self.height = side

    def set_width(self, width: int) -> None:
        """Set width of square (and height because its a square)

        Args:
            width (int): Width of square
        """
        super().set_width(width)
        super().set_height(width)

    def set_height(self, height: int) -> None:
        """Set height of square (and width because its a square)

        Args:
            width (int): Height of square
        """
        super().set_width(height)
        super().set_height(height)
