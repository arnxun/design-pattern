'a prototype pattern test, refer to <Mastering Python Design Patterns>'

__author__ = 'arnxun'

import copy
from collections import OrderedDict


class Book:

    def __init__(self, name, authors, price, **rest):
        "rest的例子如：出版社，出版日期等"
        self.name = name
        self.authors = authors
        self.price = price
        self.__dict__.update(rest)

    def __str__(self):
        myList = []
        ordered = OrderedDict(sorted(self.__dict__.items()))
        for i in ordered.keys():
            myList.append('{}: {}'.format(i, ordered[i]))
            if i == 'price':
                myList.append('$')
            myList.append('\n')
        return ''.join(myList)


class Prototype:
    
    def __init__(self):
        self.objects = dict()
    
    def register(self, identifier, obj):
        self.objects[identifier] = obj

    def unregister(self, identifier):
        if identifier and identifier in self.objects:
            del self.objects[identifier]

    def clone(self, identifier, **kwargs):
        found = self.objects.get(identifier)
        if not found:
            raise ValueError('Incorrect object identifier: {}'.format(identifier))
        obj = copy.deepcopy(found)
        obj.__dict__.update(kwargs)
        return obj


def main():
    temp_dict = {
        'name': 'The C Programming Language', 
        'authors': ('Brian W. Kernighan', 'Dennis M.Ritchie'), 
        'price': 118, 
        'publisher':'Prentice Hall', 
        'length': 228, 
        'publication_date':'1978-02-22',
        'tags':('C', 'programming', 'algorithms', 'data structures')}
    b1 = Book(**temp_dict)
    prototype = Prototype()
    cid = 'k&r-first'
    prototype.register(cid, b1)
    b2 = prototype.clone(
        cid, 
        name='The C Programming Language(ANSI)', 
        price=48.99, 
        length=274, 
        publication_date='1988-04-01', 
        edition=2)
    
    print(b1)
    print(b2)

    print("ID b1 : {} != ID b2 : {}".format(id(b1), id(b2)))


if __name__ == '__main__':
    main()