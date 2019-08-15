# -*- coding: utf-8 -*-
'''
Задание 22.1a

Создать функцию parse_output_to_dict.

Параметры функции:
* template - имя файла, в котором находится шаблон TextFSM
* command_output - вывод соответствующей команды show (строка)

Функция должна возвращать список словарей:
* ключи - имена переменных в шаблоне TextFSM
* значения - части вывода, которые соответствуют переменным

Проверить работу функции на выводе команды output/sh_ip_int_br.txt и шаблоне templates/sh_ip_int_br.template.
'''
import textfsm


def parse_output_to_dict(template, command_output):

    with open(template) as template:
        a_all = []
        fsm = textfsm.TextFSM(template)
        res = fsm.ParseText(command_output)
        a = fsm.header
        for list in res:
            a_dict = {}
            i = 0
            for string in list:
                a_dict[a[i]] = string
                i = i+1
            a_all.append(a_dict)
        return a_all


if __name__ == '__main__':
    f = open('/opt/online-7-eugene-zayka/exercises/22_textfsm/output/sh_ip_int_br.txt')
    file = f.read()
    print(parse_output_to_dict('/opt/online-7-eugene-zayka/exercises/22_textfsm/templates/sh_ip_int_br.template', file))
