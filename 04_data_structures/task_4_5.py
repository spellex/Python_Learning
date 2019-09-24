# -*- coding: utf-8 -*-
'''
Задание 4.5

Из строк command1 и command2 получить список VLANов,
которые есть и в команде command1 и в команде command2.

Результатом должен быть список: ['1', '3', '8']

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

command1 = 'switchport trunk allowed vlan 1,2,3,5,8'
command2 = 'switchport trunk allowed vlan 1,3,8,9'

# use method split ()

command1_split = command1.split()
command2_split = command2.split()

# use method split (','), use a slice and create new list

vlan1 = command1_split[-1].split(',')
vlan2 = command2_split[-1].split(',')

# create a set from the list

vlan1_set = set(vlan1)
vlan2_set = set(vlan2)

# get the intersection of sets

vlan_set = vlan1_set&vlan2_set

# create a list from set

vlan = list(vlan_set)

print(vlan)

