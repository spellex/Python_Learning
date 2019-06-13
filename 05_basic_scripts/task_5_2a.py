# -*- coding: utf-8 -*-
'''
Задание 5.2a

Всё, как в задании 5.2, но, если пользователь ввел адрес хоста, а не адрес сети,
надо преобразовать адрес хоста в адрес сети и вывести адрес сети и маску, как в задании 5.2.

Пример адреса сети (все биты хостовой части равны нулю):
* 10.0.1.0/24
* 190.1.0.0/16

Пример адреса хоста:
* 10.0.1.1/24 - хост из сети 10.0.1.0/24
* 10.0.5.1/30 - хост из сети 10.0.5.0/30

Если пользователь ввел адрес 10.0.1.1/24,
вывод должен быть таким:

Network:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

print('введите ip в формате: x.x.x.x/y')

ip_net = input()

# use method split() and break a string into ip and a mask

ip_net_split = ip_net.split('/')

# get the int mask number

mask = int(ip_net_split[1])

# use method split() and break ip into octets

ip_split = ip_net_split[0].split('.')

# find out how many zeros at the end of the mask
zero_numb = ('0' * (32 - mask))
zero_numb1 = len(zero_numb)

# extract the mask in binary code
bin_mask = ('1' * mask) + zero_numb
bin_mask = ("{0:} {1:} {2:} {3}".format(bin_mask[0:8], bin_mask[8:16], bin_mask[16:24], bin_mask[24:])).split()

# extract the ip network in binary code
bin_host = ("{0:0>8b} {1:0>8b} {2:0>8b} {3:0>8b}".format(int(ip_split[0]), int(ip_split[1]), int(ip_split[2]),
                                                         int(ip_split[3]))).split()
bin_host = ''.join(bin_host)
bin_host = [bin_host[:(-(len(zero_numb)))]] + [zero_numb]
bin_host = ''.join(bin_host)

bin_net = ("{0:} {1:} {2:} {3}".format(bin_host[0:8], bin_host[8:16], bin_host[16:24], bin_host[24:])).split()

# create template from print
template_network = '''
    Network:
    {ip_net0:<8} {ip_net1:<8} {ip_net2:<8} {ip_net3:<8}
    {bin_net0:<8} {bin_net1:<8} {bin_net2:<8} {bin_net3:<8}
    Host:
    {ip0:<8} {ip1:<8} {ip2:<8} {ip3:<8}
    {ip0:0>8b} {ip1:0>8b} {ip2:0>8b} {ip3:0>8b}
    Mask:
    /{mask}
    {ip_mask0:<8} {ip_mask1:<8} {ip_mask2:<8} {ip_mask3:<8}
    {bin_mask0:<8} {bin_mask1:<8} {bin_mask2:<8} {bin_mask3:<8}
    '''

print(template_network.format(
    ip0=int(ip_split[0]), ip1=int(ip_split[1]), ip2=int(ip_split[2]), ip3=int(ip_split[3]),
    mask=mask,
    ip_mask0=int(bin_mask[0], 2), ip_mask1=int(bin_mask[1], 2), ip_mask2=int(bin_mask[2], 2),
    ip_mask3=int(bin_mask[3], 2),
    bin_mask0=bin_mask[0], bin_mask1=bin_mask[1], bin_mask2=bin_mask[2], bin_mask3=bin_mask[3],
    ip_net0=int(bin_net[0], 2), ip_net1=int(bin_net[1], 2), ip_net2=int(bin_net[2], 2), ip_net3=int(bin_net[3], 2),
    bin_net0=bin_net[0], bin_net1=bin_net[1], bin_net2=bin_net[2], bin_net3=bin_net[3])
)
