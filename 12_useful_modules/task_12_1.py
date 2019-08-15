# -*- coding: utf-8 -*-
'''
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет доступность IP-адресов.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте ping.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

import subprocess


def ping_ip_addresses(ipadd):
    alive = []
    unreachable = []
    result = []

    for ip in ipadd:
        reply = subprocess.run(['ping', '-c', '3', '-n', ip], stdout=subprocess.DEVNULL)

        if reply.returncode == 0:
            alive.append(ip)
        else:
            unreachable.append(ip)

    result.append(alive)
    result.append(unreachable)
    result = tuple(result)
    return result


list_of_ips = ['1.1.1', '8.8.8.8', '8.8.4.4', '8.8.7.1']
print(ping_ip_addresses(list_of_ips))
