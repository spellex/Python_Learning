# -*- coding: utf-8 -*-
'''
Задание 19.2b
Скопировать функцию send_config_commands из задания 19.2a и добавить проверку на ошибки.
При выполнении каждой команды, скрипт должен проверять результат на такие ошибки:
 * Invalid input detected, Incomplete command, Ambiguous command
Если при выполнении какой-то из команд возникла ошибка,
функция должна выводить сообщение на стандартный поток вывода с информацией
о том, какая ошибка возникла, при выполнении какой команды и на каком устройстве, например:
Команда "logging" выполнилась с ошибкой "Incomplete command." на устройстве 192.168.100.1
Ошибки должны выводиться всегда, независимо от значения параметра verbose.
При этом, verbose по-прежнему должен контролировать будет ли выводиться сообщение:
Подключаюсь к 192.168.100.1...
Функция send_config_commands теперь должна возвращать кортеж из двух словарей:
* первый словарь с выводом команд, которые выполнились без ошибки
* второй словарь с выводом команд, которые выполнились с ошибками
Оба словаря в формате:
* ключ - команда
* значение - вывод с выполнением команд
Проверить работу функции можно на одном устройстве.
Пример работы функции send_config_commands:
In [16]: commands
Out[16]:
['logging 0255.255.1',
 'logging',
 'a',
 'logging buffered 20010',
 'ip http server']
In [17]: result = send_config_commands(r1, commands)
Подключаюсь к 192.168.100.1...
Команда "logging 0255.255.1" выполнилась с ошибкой "Invalid input detected at '^' marker." на устройстве 192.168.100.1
Команда "logging" выполнилась с ошибкой "Incomplete command." на устройстве 192.168.100.1
Команда "a" выполнилась с ошибкой "Ambiguous command:  "a"" на устройстве 192.168.100.1
In [18]: pprint(result, width=120)
({'ip http server': 'config term\n'
                    'Enter configuration commands, one per line.  End with CNTL/Z.\n'
                    'R1(config)#ip http server\n'
                    'R1(config)#',
  'logging buffered 20010': 'config term\n'
                            'Enter configuration commands, one per line.  End with CNTL/Z.\n'
                            'R1(config)#logging buffered 20010\n'
                            'R1(config)#'},
 {'a': 'config term\n'
       'Enter configuration commands, one per line.  End with CNTL/Z.\n'
       'R1(config)#a\n'
       '% Ambiguous command:  "a"\n'
       'R1(config)#',
  'logging': 'config term\n'
             'Enter configuration commands, one per line.  End with CNTL/Z.\n'
             'R1(config)#logging\n'
             '% Incomplete command.\n'
             '\n'
             'R1(config)#',
  'logging 0255.255.1': 'config term\n'
                        'Enter configuration commands, one per line.  End with CNTL/Z.\n'
                        'R1(config)#logging 0255.255.1\n'
                        '                   ^\n'
                        "% Invalid input detected at '^' marker.\n"
                        '\n'
                        'R1(config)#'})
In [19]: good, bad = result
In [20]: good.keys()
Out[20]: dict_keys(['logging buffered 20010', 'ip http server'])
In [21]: bad.keys()
Out[21]: dict_keys(['logging 0255.255.1', 'logging', 'a'])
Примеры команд с ошибками:
R1(config)#logging 0255.255.1
                   ^
% Invalid input detected at '^' marker.
R1(config)#logging
% Incomplete command.
R1(config)#a
% Ambiguous command:  "a"
'''

import sys
from netmiko import ConnectHandler
import yaml
from pprint import pprint
import re

commands_with_errors = ['logging 0255.255.1', 'logging', 'a']
correct_commands = ['logging buffered 20010', 'ip http server']
commands = commands_with_errors + correct_commands


def send_config_commands(device, config_commands, verbose=True):
    good_dict = {}
    bad_dict = {}
    all = []
    try:
        if verbose:
            print('Подключаюсь к {}'.format(device['ip']))
        for string in config_commands:
            with ConnectHandler(**device) as ssh:
                ssh.enable()
                result = ssh.send_config_set(string)
                #result=result.split('\n')
                if "% Invalid input detected at '^' marker." in result or '% Ambiguous command:  "a"' in result or '% Incomplete command.' in result:
                    match_command = re.search('R\S+#(?P<command>.+)', result)
                    match_error = re.search('%\s+(?P<error>\S+.+)', result)
                    bad_dict[match_command.group('command')] = result
                    print('Команда "{command}" выполнилась с ошибкой "{error}" на устройстве {ip}'.
                          format(command=match_command.group('command'), error=match_error.group('error'), ip=device['ip']))
                else:
                    match_command = re.search('R\S+#(?P<command>.+)', result)
                    good_dict[match_command.group('command')] = result
        all.append(good_dict)
        all.append(bad_dict)
        return tuple(all)
    except Exception as e:
        print(e)

if __name__=='__main__':
    with open('/opt/online-7-eugene-zayka/exercises/19_ssh_telnet/devices.yaml') as f:
        templates = yaml.safe_load(f)
    for string in templates:
        send_config_commands(string, commands, verbose=False)
