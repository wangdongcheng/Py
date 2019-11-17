#!/usr/bin/python3

# 打开一个文件
f = open('coordinate.txt', 'r')

for line in f:
    coord = line.split()
    for x in coord:
        print(x)
    print(line, end='')

for i in range(0, 10):
    print(i)

# 关闭打开的文件
f.close()
