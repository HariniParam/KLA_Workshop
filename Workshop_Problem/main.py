# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 08:02:49 2023

@author: Harini P
"""

from PIL import Image
import os
import json
import csv

defect=[]
#Reading data from json file
def read_json(file_path):
    with open(file_path , 'r') as json_file:
        data = json.load(json_file)
    return data

#Storing data into variables
def image_details(data):
    global total_width, total_height, row, columns, street_width, care_areas,top_left,top_left_x,top_left_y,bottom_right,bottom_right_x,bottom_right_y 
    total_width = data["die"]["width"]
    total_height = data["die"]["height"]
    row = data["die"]["rows"]
    columns = data["die"]["columns"]
    street_width = data["street_width"]
    care_areas = data["care_areas"][0]
    top_left = care_areas["top_left"]
    top_left_x = top_left["x"]
    top_left_y = top_left["y"]
    bottom_right = care_areas["bottom_right"]
    bottom_right_x = bottom_right["x"]
    bottom_right_y = bottom_right["y"]

#Adding image path into list
def image_array(image_list, row, columns):
    for i in range(row):
        for j in range(columns):
            image_path = os.getcwd() + "\Level_1_Input_Data\wafer_image_" + str((j+1)) + ".png"
            image_list.append(image_path)
    print(image_list)
       
#Detecting defect    
def image_defects(image_list):
    """with open("output.csv","w") as output_file:
        csv_write = csv.writer(output_file)
        
        for i in range(len(image_list)):
            image = Image.open(image_list[i])
            rgb_image1 = image.convert('RGB')
            wid1, hgt1 = rgb_image1.size
            for y in range(hgt1):
                for x in range(wid1):
                    r, g, b = rgb_image1.getpixel((x, y))
                    color1 = (r,g,b)
                    image = Image.open(image_list[i+1])
                    rgb_image = image.convert('RGB')
                    r1, g1, b1 = rgb_image.getpixel((x, y))
                    color = (r1,g1,b1)
                    if color1 != color:    
                        #print(defect)
                        defect.append((i+1,x,total_height-1-y))
                        #csv_write.writerow((i+1,x,total_height-1-y))
        print(defect)             
        csv_write.writerows(defect)"""
        
    
        
    with open("output.csv","w") as output_file:
        csv_write = csv.writer(output_file)
        image = Image.open(image_list[0])
        rgb_image1 = image.convert('RGB')
        wid1, hgt1 = rgb_image1.size
        image2 = Image.open(image_list[1])
        rgb_image2 = image2.convert('RGB')
        defect = []
        for y in range(hgt1):
            for x in range(wid1):
                r, g, b = rgb_image1.getpixel((x, y))
                color1 = (r,g,b)
                r1, g1, b1 = rgb_image2.getpixel((x, y))
                color2 = (r1,g1,b1)
                if color1 != color2:
                    #print(color1, color2)
                    #if (1,x,y) not in defect:
                    defect.append((1,x,total_height-1-y))
        print(defect)
        csv_write.writerows(defect)
        
        image = Image.open(image_list[1])
        rgb_image1 = image.convert('RGB')
        wid1, hgt1 = rgb_image1.size
        image2 = Image.open(image_list[2])
        rgb_image2 = image2.convert('RGB')
        defect = []
        for y in range(hgt1):
            for x in range(wid1):
                r, g, b = rgb_image1.getpixel((x, y))
                color1 = (r,g,b)
                r1, g1, b1 = rgb_image2.getpixel((x, y))
                color2 = (r1,g1,b1)
                if color1 != color2:
                    #print(color1, color2)
                        #if (1,x,y) not in defect:
                    defect.append((2,x,total_height-1-y))
        print(defect)
        csv_write.writerows(defect)
        
        image = Image.open(image_list[2])
        rgb_image1 = image.convert('RGB')
        wid1, hgt1 = rgb_image1.size
        image2 = Image.open(image_list[3])
        rgb_image2 = image2.convert('RGB')
        defect = []
        for y in range(hgt1):
            for x in range(wid1):
                r, g, b = rgb_image1.getpixel((x, y))
                color1 = (r,g,b)
                r1, g1, b1 = rgb_image2.getpixel((x, y))
                color2 = (r1,g1,b1)
                if color1 != color2:
                    #print(color1, color2)
                        #if (1,x,y) not in defect:
                    defect.append((3,x,total_height-1-y))
        print(defect)
        csv_write.writerows(defect)
        
        image = Image.open(image_list[3])
        rgb_image1 = image.convert('RGB')
        wid1, hgt1 = rgb_image1.size
        image2 = Image.open(image_list[4])
        rgb_image2 = image2.convert('RGB')
        defect = []
        for y in range(hgt1):
            for x in range(wid1):
                r, g, b = rgb_image1.getpixel((x, y))
                color1 = (r,g,b)
                r1, g1, b1 = rgb_image2.getpixel((x, y))
                color2 = (r1,g1,b1)
                if color1 != color2:
                    #print(color1, color2)
                        #if (1,x,y) not in defect:
                    defect.append((4,x,total_height-1-y))
        print(defect)
        csv_write.writerows(defect)
        
        image = Image.open(image_list[4])
        rgb_image1 = image.convert('RGB')
        wid1, hgt1 = rgb_image1.size
        image2 = Image.open(image_list[0])
        rgb_image2 = image2.convert('RGB')
        defect = []
        for y in range(hgt1):
            for x in range(wid1):
                r, g, b = rgb_image1.getpixel((x, y))
                color1 = (r,g,b)
                r1, g1, b1 = rgb_image2.getpixel((x, y))
                color2 = (r1,g1,b1)
                if color1 != color2:
                    #print(color1, color2)
                        #if (1,x,y) not in defect:
                    defect.append((5,x,total_height-1-y))
        print(defect)
        csv_write.writerows(defect)
        

path = os.getcwd()
json_path = path+"\Level_1_Input_Data\input.json"
data = read_json(json_path)
print(data)

image_details(data)

image_list = []
image_array(image_list, row, columns)

image_defects(image_list)
        








