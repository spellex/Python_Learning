# -*- coding: utf-8 -*-

'''
Задание 27.2a

Дополнить класс MyNetmiko из задания 27.2.

Добавить метод _check_error_in_command, который выполняет проверку на такие ошибки:
 * Invalid input detected, Incomplete command, Ambiguous command

Метод ожидает как аргумент команду и вывод команды.
Если в выводе не обнаружена ошибка, метод ничего не возвращает.
Если в выводе найдена ошибка, метод генерирует исключение ErrorInCommand с сообщениеем о том какая ошибка была обнаружена, на каком устройстве и в какой команде.

Переписать метод send_command netmiko, добавив в него проверку на ошибки.

In [2]: from task_27_2a import MyNetmiko

In [3]: r1 = MyNetmiko(**device_params)

In [4]: r1.send_command('sh ip int br')
Out[4]: 'Interface                  IP-Address      OK? Method Status                Protocol\nEthernet0/0                192.168.100.1   YES NVRAM  up                    up      \nEthernet0/1                192.168.200.1   YES NVRAM  up                    up      \nEthernet0/2                190.16.200.1    YES NVRAM  up                    up      \nEthernet0/3                192.168.230.1   YES NVRAM  up                    up      \nEthernet0/3.100            10.100.0.1      YES NVRAM  up                    up      \nEthernet0/3.200            10.200.0.1      YES NVRAM  up                    up      \nEthernet0/3.300            10.30.0.1       YES NVRAM  up                    up      '

In [5]: r1.send_command('sh ip br')
---------------------------------------------------------------------------
ErrorInCommand                            Traceback (most recent call last)
<ipython-input-2-1c60b31812fd> in <module>()
----> 1 r1.send_command('sh ip br')
...
ErrorInCommand: При выполнении команды "sh ip br" на устройстве 192.168.100.1 возникла ошибка "Invalid input detected at '^' marker."

'''
import re
import netmiko
from netmiko.cisco.cisco_ios import CiscoIosBase

device_params = {
    'device_type': 'cisco_ios',
    'ip': '192.168.100.1',
    'username': 'cisco',
    'password': 'cisco',
    'secret': 'cisco'
}


class MyNetmiko(CiscoIosBase):
    def __init__(self, **device_params):
        device_ip = device_params['ip']
        self.ip = device_ip
        super().__init__(**device_params)
        self.ssh = netmiko.ConnectHandler(**device_params)
        self.ssh.enable()

    def _check_error_in_command(self, value, error_command):
        if 'Invalid input detected' in value or 'Incomplete command' in value or 'Ambiguous command' in value:
            reg_string = re.search('(?P<message>%.+)', value)
            raise ErrorInCommand('При выполнении команды ' + error_command + ' на устройстве ' + self.ip +' возникла ошибка ' + reg_string.group('message'))

    def send_command(self, command):
        self._check_error_in_command(self.ssh.send_command(command), command)
        return self.ssh.send_command(command)

    def send_config_set(self, commands):
        return self.ssh.send_config_set(commands)


class ErrorInCommand(Exception):
    pass


if __name__ == '__main__':
    r1 = MyNetmiko(**device_params)
    print(r1.send_command('sh ip br'))
