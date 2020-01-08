# -*- coding: utf-8 -*-
# @Author  : lk
# @Email   : lk123400@163.com
# @File    : executor.py
# @Time    : 2020/1/6 16:36

import abc
import requests
import config
import time
import base64

class AbstractTest():
    """
    抽象类
    """
    @abc.abstractclassmethod
    def __init__(self):
        pass

    @abc.abstractclassmethod
    def test(self):
        """
        抽象方法,用来测试的执行
        :return:
        """
        pass

    @abc.abstractclassmethod
    def send_post(self, params):
        """
        抽象方法，向服务发送请求
        :param params:
        :return:
        """
        pass

    @abc.abstractclassmethod
    def parser_response(self):
        """
        抽象方法，解析响应
        :return:
        """
        pass


class FaceplusplusTest(AbstractTest):
    """
    旷视测试
    检测图片中的车牌，并返回车牌边框坐标、车牌号码、车牌颜色，车牌类型等信息。
    支持识别各种位置、白天以及夜间的车牌识别
    支持蓝、黄、使领管、警车、港澳通行车辆
    """
    def __init__(self):
        self.url = config.FaceplusplusConfig.LPR_PATH
        self.data = {
            'api_key': config.FaceplusplusConfig.API_KEY,
            'api_secret': config.FaceplusplusConfig.API_SECRET,
            'return_gesture': 0
        }

    def test(self, file_list):

        for filename in file_list:
            time.sleep(config.DELAY)
            print(filename)
            files = {
                'image_file': open(filename, 'rb').read()
            }
            #while (self.send_post(files)) and status == 200:
            status, response_json = self.send_post(files)
            print(status, response_json)
            self.parser_response(response_json, filename)

    def send_post(self, files):
        response = requests.post(self.url, data=self.data, files=files)
        return response.status_code, response.json()

    def parser_response(self, response_json, filename):
        try:
            for i, res in enumerate(response_json['results']):
                color = res['color']
                license_plate_number = res['license_plate_number']
                bbox = [res['bound']['left_top'],
                        res['bound']['right_top'],
                        res['bound']['right_bottom'],
                        res['bound']['left_bottom']]
                print('%s-- box:%s, license_plate_number:%s, color:%s\n' % (i, bbox, license_plate_number, color))
                with open('res\\%s.txt' % self.__class__.__name__, 'a+') as f:
                    lines = '%s %s %s %s\n' \
                            % (filename.split('\\')[-1], bbox, license_plate_number, color)
                    f.writelines(lines)
        except BaseException as e:
            with open('res\\%s.txt' % self.__class__.__name__, 'a+') as f:
                lines = '%s "error_message":"%s"\n' %(filename.split('\\')[-1], response_json['error_message'])
                f.writelines(lines)


class BaiduTest(AbstractTest):
    """
    旷视测试
    检测图片中的车牌，并返回车牌边框坐标、车牌号码、车牌颜色，车牌类型等信息。
    支持识别各种位置、白天以及夜间的车牌识别
    支持蓝、黄、使领管、警车
    """
    def __init__(self):
        host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=%s&client_secret=%s'%(
            config.BaiduConfig.API_KEY, config.BaiduConfig.API_SECRET
        )
        token = requests.get(host).json()
        self.url = config.BaiduConfig.LPR_PATH + "?access_token=" + token['access_token']
        self.headers = {'content-type': 'application/x-www-form-urlencoded'}


    def test(self, file_list):
        for filename in file_list:
            time.sleep(config.DELAY)
            print(filename)
            img = open(filename, 'rb').read()
            params = {
                'image': base64.b64encode(img)
            }
            #while (self.send_post(files)) and status == 200:
            status, response_json = self.send_post(params)
            print(status, response_json)
            self.parser_response(response_json, filename)

    def send_post(self, params):
        response = requests.post(self.url, data=params, headers=self.headers)
        return response.status_code, response.json()

    def parser_response(self, response_json, filename):
        with open('res\\%s.txt' % self.__class__.__name__, 'a+') as f:
            try:
                res = response_json['words_result']
                color = res['color']
                license_plate_number = res['number']
                bbox = res['vertexes_location']
                print('%s box:%s, license_plate_number:%s, color:%s\n' % (filename.split('\\')[-1], bbox, license_plate_number, color))
                lines = '%s %s %s %s\n' \
                        % (filename.split('\\')[-1], bbox, license_plate_number, color)
            except BaseException as e:
                lines = '%s "error_message":"%s"\n' %(filename.split('\\')[-1], response_json['error_msg'])
            finally:
                f.writelines(lines)

