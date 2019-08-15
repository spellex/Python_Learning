# -*- coding: utf-8 -*-
'''
Задание 19.1a

Скопировать функцию send_show_command из задания 19.1 и переделать ее таким образом,
чтобы обрабатывалось исключение, которое генерируется
при ошибке аутентификации на устройстве.

При возникновении ошибки, на стандартный поток вывода должно выводиться сообщение исключения.

Для проверки измените пароль на устройстве или в файле devices.yaml.
'''
import getpass
import sys
from netmiko import ConnectHandler
import yaml
from pprint import pprint

command = 'sh ip int br'


def send_show_command(device, command):
    try:
        with ConnectHandler(**device) as ssh:
            ssh.enable()
            result = ssh.send_command(command)
        return result
    except Exception as e:
        print(e)


if __name__=='__main__':
    with open('/opt/online-7-eugene-zayka/exercises/19_ssh_telnet/devices.yaml') as f:
        templates = yaml.safe_load(f)
    for string in templates:
        send_show_command(string, command)
