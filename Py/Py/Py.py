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


def method2(im1, depts,y, x):
    '''
    :param depts: 马瑟克块元素大小
    :param start: 马赛克横坐标起点元组
    :param end: 马赛克纵坐标起始点元组
    :return:
    主要通过中间值的rgb对局部范围块的rgb做修改，depts值越小越精确
    '''

    for i in range(y[0], y[1], depts):
        for j in range(x[0], x[1], depts):
            im1[i:i + depts, j:j + depts] = 0 #im1[i + (depts // 2)][j + (depts // 2)]
    #im2 = Image.fromarray(im1.astype("uint8"))

    for i in range(y[2], y[3], depts):
        for j in range(x[2], x[3], depts):
            im1[i:i + depts, j:j + depts] = 0 #im1[i + (depts // 2)][j + (depts // 2)]
    im2 = Image.fromarray(im1.astype("uint8"))
    return im2


if __name__ == '__main__':
    '''相对方法来说，方法2更实用'''
    '''方法1（通过随机颜色值对选中范围打马赛克）'''
    #method1(20, (200, 300), (140, 240))

    #im1 = np.array(Image.open("d:\\My Pictures\\screenshot\\pic3639.png"))
    img = np.array(Image.open("d:\\My Documents\\BaiduCloud\\SICOD\\GitHub\\Py\\test666\\888.jpg"))

    '''方法2（通过选中范围的中间值颜色数组打马赛克）'''
    #(depts, (start-y, end-y), (start-x, end-x)
    img2 = method2(img,8, (138,224,136,227), (275,451,770,949))
    img2.show()
    img2.save("d:\\My Documents\\BaiduCloud\\SICOD\\GitHub\\Py\\test666\\888_.jpg")