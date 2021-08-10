import os
import random


def get_filename(path, filetype):  # 输入路径、文件类型例如'.csv'
    name = []
    for root, dirs, files in os.walk(path):
        for i in files:
            if os.path.splitext(i)[1] == filetype:
                name.append(i)
    return name


trainval_percent = 0.2
train_percent = 0.8
xmlfilepath = 'F:/keras-yolo3-master/VOCdevkit/VOC2007/Annotations'
txtsavepath = 'F:/keras-yolo3-master/VOCdevkit/VOC2007/AnnotationsImageSets/Main'
total_xml = get_filename("F:/keras-yolo3-master/VOCdevkit/VOC2007/Annotations",".xml")

num = len(total_xml)
list = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(list, tv)
train = random.sample(trainval, tr)

ftrainval = open('F:/keras-yolo3-master/VOCdevkit/VOC2007/ImageSets/Main/trainval.txt', 'w')
ftest = open('F:/keras-yolo3-master/VOCdevkit/VOC2007/ImageSets/Main/test.txt', 'w')
ftrain = open('F:/keras-yolo3-master/VOCdevkit/VOC2007/ImageSets/Main/train.txt', 'w')
fval = open('F:/keras-yolo3-master/VOCdevkit/VOC2007/ImageSets/Main/val.txt', 'w')

for i in list:
    name = total_xml[i][:-4] + '\n'
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftest.write(name)
        else:
            fval.write(name)
    else:
        ftrain.write(name)

ftrainval.close()
ftrain.close()
fval.close()
ftest.close()