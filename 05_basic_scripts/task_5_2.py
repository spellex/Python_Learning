# -*- coding: utf-8 -*-
'''
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

# -*- coding: utf-8 -*-
'''
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

print('введите ip в формате: x.x.x.x/y')

ip_net = input()

# use method spit() and create new list


ip_net_split = ip_net.split('/')

# get the mask number

mask = int(ip_net_split[1])

# use method split() create new list

ip_split = ip_net_split[0].split('.')

# get bin netmask

bin_mask=('1'*mask)+('0'*(32-mask))
bin_mask = ("{0:} {1:} {2:} {3}".format(bin_mask[0:8], bin_mask[8:16], bin_mask[16:24],bin_mask[24:])).split()

# create template from print

template_networ = '''
    Network:
    {ip0:<10} {ip1:<10} {ip2:<10} {ip3:<10}
    {ip0:0>10b} {ip1:0>10b} {ip2:0>10b} {ip3:0>10b}
    Mask:
    /{mask}
    {ip_mask0:<10} {ip_mask1:<10} {ip_mask2:<10} {ip_mask3:<10}
    {bin_mask0:<10} {bin_mask1:<10} {bin_mask2:<10} {bin_mask3:<10}
    '''


print(template_networ.format(ip0=int(ip_split[0]), ip1=int(ip_split[1]), ip2=int(ip_split[2]), ip3=int(ip_split[3]),
                             mask=mask, ip_mask0=int(bin_mask[0], 2), ip_mask1=int(bin_mask[1], 2), ip_mask2=int(bin_mask[2], 2), ip_mask3=int(bin_mask[3], 2),
                             bin_mask0=bin_mask[0], bin_mask1=bin_mask[1], bin_mask2=bin_mask[2], bin_mask3=bin_mask[3]))
