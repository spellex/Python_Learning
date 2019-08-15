# -*- coding: utf-8 -*-
'''
Задание 19.1

Создать функцию send_show_command.

Функция подключается по SSH (с помощью netmiko) к одному устройству и выполняет указанную команду.

Параметры функции:
* device - словарь с параметрами подключения к устройству
* command - команда, которую надо выполнить

Функция возвращает строку с выводом команды.

Скрипт должен отправлять команду command на все устройства из файла devices.yaml с помощью функции send_show_command.

'''
import getpass
import sys
from netmiko import ConnectHandler
import yaml
from pprint import pprint

command = 'sh ip int br'


def send_show_command(device, command):
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        result = ssh.send_command(command)
    return result


if __name__=='__main__':
    with open('/opt/online-7-eugene-zayka/exercises/19_ssh_telnet/devices.yaml') as f:
        templates = yaml.safe_load(f)
    for string in templates:
        send_show_command(string, command)
