# -*- coding: utf-8 -*-

class cp:
    def __init__(self, **kwargs):
        try: self.name = kwargs['name']
        except: self.name = 'noname'
        try: self.num = kwargs['num']
        except: self.num = 1

a = set()

def acp(pnum=0,**kwargs):
    for c in a:
        if c.num > pnum: c.num = c.num + 1
    a.add(cp(num=pnum+1, **kwargs))
    
acp(0, name='one')
acp(1, name='two')
acp(1, name='one1')
for c in a: print c.name, c.num