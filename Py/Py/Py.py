import numpy as np
from PIL import Image
import random

'''
    @Author:王磊
    @Time  :2018/11/15 12:30:05
'''


def getRandArr():
    '''返回随机颜色数组'''
    return np.full((1, 3), random.randint(0, 255))


def method1(depts, start, end):
    '''
    :param depts: 马瑟克块元素大小
    :param start: 马赛克横坐标起点元组
    :param end: 马赛克纵坐标起始点元组
    :return:
    '''
    im1 = np.array(Image.open("C:\\Users\\Thinkpad-65\\Desktop\\888.jpg"))
    for i in range(start[0], start[1], depts):
        for j in range(end[0], end[1], depts):
            im1[i:i + depts, j:j + depts] = getRandArr()
    im2 = Image.fromarray(im1.astype("uint8"))
    im2.show()


def method2(depts, start, end):
    '''
    :param depts: 马瑟克块元素大小
    :param start: 马赛克横坐标起点元组
    :param end: 马赛克纵坐标起始点元组
    :return:
    主要通过中间值的rgb对局部范围块的rgb做修改，depts值越小越精确
    '''
    im1 = np.array(Image.open("C:\\Users\\Thinkpad-65\\Desktop\\888.jpg"))
    for i in range(start[0], start[1], depts):
        for j in range(end[0], end[1], depts):
            im1[i:i + depts, j:j + depts] = im1[i + (depts // 2)][j + (depts // 2)]
    im2 = Image.fromarray(im1.astype("uint8"))
    im2.show()


if __name__ == '__main__':
    '''相对方法来说，方法2更实用'''
    '''方法1（通过随机颜色值对选中范围打马赛克）'''
    #method1(20, (200, 300), (140, 240))
    '''方法2（通过选中范围的中间值颜色数组打马赛克）'''
    method2(15, (200, 300), (140, 240))