# -*- coding: utf-8 -*-
'''
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный файл коммутатора
и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов, а значения access VLAN:
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN:
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
def get_int_vlan_map (config_filename = '/opt/myallgit/online-7-eugene-zayka/exercises/09_functions/config_sw1.txt'):
    f = open(config_filename)
    p = []
    o = []
    i = []
    l = []
    k = []
    t = []
    r = []
    for string in f:
        c = []
        d = []
        if string.startswith('interface FastEthernet'):
            string = string.strip('\n')
            string = string.split(' ')
            string1 = string[-1]
        elif string.startswith(' switchport access'):
            a = string.split()
            o.append(int(a[-1]))
            p.append(string1)
        elif string.startswith(' switchport trunk allowed'):
            b = string.split()
            d.append(b[-1].split(','))
            for x in d[0]:
                c.append(int(x))
            k.append(c)
            l.append(string1)

    t.append(dict(zip(p, o)))
    r.append(dict(zip(l, k)))
    i.append(t[0])
    i.append(r[0])
    result = tuple(i)
    f.close()
    return result
print(get_int_vlan_map('/opt/myallgit/online-7-eugene-zayka/exercises/09_functions/config_sw1.txt'))

