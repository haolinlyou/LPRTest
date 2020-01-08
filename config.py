# -*- coding: utf-8 -*-
# @Author  : lk
# @Email   : lk123400@163.com
# @File    : config.py
# @Time    : 2020/1/6 10:44

# coding: utf-8

class FaceplusplusConfig():
    # NOTE: 请替换成您在face++人工智能开放平台控制台创建的API_KEY和API_SECRET
    API_KEY = 'FEIt6wDu3dScwxVQrXm3Er2lS2jaWt5V'
    API_SECRET = 'Dx-H6v6f4UrELWvV83RvEiOSPjwjm5_v'

    BEAUTIFY_PATH = 'https://api-cn.faceplusplus.com/facepp/v1/beautify'
    MERGEFACE_PATH = 'https://api-cn.faceplusplus.com/imagepp/v1/mergeface'
    SEGMENT_PATH = 'https://api-cn.faceplusplus.com/humanbodypp/v2/segment'
    GESTURE_PATH = 'https://api-cn.faceplusplus.com/humanbodypp/v1/gesture'
    SKELETON_PATH = 'https://api-cn.faceplusplus.com/humanbodypp/v1/skeleton'
    THOUSANDLANDMARK_PATH = 'https://api-cn.faceplusplus.com/facepp/v1/face/thousandlandmark'
    DETECT_PATH = 'https://api-cn.faceplusplus.com/facepp/v3/detect'
    SEARCH_PATH = 'https://api-cn.faceplusplus.com/facepp/v3/search'
    FACESET_CREATE_PATH = 'https://api-cn.faceplusplus.com/facepp/v3/faceset/create'
    LPR_PATH = 'https://api-cn.faceplusplus.com/imagepp/v1/licenseplate'

    COLOR_DICT = {0: "蓝色", 1: "黄色", 2: "黑色", 3: "白色", 4: "绿色",
                  5: "小型新能源", 6: "大型新能源", 7: "缺失", 8: "无效"}

class BaiduConfig:
    API_KEY = 'PenayiBMkMUj0f4kXwOou0Bp'
    API_SECRET = 'kRuOW9indgDslC5WzCmUqt6RHr43qyl6'
    LPR_PATH = 'https://aip.baidubce.com/rest/2.0/ocr/v1/license_plate'

DELAY=40

