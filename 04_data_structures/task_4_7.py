# -*- coding: utf-8 -*-
'''
Задание 4.7

Преобразовать MAC-адрес mac в двоичную строку такого вида:
'101010101010101010111011101110111100110011001100'

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

mac = 'AAAA:BBBB:CCCC'

# delete ":" use method replace

mac_replace = mac.replace(':', '')

# make make nuber, use int
mac_int = int(mac_replace, 16)

# convert to binary number, use bin()
mac_bin = bin(mac_int)

print(mac_bin)

