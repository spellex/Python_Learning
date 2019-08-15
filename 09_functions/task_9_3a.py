# -*- coding: utf-8 -*-
'''
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию:
    - добавить поддержку конфигурации, когда настройка access-порта выглядит так:
            interface FastEthernet0/20
                switchport mode access
                duplex auto
      То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
      Пример словаря: {'FastEthernet0/12': 10,
                       'FastEthernet0/14': 11,
                       'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
def get_int_vlan_map (config_filename='/opt/myallgit/online-7-eugene-zayka/exercises/09_functions/config_sw2.txt'):
    f = open(config_filename)
    p = []
    o = []
    i = []
    l = []
    k = []
    t = []
    r = []
    g = []
    for string in f:
        c = []
        d = []
        g.append(string)
        if string.startswith('interface FastEthernet'):
            string = string.strip('\n')
            st1 = string.split(' ')
            string1 = st1[-1]
        elif g[-1].startswith(' duplex auto') and g[-2].startswith(' switchport mode access'):
                o.append(int(1))
                p.append(string1)
                g.append(1)
        elif string.startswith(' switchport access'):
            a = string.split()
            o.append(int(a[-1]))
            p.append(string1)
            #i.append(dict(zip(p, o)))
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
print(get_int_vlan_map('/opt/myallgit/online-7-eugene-zayka/exercises/09_functions/config_sw2.txt'))

