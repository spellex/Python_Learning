# -*- coding: utf-8 -*-
'''
Задание 20.1

Создать функцию ping_ip_addresses, которая проверяет доступность IP-адресов.
Проверка IP-адресов должна выполняться параллельно в разных потоках.

Параметры функции:
* ip_list - список IP-адресов
* limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для выполнения задания можно создавать любые дополнительные функции.

Для проверки доступности IP-адреса, используйте ping.
'''
from concurrent.futures import ThreadPoolExecutor
import subprocess

list_of_ips = ['1.1.1', '8.8.8.8', '8.8.4.4', '8.8.7.1']


def ping_ip_addresses(ip_list, limit=3):
    good_ip = []
    bad_ip = []
    all_ip = []
    with ThreadPoolExecutor(max_workers=limit) as executor:
        result = executor.map(ping_ip, ip_list)
        for status, string_ip in result:
            if status == 1:
                good_ip.append(string_ip)
            else:
                bad_ip.append(string_ip)
        all_ip.append(good_ip)
        all_ip.append(bad_ip)
    return tuple(all_ip)


def ping_ip(ip):
    res = subprocess.call(['ping', '-c', '1', '-n', ip], stdout=subprocess.DEVNULL)
    if res == 0:
        a = 1
    else:
        a = 2
    return a, ip


if __name__ == '__main__':
    print(ping_ip_addresses(list_of_ips, 4))
