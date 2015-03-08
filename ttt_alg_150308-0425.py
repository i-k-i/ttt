# coding:utf

'''
0349 ==
                             ,d      ,d      ,d     
                             88      88      88     
                           MM88MMM MM88MMM MM88MMM  
                             88      88      88     
                             88      88      88     
                             88,     88,     88,    
                             "Y888   "Y888   "Y888  


150308 ==
М.. этот прототип справляется с задачей расчёта времени.
000000 ==
'''


#import pdb
import datetime
d = datetime.datetime.today()




def add(prevnum, name, optime, dtprev):
    '''  Чекпоинты нумеруются, начиная с первого.
    prevnum = 0 => чекпоинт будет первым.
    '''
    print 'adding', prevnum, name, optime, dtprev
    if prevnum > len(a): prevnum = len(a)
    
    optimeOdj = datetime.datetime(d.year, d.month, d.day, optime[0], optime[1])
    dtprevObj = datetime.timedelta(hours=dtprev[0], minutes=dtprev[1])
    a.insert(prevnum, [name, optimeOdj, dtprevObj])
    
    dtsum = datetime.timedelta() # Все, кто правее:
    for c in a[prevnum+1:]: 
        dtsum += c[2]
        c[1] = optimeOdj + dtsum
    
    dtsum = datetime.timedelta() # Все, кто левее:
    for ct in zip(a[0:prevnum][::-1], a[0:prevnum+1][::-1]): # Сдвиг: вычитаем
        c = ct[0]; c1 = ct[1]                                # dt следующего c.
        dtsum += c1[2]
        c[1] = optimeOdj - dtsum
#
#
def edit(num, name, optime, dtprev):
    ''' Чекпоинты нумеруются, начиная с первого.
    '''
    print 'editing', num, name, optime, dtprev
    num = num-1
    if num > len(a): num = len(a)

    optimeOdj = datetime.datetime(d.year, d.month, d.day, optime[0], optime[1])
    dtprevObj = datetime.timedelta(hours=dtprev[0], minutes=dtprev[1])
    a[num] = [name, optimeOdj, dtprevObj]

    dtsum = datetime.timedelta() # Все, кто правее:
    for c in a[num+1:]: 
        dtsum += c[2]
        c[1] = optimeOdj + dtsum

    dtsum = datetime.timedelta() # Все, кто левее:
    for ct in zip(a[0:num][::-1], a[0:num+1][::-1]): # Сдвиг: вычитаем
        c = ct[0]; c1 = ct[1]                        # dt следующего c.
        dtsum += c1[2]
        c[1] = optimeOdj - dtsum
#
#
def delete(num):
    ''' Чекпоинты нумеруются, начиная с первого.
    Опорным чекпоинтом становится первый из оставшихся чекпоинтов.
    '''
    print 'deleting', num

    num = num-1
    if num > len(a): num = len(a)
    del a[num]
    
    optimeOdj = a[0][1]

    dtsum = datetime.timedelta() # Все, кто правее:
    for c in a[1:]: 
        dtsum += c[2]
        c[1] = optimeOdj + dtsum



# Тест 1:
a = []
add (0, 'I', (12, 00), (0, 10))
add (1, 'II', (12, 00), (0, 20))
add (2, 'III', (12, 00), (0, 10))
add (1, 'IV', (12, 00), (0, 20))
add (10, 'V', (12, 00), (0, 10))
add (0, 'VI', (12, 00), (0, 20))
add (5, 'VII', (12, 00), (0, 10))
edit (5, 'new', (00, 00), (0, 45))
delete (2)

# Тест 2. Добавляем события в конец:
a = []
add (100, 'начало сборов', (00,00), (00,10))
add (100, 'выход с раб', (00,00), (00,10))
add (100, 'проход через прох.', (00,00), (00,05))
add (100, 'приход домой', (00,00), (00,05))
add (100, 'выход из дома', (00,00), (00,30))
add (100, 'у макдака', (00,00), (00,12))
add (100, 'закончен перекус', (00,00), (00,20))
add (100, 'сел в поезд м. полеж.', (00,00), (00,05))
add (100, 'на м. волг. пр.', (00,00), (00,21))
add (100, 'геймер', (19,50), (00,10))




print

lenlist = []
for i in a: 
    lenlist.append(len(i[0].decode('utf-8')))

for i in a: # Вывод через .format работал криво. 
            # Ошибка ширины кириллицы. Декодирование.
    print '{0:3d}. '.format(a.index(i)+1),
    print '*' * (max(lenlist) - len(i[0].decode('utf-8'))), i[0],
    if a.index(i)+1 == 1: dttek = ' '
    else: dttek = str(i[2])[::-1][3:][::-1] # Обрезка секунд
    print str(i[1])[10:], ' ',
    print dttek






