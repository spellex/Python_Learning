# -*- coding: utf-8 -*-
'''
Задание 7.1

Аналогично заданию 4.6 обработать строки из файла ospf.txt
и вывести информацию по каждой в таком виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
# open file
f = open('/opt/myallgit/online-7-eugene-zayka/exercises/07_files/ospf.txt')

# read line from file
# -*- coding: utf-8 -*-
'''
Задание 7.1

Аналогично заданию 4.6 обработать строки из файла ospf.txt
и вывести информацию по каждой в таком виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
# open file
f = open('/opt/myallgit/online-7-eugene-zayka/exercises/07_files/ospf.txt')

# read the string from file
for ospf_route in f:

# create template
    output = '''
    {:25} {}
    {:25} {}
    {:25} {}
    {:25} {}
    {:25} {}
    {:25} {}
    '''

# delete extra characters and assign variables

    _, prefix, ad_metric, _, nhop, update, intf  = (ospf_route.replace(',', ' ').replace('[', '').replace(']', '')).split()

# display the result

    print(output.format("Protocol:", "OSPF",
                        "Prefix:", prefix,
                        "AD/Metric:", ad_metric,
                        "Next-Hop:", nhop,
                        "Last update:", update,
                        "Outbound Interface:", intf))

f.close()



