# -*- coding: utf-8 -*-
# python: 2.7.2 (qpython)

from __future__ import division

# print 'hiiiiaaaa...'

class cp:
    ''' Чекпоинт'''
    def __init__(self, **kwargs):
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
    
def addcp(pn, *args): # номер предыдущего чекпоинта. 
               # Если pn=0 - чекпоинт становится первым.
    numlist = []
    for i in cps: numlist.append(i.num)
    if pn in numlist: return 'bad ptev. cp number!' # фигня, 
                                     # такого быть не может
    if len(cps) == 0:
        cps.add(cp(*args))
    for i in cps: 
        ...
        # Все это надо (было) делать при создании экземпляра..
'''
150223 == Задолбался питонить с планшета.
Идея такая:
* Создаём экземпляр чекпоинта (метод add), 
выбираем за каким чекпоинтом он следует 
(все прочие параметры - не обязательные).
* Если экземпляр единственный - он назначается первым.
* Если нет - все остальные экземпляры перенумеруются 
в соотв. с точкой вставки.
* Если удаляем экземпляр (метод remove) - все прочие перенумерутся.

План выглядит так:
#. Перенумеровывать чекпоинты при вставке.
#. Обновлять расчётные времена при изменении 
опорного времени или любой из дельт.
'''

