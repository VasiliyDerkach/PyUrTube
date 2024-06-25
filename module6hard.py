class Figure:
    def __init__(self):
        sides_count = 0
        __sides:[]
        #список сторон(целые числа)
        __color:[]
        #список цветов в формате RGB
        filled: None
        #закрашенный, bool
    def get_color(self):
        return self.__color
    def __is_valid_color(self,r, g, b):
        return True if (0>= r >=255) and (0>= g >=255) and (0>= b >=255) else False