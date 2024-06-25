import math
class Figure:
    def __init__(self):
        self.sides_count = 0
        self.__sides=[]
        #список сторон(целые числа)
        self.__color=[]
        #список цветов в формате RGB
        filled= None
        #закрашенный, bool
    def get_color(self):
        return self.__color
    def get_sides(self):
        return self.__sides
    def __is_valid_color(self,r, g, b):
        return True if (0>= r >=255) and (0>= g >=255) and (0>= b >=255) else False
    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *args):
        if (len(args) == self.sides_count) or (isinstance(self,Cube) and len(args) == 1):
            for g in args:
                if g<0 or type(g) != 'int':
                    return False
        else:
            return False
        return True
    def set_sides(self, *args):
        if self.__is_valid_sides( *args):
            if isinstance(self,Cube):
                for i in range(1,12):
                    self.__sides.append(args[0])
            else:
                for u in args:
                    self.__sides.append(u)
        else:
            for i in range(1,self.sides_count):
                self.__sides.append(1)
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
        if len(args) == 1:
            perim_okr = args[0]
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
        t_sides= self.get_sides()
        d = pperim
        for i in range(1,3):
            d*= (pperim-self.t_sides[i-1])

        self.__height = 2 * math.sqrt(d)/self.t_sides[0]
    def get_square(self):
        return self.__height*self.t_sides[0]/2
class Cube(Figure):
    def __init__(self, color, *args):
        super().__init__()
        self.sides_count = 12
        self.set_params(color,*args)
    def get_volume(self):
        t_sides= self.get_sides()
        return t_sides[0]*t_sides[0]*t_sides[0]

if __name__=='__main__':
    circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
    cube1 = Cube((222, 35, 130), 6)

    # Проверка на изменение цветов:
    circle1.set_color(55, 66, 77)  # Изменится
    cube1.set_color(300, 70, 15)  # Не изменится
    print(circle1.get_color())
    print(cube1.get_color())

    # Проверка на изменение сторон:
    cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
    circle1.set_sides(15)  # Изменится
    print(cube1.get_sides())
    print(circle1.get_sides())

    # Проверка периметра (круга), это и есть длина:
    print(len(circle1))

    # Проверка объёма (куба):
    print(cube1.get_volume())