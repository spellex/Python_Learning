# -*- coding: utf-8 -*-
'''
Задание 17.2a

Создать функцию generate_topology_from_cdp, которая обрабатывает вывод команды show cdp neighbor из нескольких файлов и записывает итоговую топологию в один словарь.

Функция generate_topology_from_cdp должна быть создана с параметрами:
* list_of_files - список файлов из которых надо считать вывод команды sh cdp neighbor
* save_to_filename - имя файла в формате YAML, в который сохранится топология.
 * значение по умолчанию - None. По умолчанию, топология не сохраняется в файл
 * топология сохраняется только, если save_to_filename как аргумент указано имя файла

Функция должна возвращать словарь, который описывает соединения между устройствами, независимо от того сохраняется ли топология в файл.

Структура словаря должна быть такой:
{'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
        'Fa 0/2': {'R6': 'Fa 0/0'}},
 'R5': {'Fa 0/1': {'R4': 'Fa 0/1'}},
 'R6': {'Fa 0/0': {'R4': 'Fa 0/2'}}}

Интерфейсы должны быть записаны с пробелом. То есть, так Fa 0/0, а не так Fa0/0.

Проверить работу функции generate_topology_from_cdp на списке файлов:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt
* sh_cdp_n_r4.txt
* sh_cdp_n_r5.txt
* sh_cdp_n_r6.txt

Проверить работу параметра save_to_filename и записать итоговый словарь в файл topology.yaml.

'''
import glob
import yaml
import re
from pprint import pprint

sh_cdp_files = glob.glob('sh_cdp*')


def generate_topology_from_cdp(list_of_files,save_to_filename=None):
    all_dict = {}
    for line in list_of_files:
        match = re.search('n_(?P<hostname>\S+)\.txt', line)
        hostname = match.group('hostname')
        hostname = hostname.upper()
        with open(line) as f:
            f = f.read()
            f = f.split('\n')
            host_port_dict = {}
            host_dict = {}
            for string in f:
                neighbor_dict = {}
                if re.search('\S\d+\s', string):
                    match = re.search('(?P<neighbor>\S+\d+)\s+(?P<host_port>\S+\s\S+)', string)
                    match1 = re.search('\S+\s\S+$', string)
                    neighbor = match.group('neighbor')
                    host_port = match.group('host_port')
                    neighbor_port = match1.group()
                    neighbor_dict[neighbor] = neighbor_port
                    host_port_dict[host_port] = neighbor_dict
            host_dict[hostname] = host_port_dict
            all_dict.update(host_dict)
    if save_to_filename:
        with open(save_to_filename, 'w') as f:
            yaml.dump(all_dict, f)
    return all_dict


if __name__=='__main__':
    generate_topology_from_cdp(sh_cdp_files, '/home/esz/topology.yaml')

