import math
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
    def set_color(self, r, g, b):
        if self.__is_valid_color(self,r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *args):
        if (args.count() == self.sides_count) or (isinstance(self,Cube) and args.count() == 1):
            for g in args:
                if g<0 or type(g) != 'int':
                    return False
        else:
            return False
        return True
    def set_sides(self, *args):
        if self.__is_valid_sides( *args):
            self.__sides = args
        else:
            for i in range(1,self.sides_count):
                self.__sides[i] = 1
    def __len__(self):
        perim= 0
        for y in self.__sides:
            perim+= y
        return perim
    def set_params(self,color,*args):
        self.set_color(*color)
        self.set_sides( *args)

class Circle(Figure):
    def __init__(self, color, *args):
        super().__init__()
        self.sides_count = 1
        self.set_params(color,*args)
        if args.count() == 1:
            perim_okr = args[1]
        else:
            perim_okr = 1
        self.__radius = perim_okr/(2* math.pi)
    def get_square(self):
        return 2*self.__radius * self.__radius * math.pi

class Triangle(Figure):
    def __init__(self,color, *args):
        super().__init__()
        self.sides_count = 3
        self.set_params(color, *args)
        pperim = self.__len__()/2
        d = pperim
        for i in range(1,3):
            d*= (pperim-self.__sides[i])

        self.__height = 2 * math.sqrt(d)/self.__sides[1]
    def get_square(self):
        return self.__height*self.__sides[1]/2
