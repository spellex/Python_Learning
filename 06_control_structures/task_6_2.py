# -*- coding: utf-8 -*-
'''
Задание 6.2

1. Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
2. Определить тип IP-адреса.
3. В зависимости от типа адреса, вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''


# Запрашиваем ip у пользователя
ip = input("Введите ip: ")

# разделяем ip на байты (получаем список)
ip_split = ip.split('.')

# при помощи функции if и elif проверяя различные условия

if int(ip_split[0]) in range(224) and int(ip_split[0]) > 0:
    print('unicast')

elif (int(ip_split[0]) in range(240)) and int(ip_split[0]) > 0 and (int(ip_split[0]) <= 224):
    print('multicast')

elif int(ip_split[0]) == 255 and int(ip_split[1]) == 255 and int(ip_split[2]) == 255 and int(ip_split[3]) == 255:
    print('local broadcast')

elif int(ip_split[0]) == 0 and int(ip_split[1]) == 0 and int(ip_split[2]) == 0 and int(ip_split[3]) == 0:
    print('unassigned')

else:
    print('unused')

