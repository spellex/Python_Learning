# -*- coding: utf-8 -*-
'''
Задание 11.1

Создать функцию parse_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

У функции должен быть один параметр command_output, который ожидает как аргумент вывод команды одной строкой (не имя файла). Для этого надо считать все содержимое файла в строку.

Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:

    {('R4', 'Fa0/1'): ('R5', 'Fa0/1'),
     ('R4', 'Fa0/2'): ('R6', 'Fa0/0')}

В словаре интерфейсы должны быть записаны без пробела между типом и именем. То есть так Fa0/0, а не так Fa 0/0.

Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''


def parse_cdp_neighbors(command_output):
    r = []
    r1 = []
    sh_cdp_n_sw1 = command_output.split('\n')
    for string in sh_cdp_n_sw1:
        string = string.strip('\n')
        if string.endswith('show cdp neighbors'):
            string = string.split('>')
            s = string[0]
        elif string.startswith('R') or string.startswith('S'):
            w = []
            w1 = []
            string = string.split()
            g = string[1] + string[2]
            d = string[-2] + string[-1]
            w.append(s)
            w.append(g)
            w1.append(string[0])
            w1.append(d)
            r.append(tuple(w))
            r1.append(tuple(w1))
    result = dict(zip(r, r1))
    return result


if __name__=='__main__':
    with open('/opt/myallgit/online-7-eugene-zayka/exercises/11_modules/sh_cdp_n_sw1.txt') as f:
        print(parse_cdp_neighbors(f.read()))
