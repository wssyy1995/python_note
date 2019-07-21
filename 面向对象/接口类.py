二.接口类（python中没有接口类，这只是定义一个规范）

（1）写一个规范接口类，来约束这个接口类的继承者
 1.这个规范规定了：这个类的继承者必须已经拥有类里的方法，否则在实例化的时候就会报错
 2.这个规范接口类里的方法只是一种规则，本身不实现


（2）将类变成接口类：
1.让这些类继承metaclass=ABCmeta
2.在每个方法装上abstractmethod

例子：
from abc import abstractmethod,ABCMeta
class Swim_Animal(metaclass=ABCMeta):
    @abstractmethod
    def swim(self):
        pass


class Walk_Animal(metaclass=ABCMeta):
    @abstractmethod
    def walk(self):
        pass


class Fly_Animal(metaclass=ABCMeta):
    @abstractmethod
    def fly(self):
        pass


class Tiger(Walk_Animal, Swim_Animal):
    def walk(self):
        print('it can walk')

    def swim(self):
        print('it can Swim')



class Owl(Walk_Animal, Fly_Animal):
    def walk(self):
        print('it can walk')
    def fly(self):
        print('it can fly')


class Swan(Fly_Animal, Walk_Animal, Swim_Animal):
    def walk(self):
        print('it can walk')
    def fly(self):
        print('it can fly')
    def swim(self):
        print('it can Swim')


tiger=Tiger()
owl=Owl()
swan=Swan()