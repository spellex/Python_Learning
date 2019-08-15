# -*- coding: utf-8 -*-
'''
Задание 22.3

Создать функцию parse_command_dynamic.

Параметры функции:
* command_output - вывод команды (строка)
* attributes_dict - словарь атрибутов, в котором находятся такие пары ключ-значение:
 * 'Command': команда
 * 'Vendor': вендор
* index_file - имя файла, где хранится соответствие между командами и шаблонами. Значение по умолчанию - "index"
* templ_path - каталог, где хранятся шаблоны. Значение по умолчанию - templates

Функция должна возвращать список словарей с результатами обработки вывода команды (как в задании 22.1a):
* ключи - имена переменных в шаблоне TextFSM
* значения - части вывода, которые соответствуют переменным

Проверить работу функции на примере вывода команды sh ip int br.
'''
import clitable


def parse_command_dynamic(command_output, attributes_dict, index_file='index', templ_path='templates'):
    cli_table = clitable.CliTable(index_file, templ_path)
    cli_table.ParseCmd(command_output, attributes_dict)
    a = list(cli_table.header)
    res = [list(row) for row in cli_table]
    a_all = []
    for list1 in res:
        a_dict = {}
        i = 0
        for string in list1:
            a_dict[a[i]] = string
            i = i+1
        a_all.append(a_dict)
    return a_all


if __name__ == '__main__':
    attributes = {'Command': 'show ip int br', 'Vendor': 'cisco_ios'}
    f = open('/opt/myallgit/online-7-eugene-zayka/exercises/22_textfsm/output/sh_ip_int_br.txt')
    file = f.read()
    parse_command_dynamic(file, attributes, 'index', '/opt/myallgit/online-7-eugene-zayka/exercises/22_textfsm/templates/')
