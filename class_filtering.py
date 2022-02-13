#!/usr/bin/env python3
#
# If you want to train specific object not all, 
# from Pascal VOC 2012.
# You can use this scripts to 
# delete indifferent images and labeling data.
#
# You can easily download Pascal VOC 2012'
# origin images, labeling data from here
# https://universe.roboflow.com/jacob-solawetz/pascal-voc-2012
#
# Author: Seokjun Moon
# Date  : 2022.Feb.12.
# Mail  : msjun23@gmail.com


import os


ABS_CLASSES = {'aeroplane': 0, 
'bicycle': 1, 
'bird': 2, 
'boat': 3, 
'bottle': 4, 
'bus': 5, 
'car': 6, 
'cat': 7, 
'chair': 8, 
'cow': 9, 
'diningtable': 10, 
'dog': 11, 
'horse': 12, 
'motorbike': 13, 
'person': 14, 
'pottedplant': 15, 
'sheep': 16, 
'sofa': 17, 
'train': 18, 
'tvmonitor': 19}

ABS_CLASSES_REV = {0: 'aeroplane', 
1: 'bicycle', 
2: 'bird', 
3: 'boat', 
4: 'bottle', 
5: 'bus', 
6: 'car', 
7: 'cat', 
8: 'chair', 
9: 'cow', 
10: 'diningtable', 
11: 'dog', 
12: 'horse', 
13: 'motorbike', 
14: 'person', 
15: 'pottedplant', 
16: 'sheep', 
17: 'sofa', 
18: 'train', 
19: 'tvmonitor'}

my_classes = {}

curr_dir = os.getcwd()
#print(curr_dir)

train_dir = curr_dir + "/train"
valid_dir = curr_dir + "/valid"
#print(train_dir + '\n' + valid_dir)

train_labels_dir = train_dir + "/labels"
train_images_dir = train_dir + "/images"

valid_labels_dir = valid_dir + "/labels"
valid_images_dir = valid_dir + "/images"


def GetClass():
    while True:
        flag = True;
        
        # Get user's interest
        print("[aeroplane, bicycle, bird, boat, bottle, bus, car, cat, chair, cow, diningtable, dog, horse, motorbike, person, pottedplant, sheep, sofa, train, tvmonitor]")
        print("Classes you want to detect: ")
        input_str = input()
        classes = input_str.split()
        #print(classes)
        
        for obj in classes:
            if obj in ABS_CLASSES:
                pass
            else:
                # If typed wrong class, retyping is needed
                print("\n##########")
                print("Check your class is in Pascal VOC 2012")
                print("[aeroplane, bicycle, bird, boat, bottle, bus, car, cat, chair, cow, diningtable, dog, horse, motorbike, person, pottedplant, sheep, sofa, train, tvmonitor]")
                print("##########\n")
                flag = False
                break
            
        if flag:
            # All classes typed in is in Pascal VOC 2012
            # Save interests as my_classes
            class_num = 0
            for obj in classes:
                my_classes[obj] = class_num
                class_num += 1
            print(my_classes)
            break

def ClassFiltering(target_dir=train_labels_dir):
    file_num = 0
    for file in os.listdir(target_dir):
        # print(file)
        
        del_flag = True
        with open(target_dir + '/' + file, 'r') as f:
            # Open file as read mode & save lines at buffer
            lines = f.readlines()
        with open(target_dir + '/' + file, 'w') as f:
            # Open file again as write mode
            for line in lines:
                obj_info = line.split()
                curr_obj = ABS_CLASSES_REV[int(obj_info[0])]
                if (curr_obj in my_classes):
                    # If current line is interest, keep the line
                    del_flag = False
                    
                    # Change class number
                    obj_info[0] = str(my_classes[curr_obj])
                    new_line = ""
                    for info in obj_info:
                        new_line += (info + ' ')
                    new_line = new_line[:-1] + '\n'
                    print(new_line)
                    f.write(new_line)
                else:
                    # If current line is about object that we don't want to know, delete current line
                    pass
                
        if del_flag:
            # No interest in current file, delete it
            print("Delete", target_dir + '/' + file)
            os.remove(target_dir + '/' + file)
            
            # Also delete not interested images
            if (target_dir == train_labels_dir):
                print("Delete", train_images_dir + '/' + file[:-3] + 'jpg')
                os.remove(train_images_dir + '/' + file[:-3] + 'jpg')
            elif (target_dir == valid_labels_dir):
                print("Delete", valid_images_dir + '/' + file[:-3] + 'jpg')
                os.remove(valid_images_dir + '/' + file[:-3] + 'jpg')
        else:
            file_num += 1

    print(file_num)

if __name__=="__main__":
    GetClass()
    ClassFiltering(train_labels_dir)
    ClassFiltering(valid_labels_dir)
