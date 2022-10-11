#!/usr/bin/python3
"""Defines a square"""


class Square:
    """A class that defines a square by its size"""

    def __init__(self, size=0):
        """Method to initialize the square  object
        Args:
            size: represnets the size of the square defined
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """

        if not isinstance(size, int):
            raise TypeError('size must be an intege')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = int(size)
