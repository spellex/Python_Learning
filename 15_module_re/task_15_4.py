# -*- coding: utf-8 -*-
'''
Задание 15.4

Создать функцию get_ints_without_description, которая ожидает как аргумент
имя файла, в котором находится конфигурация устройства.


Функция должна обрабатывать конфигурацию и возвращать список имен интерфейсов,
на которых нет описания (команды description).

Пример интерфейса с описанием:
interface Ethernet0/2
 description To P_r9 Ethernet0/2
 ip address 10.0.19.1 255.255.255.0
 mpls traffic-eng tunnels
 ip rsvp bandwidth

Интерфейс без описания:
interface Loopback0
 ip address 10.1.1.1 255.255.255.255

Проверить работу функции на примере файла config_r1.txt.
'''


def get_ints_without_description(file):
    f = open(file)
    a = []
    for line in f:
        line = line.strip('\n')
        if line.startswith('interface'):
            line = line.split(' ')
            a.append(line[-1])
        elif line.startswith(' description'):
            a.pop()
    return a


if __name__=='__main__':
    print(get_ints_without_description('/opt/myallgit/online-7-eugene-zayka/exercises/15_module_re/config_r1.txt'))

