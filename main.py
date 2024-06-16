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
                lst.append(g)
        return lst
    def watch_video(self,CurrentTitle):
        if self.current_user:
            for i in self.videos.items:
                if i.title==CurrentTitle:
                    if self.current_user.age < 18 and i.adult_mode:
                        print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    else:
                        for j in range(i.duration-1):
                            print(j+1)
                            time.sleep(2)
                        print("Конец видео")
        else:
            print("Войдите в аккаунт, чтобы смотреть видео")


if __name__ == '__main__':
    TestUrTube= UrTube()
    TestUrTube.register('John','0987',25)
    TestUrTube.register('Johna','097',35)
    TestUrTube.add(Video('Pyton',200),Video('JS',500,True),
                   Video('Pyton3',400,True))
    ListTitle=TestUrTube.get_videos('Pyton')
    print(TestUrTube)

#    print(use1==use2)
#    use3=User('John','0987',55)
#    print(use1==use3)
