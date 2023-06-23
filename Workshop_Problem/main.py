# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 08:02:49 2023

@author: Harini P
"""

from PIL import Image
import os
import json
import csv

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

def image_array(image_list, row, columns):
    for i in range(row):
        for j in range(columns):
            image_path = os.getcwd() + "\Level_1_Input_Data\wafer_image_" + str((j+1)) + ".png"
            image_list.append(image_path)
    print(image_list)
           
def image_defects(image_list):
    """care_area_width = bottom_right_x - top_left_x
    care_area_height = top_left_y - bottom_right_y
    image = Image.new("RGB",(care_area_width, care_area_height))
    i = Image.open(image_path)
    i.show()
    for i in range(care_area_height):
        for j in range(care_area_width):"""
    

    with open("output.csv","w") as output_file:
        csv_write = csv.writer(output_file)
        defect = []
        for i in range(len(image_list)):
            for j in range(len(image_list)):
                image = Image.open(image_list[i])
                rgb_image1 = image.convert('RGB')
                wid1, hgt1 = rgb_image1.size
                for y in range(hgt1):
                    for x in range(wid1):
                        r, g, b = rgb_image1.getpixel((x, y))
                        color1 = (r,g,b)
                        if i!=j:
                            image = Image.open(image_list[j])
                            rgb_image = image.convert('RGB')
                            r1, g1, b1 = rgb_image.getpixel((x, y))
                            color = (r1,g1,b1)
                            if color1 != color:    
                                if (i+1,x,y) not in defect:
                                    defect.append((i+1,x,y))
                                    print(defect)
                                    csv_write.writerow((i+1,x,y))
        #print(defect)
            

path = os.getcwd()
json_path = path+"\Level_1_Input_Data\input.json"
data = read_json(json_path)
print(data)

image_details(data)

image_list = []
image_array(image_list, row, columns)

image_defects(image_list)

        








