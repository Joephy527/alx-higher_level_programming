#!/usr/bin/python3
#!/usr/bin/python3
"""A class that defines a rectangle"""


class Rectangle:
    """this represents a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializing this rectangle class
        Args:
            width: represents the width of the rectangle
            height: represents the height of the rectangle
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """

        self.width = width
        self.height = height

    def __str__(self):
        """presents a diagram of the rectangle defined for an object"""

        if self.__height == 0 or self.__width == 0:
            return ''
        rectangle = ''
        for column in range(self.__height):
            for row in range(self.__width):
                rectangle += '#'
            if column < self.__height - 1:
                rectangle += '\n'
        return (rectangle)

    @property
    def height(self):
        """retrieves height attribute"""

        return self.__height

    @height.setter
    def height(self, value):
        """sets height attribute"""

        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    @property
    def width(self):
        """retrieves width attribute"""

        return self.__width

    @width.setter
    def width(self, value):
        """sets width attribute"""

        if not type(value) == int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    def area(self):
        """Returns the area of the rectangle"""

        return self.__height * self.__width

    def perimeter(self):
        """Returns the perimeter of the rectangle"""

        if self.__height == 0 or self.__width == 0:
            return 0
        return ((self.__height + self.__width) * 2)
