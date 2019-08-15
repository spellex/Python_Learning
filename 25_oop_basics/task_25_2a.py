# -*- coding: utf-8 -*-

'''
Задание 25.2a

Скопировать класс CiscoTelnet из задания 25.2 и изменить метод send_show_command добавив два параметра:

* parse - контролирует то, будет возвращаться обычный вывод команды или список словарей, полученные после обработки с помощью TextFSM. При parse=True должен возвращаться список словарей, а parse=False обычный вывод
* templates - путь к каталогу с шаблонами



Пример создания экземпляра класса:

In [1]: r1_params = {
   ...:     'ip': '192.168.100.1',
   ...:     'username': 'cisco',
   ...:     'password': 'cisco',
   ...:     'secret': 'cisco'}

In [2]: from task_25_2a import CiscoTelnet

In [3]: r1 = CiscoTelnet(**r1_params)

Использование метода send_show_command:
In [4]: r1.send_show_command('sh ip int br', parse=False)
Out[4]: 'sh ip int br\r\nInterface                  IP-Address      OK? Method Status                Protocol\r\nEthernet0/0                192.168.100.1   YES NVRAM  up                    up      \r\nEthernet0/1                192.168.200.1   YES NVRAM  up                    up      \r\nEthernet0/2                190.16.200.1    YES NVRAM  up                    up      \r\nEthernet0/3                192.168.130.1   YES NVRAM  up                    up      \r\nEthernet0/3.100            10.100.0.1      YES NVRAM  up                    up      \r\nEthernet0/3.200            10.200.0.1      YES NVRAM  up                    up      \r\nEthernet0/3.300            10.30.0.1       YES NVRAM  up                    up      \r\nLoopback0                  10.1.1.1        YES NVRAM  up                    up      \r\nLoopback55                 5.5.5.5         YES manual up                    up      \r\nR1#'

In [5]: r1.send_show_command('sh ip int br', parse=True)
Out[5]:
[{'intf': 'Ethernet0/0',
  'address': '192.168.100.1',
  'status': 'up',
  'protocol': 'up'},
 {'intf': 'Ethernet0/1',
  'address': '192.168.200.1',
  'status': 'up',
  'protocol': 'up'},
 {'intf': 'Ethernet0/2',
  'address': '190.16.200.1',
  'status': 'up',
  'protocol': 'up'},
 {'intf': 'Ethernet0/3',
  'address': '192.168.130.1',
  'status': 'up',
  'protocol': 'up'},
 {'intf': 'Ethernet0/3.100',
  'address': '10.100.0.1',
  'status': 'up',
  'protocol': 'up'},
 {'intf': 'Ethernet0/3.200',
  'address': '10.200.0.1',
  'status': 'up',
  'protocol': 'up'},
 {'intf': 'Ethernet0/3.300',
  'address': '10.30.0.1',
  'status': 'up',
  'protocol': 'up'},
 {'intf': 'Loopback0',
  'address': '10.1.1.1',
  'status': 'up',
  'protocol': 'up'},
 {'intf': 'Loopback55',
  'address': '5.5.5.5',
  'status': 'up',
  'protocol': 'up'}]
'''
import telnetlib
import time
import textfsm
from pprint import pprint

r1_params = {'ip': '192.168.100.1', 'username': 'cisco', 'password': 'cisco', 'secret': 'cisco'}


class CiscoTelnet:

    def __init__(self, ip, username, password, secret):
        self.t = telnetlib.Telnet(ip)
        self.t.read_until(b'Username:')
        self.t.write(username.encode('ascii') + b'\n')
        self.t.read_until(b'Password:')
        self.t.write(password.encode('ascii') + b'\n')
        if secret:
            self.t.write(b'enable\n')
            self.t.read_until(b'Password:')
            self.t.write(secret.encode('ascii') + b'\n')
        time.sleep(1)
        self.t.read_very_eager()

    def send_show_command(self, command, parse, templates='/opt/online-7-eugene-zayka/exercises/25_oop_basics/templates'):
        self.t.write(command.encode('ascii') + b'\n')
        time.sleep(1)
        output = self.t.read_very_eager().decode('ascii')
        a_all = []
        if parse:
            with open(templates+'/sh_ip_int_br.template') as template:
                fsm = textfsm.TextFSM(template)
                res = fsm.ParseText(output)
                a = fsm.header
                for list in res:
                    a_dict = {}
                    i = 0
                    for string in list:
                        a_dict[a[i]] = string
                        i = i+1
                    a_all.append(a_dict)
        else:
            a_all = output

        return a_all

    def _write_line(self, string_to_switch):
        self.t.write(string_to_switch.encode('ascii') + b'\n')


if __name__ == '__main__':
    r1 = CiscoTelnet(**r1_params)
    pprint(r1.send_show_command('sh ip int br', parse=False))
    print('*'*50)
    pprint(r1.send_show_command('sh ip int br', parse=True))
