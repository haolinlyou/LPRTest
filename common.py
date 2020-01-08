# -*- coding: utf-8 -*-
# @Author  : lk
# @Email   : lk123400@163.com
# @File    : common.py
# @Time    : 2020/1/6 10:38

import os


def get_files(dir_name):
    files = os.listdir(dir_name)
    return list(map(lambda x: os.path.join(dir_name, x), files))


def get_input_file_path(dir_name, file_name):
    exts = ['.png', '.jpg']
    for ext in exts:
        if os.path.exists(dir_name + '/' + file_name + ext):
            return dir_name + '/' + file_name + ext
