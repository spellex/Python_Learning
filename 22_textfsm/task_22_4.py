# -*- coding: utf-8 -*-
'''
Задание 22.4

Создать функцию send_and_parse_show_command.

Параметры функции:
* device_dict - словарь с параметрами подключения к одному устройству
* command - команда, которую надо выполнить
* templates_path - путь к каталогу с шаблонами TextFSM

Функция должна подключаться к одному устройству, отправлять команду show с помощью netmiko,
а затем парсить вывод команды с помощью TextFSM.

Функция должна возвращать список словарей с результатами обработки вывода команды (как в задании 22.1a):
* ключи - имена переменных в шаблоне TextFSM
* значения - части вывода, которые соответствуют переменным

Проверить работу функции на примере вывода команды sh ip int br и устройствах из devices.yaml.
'''
import textfsm
from netmiko import ConnectHandler
import yaml
from pprint import pprint


def send_and_parse_show_command(device_dict, command, templ_path):
    a_all = []
    with ConnectHandler(**device_dict) as ssh:
        ssh.enable()
        result = ssh.send_command(command)
    with open(templ_path+'/sh_ip_int_br.template') as template:
        fsm = textfsm.TextFSM(template)
        res = fsm.ParseText(result)
        a = fsm.header
        for list in res:
            a_dict = {}
            i = 0
            for string in list:
                a_dict[a[i]] = string
                i = i+1
            a_all.append(a_dict)
    return a_all


if __name__ == '__main__':
    with open('/opt/online-7-eugene-zayka/exercises/22_textfsm/devices.yaml') as f:
        devices = yaml.safe_load(f)
        for device in devices:
            send_and_parse_show_command(device,'sh ip int br', '/opt/online-7-eugene-zayka/exercises/22_textfsm/templates')
