# -*- coding: utf-8 -*-

class cp:
    def __init__(self, **kwargs):
        try: self.name = kwargs['name']
        except: self.name = 'noname'
        try: self.num = kwargs['num']
        except: self.num = 1
        try: self.pd = kwargs['pd']
        except: self.pd = 5
        try: self.time = kwargs['time']
        except: self.time = 1200
        


#l = [1, 2, 3]
#l.insert(2, 42)
#print l

a = list() # чекпоинты
#d = list() # дельты

def add(pn=42e42, pt=5, **kwargs):
    if pn > len(a): pn = len(a)
    i = 0
    for c in a:
        i += 1
        c.num = i
    
    for c in a:
        #print c.num, 'cnum'
        if pn > c.num:
            tadd = 0
            for cc in a[pn:]:
                tadd += cc.pd
                print tadd, 'tadd+'
                cc.time = kwargs['time'] + tadd
        if pn < c.num: # здесь что-то не так.
            #print c.name, '<cnum'
            tadd = 0
            for cc in reversed(a[:pn]):
                print cc. name, 'cc rev'
                tadd += cc.pd
                print tadd, 'tadd-'
                cc.time = kwargs['time'] - tadd
            
            
    
    a.insert(pn, cp(**kwargs))
    #d.insert(pn, pt)
    
    
def edit(n, **kwargs):
    pass
    
    
add (10, name='one', time = 1200)
add (name='two', time = 1200)
add (0, name='three', time = 1200)
add (2, name='four', pd=20, time=1300)
for c in a: 
    print c.pd
    print c.name, c.time



