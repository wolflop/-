# -*- coding:utf-8 -*-

import os
def getword(linePath):
    keyword = ['step','descript']

    a = []
    
    with open(filePath, encoding='utf-8') as f:
        for line in f.readlines():
            for key in keyword:
                if key in line:
                    a.append(line)
                else:
                    continue
    return a



if __name__ =='__main__':
    filePath = 'test.txt'
    a = getword(filePath)
    print(a)
