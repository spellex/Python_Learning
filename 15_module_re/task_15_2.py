# -*- coding: utf-8 -*-
'''
Задание 15.2

Создать функцию parse_sh_ip_int_br, которая ожидает как аргумент
имя файла, в котором находится вывод команды show ip int br

Функция должна обрабатывать вывод команды show ip int br и возвращать такие поля:
* Interface
* IP-Address
* Status
* Protocol

Информация должна возвращаться в виде списка кортежей:
[('FastEthernet0/0', '10.0.1.1', 'up', 'up'),
 ('FastEthernet0/1', '10.0.2.1', 'up', 'up'),
 ('FastEthernet0/2', 'unassigned', 'down', 'down')]

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла sh_ip_int_br.txt.

'''
import re
from pprint import pprint


def parse_sh_ip_int_br(file):
    f = open(file)
    a = []
    for line in f:
        if re.search(('FastEthernet|Loopback' ), line):
            b = []
            match = re.search('(?P<Interface>\S+)\s+(?P<Address>[\d.]|\S+)\s+(?P<OK>\S+)\s+(?P<Method>\S+)\s+(?P<Status>\S+)\s+(?P<Status1>\S+)', line)

            if match.group('Status').startswith('administratively'):
                match = re.search('(?P<Interface>\S+)\s+(?P<Address>[\d.]|\S+)\s+(?P<OK>\S+)\s+(?P<Method>\S+)\s+(?P<Status>\S+\s\S+)\s+(?P<Status1>\S+)', line)
            b.append(match.group('Interface'))
            b.append(match.group('Address'))
            b.append(match.group('Status'))
            b.append(match.group('Status1'))
            a.append(tuple(b))
    f.close()
    return a


if __name__=='__main__':
    pprint(parse_sh_ip_int_br('/opt/myallgit/online-7-eugene-zayka/exercises/15_module_re/sh_ip_int_br.txt'))


