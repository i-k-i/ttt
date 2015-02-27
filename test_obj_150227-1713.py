# -*- coding: utf-8 -*-

class cp:
    def __init__(self, **kwargs):
        try: self.name = kwargs['name']
        except: self.name = 'noname'
        try: self.num = kwargs['num']
        except: self.num = 1


#l = [1, 2, 3]
#l.insert(2, 42)
#print l

a = list()

def add(pn=42e42, **kwargs):
    if pn > len(a): pn = len(a)
    a.insert(pn, cp(**kwargs))
    
add (10, name='one')
add (name='two')
add (0, name='three')
add (2, name='four')
for c in a: print c.name