# -*- coding: utf-8 -*-
'''
Задание 20.2

Создать функцию send_show_command_to_devices, которая отправляет
одну и ту же команду show на разные устройства в параллельных потоках,
а затем записывает вывод команд в файл.

Параметры функции:
* devices - список словарей с параметрами подключения к устройствам
* command - команда
* filename - имя файла, в который будут записаны выводы всех команд
* limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция ничего не возвращает.

Вывод команд должен быть записан в файл в таком формате (перед выводом команды надо написать имя хоста и саму команду):

R1#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.1   YES NVRAM  up                    up
Ethernet0/1                192.168.200.1   YES NVRAM  up                    up
R2#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.2   YES NVRAM  up                    up
Ethernet0/1                10.1.1.1        YES NVRAM  administratively down down
R3#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.3   YES NVRAM  up                    up
Ethernet0/1                unassigned      YES NVRAM  administratively down down

Для выполнения задания можно создавать любые дополнительные функции.

Проверить работу функции на устройствах из файла devices.yaml
'''
from itertools import repeat
from concurrent.futures import ThreadPoolExecutor
import netmiko
import yaml


def send_show_command_to_devices(devices,command,filename,limit=3):
    f = open(filename, 'w')
    with ThreadPoolExecutor(max_workers=limit) as executor:
        result = executor.map(send_show, devices, repeat(command))
        for device_ip,output in zip(devices,result):
            if '100.1' in device_ip['ip']:
                a = 'R1#'+command+'\n'+output+'\n'
                f.write(a)
            elif '100.2' in device_ip['ip']:
                a = 'R2#'+command+'\n'+output+'\n'
                f.write(a)
            elif '100.3' in device_ip['ip']:
                a = 'R3#'+command+'\n'+output+'\n'
                f.write(a)
    f.close()


def send_show(device, show):
    with netmiko.ConnectHandler(**device) as ssh:
        ssh.enable()
        show_result = ssh.send_command(show)
    return show_result


if __name__=='__main__':
    with open('/opt/online-7-eugene-zayka/exercises/20_concurrent_connections/devices.yaml') as f:
        devices_send = yaml.safe_load(f)
    send_show_command_to_devices(devices_send,'sh ip int br','/home/python/20_2.txt',3)
