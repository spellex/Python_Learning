# -*- coding: utf-8 -*-

'''
Задание 26.1a

В этом задании надо сделать так, чтобы экземпляры класса Topology были итерируемыми объектами.
Основу класса Topology можно взять из любого задания 25.1x или задания 26.1.

После создания экземпляра класса, экземпляр должен работать как итерируемый объект.
На каждой итерации должен возвращаться кортеж, который описывает одно соединение.
Порядок вывода соединений может быть любым.


Пример работы класса:

In [1]: top = Topology(topology_example)

In [2]: for link in top:
   ...:     print(link)
   ...:
(('R1', 'Eth0/0'), ('SW1', 'Eth0/1'))
(('R2', 'Eth0/0'), ('SW1', 'Eth0/2'))
(('R2', 'Eth0/1'), ('SW2', 'Eth0/11'))
(('R3', 'Eth0/0'), ('SW1', 'Eth0/3'))
(('R3', 'Eth0/1'), ('R4', 'Eth0/0'))
(('R3', 'Eth0/2'), ('R5', 'Eth0/0'))


Проверить работу класса.
'''

topology_example = {('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
                    ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
                    ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
                    ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
                    ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
                    ('R3', 'Eth0/2'): ('R5', 'Eth0/0'),
                    ('SW1', 'Eth0/1'): ('R1', 'Eth0/0'),
                    ('SW1', 'Eth0/2'): ('R2', 'Eth0/0'),
                    ('SW1', 'Eth0/3'): ('R3', 'Eth0/0')}
from pprint import pprint
import itertools

class Topology:
    def __init__(self, topology_dict):
        self.topology = self._topology_without_dubl(topology_dict)
        a = []
        for key, value in self.topology.items():
            b = []
            b.append(key)
            b.append(value)
            a.append(tuple(b))
        self.list = a

    def _topology_without_dubl(self, topology_dict):
        dictionary_string = []
        for key in topology_dict.keys():
            for value in topology_dict.values():
                if key == value:
                    dictionary_string.append(value)
        dictionary_string = reversed(dictionary_string)
        for string in dictionary_string:
            if string in topology_dict.keys() and string in topology_dict.values():
                del topology_dict[string]
        return topology_dict

    def __iter__(self):
        return iter(self.list)

if __name__ == '__main__':
    top = Topology(topology_example)
    #pprint(top.topology)
    for string in top:
        print(string)
