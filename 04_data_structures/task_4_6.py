# -*- coding: utf-8 -*-
'''
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface     FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'

#delete space and "," and "[]"

ospf_route1 = ospf_route.split()

ospf_route1[0] = 'OSPF'
ospf_route1[2] = ospf_route1[2].strip('[]')
ospf_route1[4] = ospf_route1[4].strip(',')
ospf_route1[5] = ospf_route1[5].strip(',')

#create tamplate from format

template = '''
Protocol:              {:15}
Prefix:                {:15}
AD/Metric:             {:15}
Next-Hop:              {:15}
Last update:           {:15}
Outbound Interface     {:15}
'''

print(template.format(ospf_route1[0],ospf_route1[1],ospf_route1[2],ospf_route1[4],ospf_route1[5],ospf_route1[6]))
