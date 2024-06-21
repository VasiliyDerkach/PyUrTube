import time
class User:
    def __init__(self, nickname, password, age):
        self.nickname= nickname
        self.age= age
#        if password==password_conf:
        self.password= hash(password)
#        else:
#            self.password= None
    def __eq__(self, other):
        return (self.nickname==other.nickname and
                hash(self.password)==hash(other.password))
    def __str__(self):
        return self.nickname
class Video:
    def __init__(self,title,duration,adult_mode= False):
        self.title= title
        self.duration= duration
        self.time_now= 0
        self.adult_mode= adult_mode
class ListVideos:
    def __init__(self, *args):
        self.items= list(args)
    def __contains__(self, item):
        for i in self.items:
            if i.title == item.title:
                return True

        return False
    # def __str__(self):
    #     s= []
    #     for p in self.items:
    #         s.append(p.title)
    #     return s


class ListUsers:
    def __init__(self, *args):
        self.items= list(args)
    def __contains__(self, item):
        for i in self.items:
            if i == item:
                return True

        return False
    def add(self, other):
        self.items.append(other)
class UrTube:
    def __init__(self):
        self.current_user= None
        self.videos= ListVideos()
        self.users= ListUsers()
    def log_in(self, login, password):
        newuser = User(login, password)
        self.current_user = (newuser if newuser in self.users else self.current_user)
    def register(self,nickname, password, age):
        is_exist = False
        for a in self.users.items:
            nickname1=a.nickname
            if nickname1==nickname:
                is_exist= True
                break
        if is_exist:
            print(f"Пользователь {nickname} уже существует")
        else:
            newuser = User(nickname, password, age)
            self.users.add(newuser)
            self.current_user= newuser
    def log_out(self):
        self.current_user = None
    def add(self,*args):
        for a in args:
            if a in self.videos:
                break
            else:
                self.videos.items.append(a)
    def get_videos(self,FindString):
        lst= []
        for g in self.videos.items:
            p= g.title.upper()
            p1= FindString.upper()
            k= p.find(p1)
            if k>=0:
                lst.append(g.title)
        return lst
    def watch_video(self,CurrentTitle):
        if self.current_user:
            for i in self.videos.items:
                if i.title==CurrentTitle:
                    if self.current_user.age < 18 and i.adult_mode:
                        print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    else:
                        for j in range(i.time_now, i.duration-1):
                            print(j+1,  end=' ')
                            time.sleep(1)
                        print("Конец видео")
                        i.time_now=0
        else:
            print("Войдите в аккаунт, чтобы смотреть видео")
    def __contains__(self, item):
        if type(item)=='__main__.Video':
            for i in self.videos.items:
                if i.title == item.title:
                    return True
        elif type(item)=='__main__.User':
            for i in self.users.items:
                if i == item:
                    return True

        return False


if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
    print((type(v1)))
    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')

    #
    # TestUrTube= UrTube()
    # TestUrTube.register('John','0987',25)
    # TestUrTube.register('Johna','097',35)
    # TestUrTube.add(Video('Pyton',200),Video('JS',500,True),
    #                Video('Pyton3',400,True))
    # ListTitle=TestUrTube.get_videos('Pyton')
    # print(TestUrTube)

#    print(use1==use2)
#    use3=User('John','0987',55)
#    print(use1==use3)
