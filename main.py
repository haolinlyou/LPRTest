# -*- coding: utf-8 -*-
# @Author  : lk
# @Email   : lk123400@163.com
# @File    : main.py
# @Time    : 2020/1/6 9:50

from common import get_files


class TestFactory(object):
    """
    简单工厂模式
    """
    @staticmethod
    def get_class(com_class):
        if com_class == 'face++':
            from executor import FaceplusplusTest
            return FaceplusplusTest()
        elif com_class == 'baidu':
            from executor import BaiduTest
            return BaiduTest()


if __name__ == '__main__':
    file_list = get_files('data_img\\')
    test_executor = TestFactory.get_class('face++')
    test_executor.test(file_list)
