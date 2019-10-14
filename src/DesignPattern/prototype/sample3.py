' a prototype pattern test'

__author__ = 'arnxun'

import copy
# import abc

class baseObject:
    """
    原型角色：定义用于复制现有实例来生成新实例的方法； 
    静态语言中常用一个实现了某个接口类(Cloneable)的抽象类来实现，只有实现了接口中clone方法的类才可进行克隆对象
    """

    def clone(self):
        "定义复制现有实例来生成新实例的方法"
        return copy.deepcopy(self)
    
    # @abc.abstractmethod
    # def clone1(self):
    #     "子类必须定义clone1功能"
    #     pass


class PrototypeManager:

    def __init__(self):
        self.source_dict = dict()
    
    def register(self, key, obj):
        self.source_dict[key] = obj

    def get(self, key):
        source = self.source_dict.get(key)
        if not source:
            raise ValueError('Incorrect key: {}'.format(key))
        return source.clone()


class Animal(baseObject):

    def __init__(self, name, classes):
        self.classes = classes
        self.name = name

    def __str__(self):
        return '%s_%s' % (self.classes, self.name)


class Person(baseObject):
    
    def __init__(self, name, age, city='China'):
        self.name = name
        self.age = age
        self.city = city

    def __str__(self):
        return '%s_%s_%s' % (self.name, self.age, self.city)
    

    def clone(self):
        new_person = copy.deepcopy(self)
        new_person.age = 18
        new_person.name = 'None'
        return new_person



def main():
    manager = PrototypeManager()

    a1 = Animal('小白', 'Dog')
    a2 = Animal('小黑', 'cat')
    manager.register('dog1', a1)
    manager.register('cat1', a2)

    p1 = Person('zhangsan', 20)
    p2 = Person('lisi', 15, 'wuhan')
    manager.register('person1', p1)
    manager.register('person2', p2)

    b1 = manager.get('dog1')
    b2 = manager.get('cat1')

    m1 = manager.get('person1')
    m2 = manager.get('person2')
    
    print(a1)
    print(b1)
    print('\n')

    print(a2)
    print(b2)
    print('\n')

    print(p1)
    print(m1)
    print('\n')

    print(p2)
    print(m2)


if __name__ == "__main__":
    main()

