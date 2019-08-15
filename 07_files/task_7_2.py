# -*- coding: utf-8 -*-
'''
Задание 7.2

Создать скрипт, который будет обрабатывать конфигурационный файл config_sw1.txt:
- имя файла передается как аргумент скрипту

Скрипт должен возвращать на стандартный поток вывода команды из переданного
конфигурационного файла, исключая строки, которые начинаются с '!'.

Между строками не должно быть дополнительного символа перевода строки.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

# open file
f = open('/opt/myallgit/online-7-eugene-zayka/exercises/07_files/config_sw1.txt')

# read the string from file
for string in f:

    # no string with "!"
    if string[0] == '!':
        pass
    else:
        # delete extra characters and display result
        string = string.strip('\n')
        print(string)

f.close()

