import os
import sys
for a in range(4,23):
    path = 'd:/BaiduYunDownload/[艾奥里亚中文网]圣斗士星矢原版漫画全集/txt' + str(a).zfill(2) + '/'
    filenames = os.listdir(path)
    for filename in filenames:
        new_name = filename.replace('Image','').replace('.jpg','')
        new_name = new_name.zfill(3) + '.jpg'
        print(filename)
        print(new_name)
        os.rename(path+filename,path+new_name)