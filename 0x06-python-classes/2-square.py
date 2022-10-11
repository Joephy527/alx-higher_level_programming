#!/usr/bin/python3
"""Defines a square"""

class Square:
    """sw"""

    def __init__(self, size=0):
        """ sw """

        self.__size = size
        if type(self.__size) != int:
            raise TypeError('size must be an intege')
        if self.__size < 0:
            raise ValueError('size must be >= 0')
