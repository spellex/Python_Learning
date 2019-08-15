# -*- coding: utf-8 -*-
'''
Задание 20.3

Создать функцию send_command_to_devices, которая отправляет
разные команды show на разные устройства в параллельных потоках,
а затем записывает вывод команд в файл.

Параметры функции:
* devices - список словарей с параметрами подключения к устройствам
* commands_dict - словарь в котором указано на какое устройство отправлять какую команду. Пример словаря - commands
* filename - имя файла, в который будут записаны выводы всех команд
* limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция ничего не возвращает.

Вывод команд должен быть записан в файл в таком формате (перед выводом команды надо написать имя хоста и саму команду):

R1#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.1   YES NVRAM  up                    up
Ethernet0/1                192.168.200.1   YES NVRAM  up                    up
R2#sh arp
Protocol  Address          Age (min)  Hardware Addr   Type   Interface
Internet  192.168.100.1          76   aabb.cc00.6500  ARPA   Ethernet0/0
Internet  192.168.100.2           -   aabb.cc00.6600  ARPA   Ethernet0/0
Internet  192.168.100.3         173   aabb.cc00.6700  ARPA   Ethernet0/0
R3#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.3   YES NVRAM  up                    up
Ethernet0/1                unassigned      YES NVRAM  administratively down down


Для выполнения задания можно создавать любые дополнительные функции.

Проверить работу функции на устройствах из файла devices.yaml и словаре commands
'''
from itertools import repeat
from concurrent.futures import ThreadPoolExecutor
import netmiko
import yaml


def send_command_to_devices(devices,command,filename,limit=3):
    a =[]
    for value in command.values():
        a.append(value)
    f = open(filename, 'w')
    with ThreadPoolExecutor(max_workers=limit) as executor:
        result = executor.map(send_command, devices, a)
        for device_ip,output in zip(devices,result):
            if '100.1' in device_ip['ip']:
                b = 'R1#'+command[device_ip['ip']]+'\n'+output+'\n'
                f.write(b)
            elif '100.2' in device_ip['ip']:
                b = 'R2#'+command[device_ip['ip']]+'\n'+output+'\n'
                f.write(b)
            elif '100.3' in device_ip['ip']:
                b = 'R3#'+command[device_ip['ip']]+'\n'+output+'\n'
                f.write(b)
    f.close()


def send_command(device, show):
    with netmiko.ConnectHandler(**device) as ssh:
        ssh.enable()
        show_result = ssh.send_command(show)
    return(show_result)


if __name__=='__main__':
    commands = {'192.168.100.1': 'sh ip int br',
                '192.168.100.2': 'sh arp',
                '192.168.100.3': 'sh ip int br'}
    with open('/opt/online-7-eugene-zayka/exercises/20_concurrent_connections/devices.yaml') as f:
        devices_send = yaml.safe_load(f)
    send_command_to_devices(devices_send,commands,'/home/python/20_3.txt',3)
