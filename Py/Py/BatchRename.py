import os
import sys
import glob
import re

FROM_PATH   = '//diskstation/homes/admin/Drive/Moments/Mobile/Spring’s 6S+/'
TO_PATH     = 't:/2017_影像日记/'
FROM        = 'From :'
TO          = '\nTo   :'
FIVE_SPACE = '     '
COPY_MARK = '---->'

def compare_dir(from_dirs_path, to_dirs_path):
    from_dirs = glob.glob(from_dirs_path+'2017*')
    to_dirs = os.listdir(to_dirs_path)

    for from_dir in from_dirs:
        key_date = from_dir[-6:]  # the 6th last character to the last

        for to_dir in to_dirs:
            if to_dir.find(key_date) != -1:
               print(FROM, from_dir, TO ,to_dirs_path+to_dir)
               compare_pics(from_dir, to_dirs_path+to_dir)
               break
                                                   
def compare_pics(from_path, to_path):
    # print(FROM, from_path, TO, to_path)

    from_pics = os.listdir(from_path)
    to_pics = os.listdir(to_path)

    

    for fr_pic in from_pics:
        found = 0
        key = re.search( '\d\d\d\d', fr_pic) # regrex, 4 numbers
        if key:
            for to_pic in to_pics:
                if to_pic.find(key.group()) != -1:
                    from_size = os.path.getsize(from_path+'/'+fr_pic) / 1024
                    to_size = os.path.getsize(to_path+'/'+ to_pic) / 1024
                    if from_size == to_size:
                        found = 1
                        OUTPUT = '%s%s already copied to %s, with size %dk equals %dk'
                        print (OUTPUT %(FIVE_SPACE, fr_pic, to_pic, from_size, to_size))
                        break

            if found == 0:
                print(COPY_MARK, fr_pic,'need to be copied')

if __name__ == '__main__':
    compare_dir(FROM_PATH, TO_PATH)