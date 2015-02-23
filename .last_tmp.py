# -*- coding: utf-8 -*-
# python: 2.7.2 (qpython)

from __future__ import division

# print 'hiiiiaaaa...'

class cp:
    ''' Чекпоинт'''
    def __init__(self):
        self.name = 'newcp'
        self.ctime = 0 # время чекпоинта, в этой версии 
                            # время считается "как расстояние"
        self.d1 = 4 # расстояние до предыдущего чекпоинта
        self.d2 = 6 # расстояние до следующего чекпоинта
        self.num = 1 # порядковый номер чекпоинта
    def setname(self, name):
        self.name = name
    def setctime(self, ctime):
        self.ctime = ctime
    def setd1(self, d1):
        self.d1 = d1
    def setd2(self, d2):
        self.d2 = d2
    def setnum(num):
        self.num = num
        
# print cp().name

c = cp()
c.setname('вышел из дома')
print c.name

cps = set() # сет чекпоинтов

cps.add(c)
print cps
c1 = cp()
c2 = cp()
cps.add(c1)
cps.add(c2)
print cps
for i in cps:
    print i.num, i.name