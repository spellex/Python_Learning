# -*- coding: utf-8 -*-
'''
Задание 15.3

Создать функцию convert_ios_nat_to_asa, которая конвертирует правила NAT из синтаксиса cisco IOS в cisco ASA.

Функция ожидает такие аргументы:
- имя файла, в котором находится правила NAT Cisco IOS
- имя файла, в который надо записать полученные правила NAT для ASA

Функция ничего не возвращает.

Проверить функцию на файле cisco_nat_config.txt.

Пример правил NAT cisco IOS
ip nat inside source static tcp 10.1.2.84 22 interface GigabitEthernet0/1 20022
ip nat inside source static tcp 10.1.9.5 22 interface GigabitEthernet0/1 20023

И соответствующие правила NAT для ASA:
object network LOCAL_10.1.2.84
 host 10.1.2.84
 nat (inside,outside) static interface service tcp 22 20022
object network LOCAL_10.1.9.5
 host 10.1.9.5
 nat (inside,outside) static interface service tcp 22 20023

В файле с правилами для ASA:
- не должно быть пустых строк между правилами
- перед строками "object network" не должны быть пробелы
- перед остальными строками должен быть один пробел

Во всех правилах для ASA интерфейсы будут одинаковыми (inside,outside).
'''

import re


def convert_ios_nat_to_asa(file, file1='/home/esz/cisco_asa_nat_config.txt') -> object:
    f = open(file)
    f1 = open(file1, 'w')
    a = []
    for line in f:
        b = 'object network LOCAL_'
        c = ' host '
        d = ' nat (inside,outside) static interface service tcp '
        match = re.search('(?P<Address>\d+\.\d+\.\d+\.\d+)\s+(?P<Port>\d+)\s+(?P<int>\S+\s+\S+)\s+(?P<Port1>\d+)', line)
        a.append(b+match.group('Address'))
        a.append(c+match.group('Address'))
        a.append(d+match.group('Port')+' '+match.group('Port1'))
    for string in a:
        f1.write(string + '\n')
    f.close()
    f1.close()


if __name__=='__main__':
    convert_ios_nat_to_asa('/opt/myallgit/online-7-eugene-zayka/exercises/15_module_re/cisco_nat_config.txt')
