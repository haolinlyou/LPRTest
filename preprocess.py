# -*- coding: utf-8 -*-
# @Author  : lk
# @Email   : lk123400@163.com
# @File    : preprocess.py
# @Time    : 2020/1/6 11:30

import os
import cv2
import numpy as np
from common import get_files


def resize_img(img):

    img_size = img.shape[0:2]
    im_size_min = np.min(img_size)
    im_size_max = np.max(img_size)

    #im_scale = float(2000)/float(im_size_min)
    #if np.round(im_scale*im_size_max) > 3800:
    #    im_scale = float(3800)/float(im_size_max)
    if im_size_max > 2000:
        im_scale = float(2000) / float(im_size_max)
    else:
        im_scale = 1.0
    new_h = int(img_size[0]*im_scale)
    new_w = int(img_size[1]*im_scale)

    new_h = new_h if new_h // 16 == 0 else (new_h // 16 + 1) * 16
    new_w = new_w if new_w // 16 == 0 else (new_w // 16 + 1) * 16
    re_im = cv2.resize(img, (new_w, new_h), interpolation=cv2.INTER_LINEAR)
    return re_im


filenames = get_files('F:\workspace\python\LPRTest\data')
print(filenames)
for filename in filenames:
    '''
    new_filename = filename.replace(')', '')
    os.rename(filename, new_filename)
    '''
    print(filename)
    img = cv2.imread(filename)
    if np.max(img.shape[0:2]) > 2000:
        re_img = resize_img(img)
    else:
        re_img = img.copy()
    save_name = os.path.join('data_img', filename.split('\\')[-1])
    cv2.imwrite(save_name, re_img)




