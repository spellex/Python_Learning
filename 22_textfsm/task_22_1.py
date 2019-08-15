# -*- coding: utf-8 -*-
'''
Задание 22.1

Создать функцию parse_command_output. Параметры функции:
* template - имя файла, в котором находится шаблон TextFSM
* command_output - вывод соответствующей команды show (строка)

Функция должна возвращать список:
* первый элемент - это список с названиями столбцов
* остальные элементы это списки, в котором находятся результаты обработки вывода

Проверить работу функции на выводе команды output/sh_ip_int_br.txt и шаблоне templates/sh_ip_int_br.template.

'''
import textfsm


def parse_command_output(template, command_output):
    a = []
    with open(template) as template:
        fsm = textfsm.TextFSM(template)
        res = fsm.ParseText(command_output)
        a.append(fsm.header)
        for string in res:
            a.append(string)
        return a


if __name__ == '__main__':
    f = open('/opt/myallgit/online-7-eugene-zayka/exercises/22_textfsm/output/sh_ip_int_br.txt')
    file = f.read()
    print(parse_command_output('/opt/myallgit/online-7-eugene-zayka/exercises/22_textfsm/templates/sh_ip_int_br.template', file))
