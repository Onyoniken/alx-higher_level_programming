#!/usr/bin/python3


class Square:

    def __str__(self):
  
        return self.pos_print()[:-1]

    def __init__(self, size=0, position=(0, 0)):
    
        self.size = size
        self.position = position

    @property
    def size(self):
      
        return self.__size

    @size.setter
    def size(self, value):
      
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
  
        return self.__position

    @position.setter
    def position(self, value):
  
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len([k for k in value if isinstance(k, int) and k >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
  
        return self.__size * self.__size

    def pos_print(self):
        pos = ""
        if not self.size:
            return "\n"
        for y in range(self.position[1]):
            pos += "\n"
        for y in range(self.size):
            for k in range(self.position[0]):
                pos += " "
            for l in range(self.size):
                pos += "#"
            pos += "\n"
        return pos

    def my_print(self):
        print(self.pos_print(), end="")
