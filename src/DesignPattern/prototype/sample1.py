'a simple prototype pattern test'

__author__ = 'arnxun'

import copy

class Person:

    def __init__(self, country='China', city='beijing', name='None', **kwargs):
        self.country = country
        self.city = city
        self.name = name
        self.__dict__.update(kwargs)

    def __str__(self):
        return '%s_%s_%s' % (self.country, self.city, self.name)


if __name__ == '__main__':
    obj_a = Person(name='zhangsan')
    obj_b = copy.deepcopy(obj_a)
    obj_b.city = 'wuhan'
    obj_b.name = 'lisi'

    print(obj_a)
    print(obj_b)
