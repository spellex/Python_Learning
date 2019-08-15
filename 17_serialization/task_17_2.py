# -*- coding: utf-8 -*-
'''
Задание 17.2

Создать функцию parse_sh_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

Функция ожидает, как аргумент, вывод команды одной строкой (не имя файла).
Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:
{'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
        'Fa 0/2': {'R6': 'Fa 0/0'}}}

Интерфейсы должны быть записаны с пробелом. То есть, так Fa 0/0, а не так Fa0/0.


Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt
'''
import csv
import re
from pprint import pprint


def parse_sh_cdp_neighbors(file):
    file = file.split('\n')
    host_port_dict = {}
    sw_dict = {}
    for string in file:
        neighbor_dict = {}
        if re.search('\S\d+\s', string):
            match = re.search('(?P<neighbor>\S+\d+)\s+(?P<host_port>\S+\s\S+)', string)
            match1 = re.search('\S+\s\S+$', string)
            neighbor = match.group('neighbor')
            host_port = match.group('host_port')
            neighbor_port = match1.group()
            neighbor_dict[neighbor] = neighbor_port
            host_port_dict[host_port] =neighbor_dict
    sw_dict['SW1'] = host_port_dict
    return sw_dict


if __name__=='__main__':
    with open('/opt/myallgit/online-7-eugene-zayka/exercises/17_serialization/sh_cdp_n_sw1.txt') as f:
        parse_sh_cdp_neighbors(f.read())
