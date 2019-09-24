# -*- coding: utf-8 -*-
'''
Задание 4.3

Получить из строки config список VLANов вида:
['1', '3', '10', '20', '30', '100']

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

config = 'switchport trunk allowed vlan 1,3,10,20,30,100'

# use method split (),

nconfig = config.split()

# use method split (','), use a slice and create new list

vlan = nconfig[-1].split(',')

print(vlan)
