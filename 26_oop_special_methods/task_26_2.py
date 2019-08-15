# -*- coding: utf-8 -*-

'''
Задание 26.2

Добавить к классу CiscoTelnet из задания 25.2x поддержку работы в менеджере контекста.
При выходе из блока менеджера контекста должно закрываться соединение.
Все исключения, которые возникли в менеджере контекста, должны генерироваться после выхода из блока with.

Пример работы:

In [14]: r1_params = {
    ...:     'ip': '192.168.100.1',
    ...:     'username': 'cisco',
    ...:     'password': 'cisco',
    ...:     'secret': 'cisco'}

In [15]: from task_26_2 import CiscoTelnet

In [16]: with CiscoTelnet(**r1_params) as r1:
    ...:     print(r1.send_show_command('sh clock'))
    ...:
sh clock
*19:17:20.244 UTC Sat Apr 6 2019
R1#

In [17]: with CiscoTelnet(**r1_params) as r1:
    ...:     print(r1.send_show_command('sh clock'))
    ...:     raise ValueError('Возникла ошибка')
    ...:
sh clock
*19:17:38.828 UTC Sat Apr 6 2019
R1#
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-17-f3141be7c129> in <module>
      1 with CiscoTelnet(**r1_params) as r1:
      2     print(r1.send_show_command('sh clock'))
----> 3     raise ValueError('Возникла ошибка')
      4

ValueError: Возникла ошибка
'''
import telnetlib
import time

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

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.t.close()

    def send_show_command(self, command):
        self.t.write(command.encode('ascii') + b'\n')
        time.sleep(1)
        output = self.t.read_very_eager().decode('ascii')
        return output


if __name__ == '__main__':
    with CiscoTelnet(**r1_params) as r1:
        print(r1.send_show_command('sh clock'))
