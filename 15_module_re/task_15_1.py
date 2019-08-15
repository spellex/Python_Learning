# -*- coding: utf-8 -*-
'''
Задание 15.1

Создать функцию get_ip_from_cfg, которая ожидает как аргумент имя файла,
в котором находится конфигурация устройства.

Функция должна обрабатывать конфигурацию и возвращать IP-адреса и маски,
которые настроены на интерфейсах, в виде списка кортежей:
* первый элемент кортежа - IP-адрес
* второй элемент кортежа - маска

Например (взяты произвольные адреса):
[('10.0.1.1', '255.255.255.0'), ('10.0.2.1', '255.255.255.0')]

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла config_r1.txt.


Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды, а не ввод пользователя.

'''
import re


def get_ip_from_cfg(file):
    f = open(file)
    b = []
    for line in f:
        a = []
        if line.startswith(' ip address'):
            a.append(re.search('\d+\.\d+\.\d+\.\d+', line).group())
            a.append(re.search('\d+\.\d+\.\d+\.\d+$', line).group())
            b.append(tuple(a))
    f.close()
    return b


if __name__=='__main__':
    print(get_ip_from_cfg('/opt/myallgit/online-7-eugene-zayka/exercises/15_module_re/config_r1.txt'))
