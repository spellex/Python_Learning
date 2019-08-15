# -*- coding: utf-8 -*-
'''
Задание 21.1

Создать функцию generate_config.

Параметры функции:
* template - путь к файлу с шаблоном (например, "templates/for.txt")
* data_dict - словарь со значениями, которые надо подставить в шаблон

Функция должна возвращать строку с конфигурацией, которая была сгенерирована.

Проверить работу функции на шаблоне templates/for.txt и данных из файла
data_files/for.yml.

'''
from jinja2 import Environment, FileSystemLoader
import yaml


def generate_config(template, data_dict):
    env = Environment(loader=FileSystemLoader('/opt/myallgit/online-7-eugene-zayka/exercises/21_jinja2/'), trim_blocks=True, lstrip_blocks=True)
    template_r1 = env.get_template(template)
    return template_r1.render(data_dict)


if __name__ == '__main__':
    router_1 = yaml.load(open('/opt/myallgit/online-7-eugene-zayka/exercises/21_jinja2/data_files/for.yml'))
    generate_config('templates/for.txt', router_1)
