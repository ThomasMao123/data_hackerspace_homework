#
# CS 196 Data Hackerspace
# Assignment 1: Data Parsing and NumPy
# Due September 24th, 2018
#

import json
import csv
import numpy as np
import math

def histogram_times(filename):
    arr=[]
    for i in range(0,24):
        arr.append(0)
    with open(filename,'r',encoding='utf-8') as f:
        csv_reader=csv.reader(f)
        airplane_data=list(csv_reader)
    for i in range(1,len(airplane_data)-1):
        if len(airplane_data[i][1])==0:
            continue
        numCounter=0
        index=0
        numarr=''
        while numCounter<2:
            if airplane_data[i][1][index].isdigit():
                numarr=numarr+airplane_data[i][1][index]
                index=index+1
                numCounter=numCounter+1
                continue
            index=index+1
        if int(numarr) > 23:
            continue
        else:
            arr[int(numarr)]=arr[int(numarr)]+1
    return arr
    
def weigh_pokemons(filename, weight):
    with open(filename,'r',encoding='utf-8')as f:
        data_dic=json.load(f)
    retlist=[]
    for i in range(0,len(data_dic['pokemon'])):
        numarr=''
        for j in data_dic['pokemon'][i]['weight']:
            if j=='.':
                numarr=numarr+j
            if j.isdigit():
                numarr=numarr+j
        if float(numarr)==weight:
            retlist.append(data_dic['pokemon'][i]['name'])
    return retlist

def single_type_candy_count(filename):
    with open(filename,'r',encoding='utf-8')as f:
        data_dic=json.load(f)
    count=0
    for i in range(0,len(data_dic['pokemon'])):
        if len(data_dic['pokemon'][i]['type'])==1:
            if 'candy_count' in data_dic['pokemon'][i].keys():
                count=count+data_dic['pokemon'][i]['candy_count']
    return count
        
def reflections_and_projections(points):
    for i in range(0,len(points[0])-1):
        points[1][i]=2-points[1][i]
    rotateMatrix=[[0,-1],
                  [1,0]]
    new_points=np.dot(rotateMatrix,points)
    projMatrix=[[1,3],
                [3,9]]
    final_points=np.dot(projMatrix,new_points)
    final_points=final_points/10.0
    return final_points
    
def normalize(image):
    max_value=np.amax(image)
    min_value=np.amin(image)
    for i in range(0,len(image)):
        for j in range(0,len(image[i])):
            image[i][j]=255/(max_value-min_value)*(image[i][j]-min_value)
    return image

def sigmoid_normalize(image,var):
    retMat=np.zeros([len(image),len(image[0])],dtype=np.float32)
    for i in range(0,len(image)):
        for j in range(0,len(image[i])):
            retMat[i][j]=255/(1+math.exp(-1/var*(image[i][j]-128)))
    return retMat
