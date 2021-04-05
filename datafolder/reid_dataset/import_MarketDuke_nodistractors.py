import os
from .reiddataset_downloader import *


def import_MarketDuke_nodistractors(data_dir, dataset_name): #arg dataset dir and dataset_name
    dataset_dir = os.path.join(data_dir,dataset_name) #path to the dataset.
    
    if not os.path.exists(dataset_dir):
        print('Please Download '+dataset_name+ ' Dataset') #if there is not dataset.
        
    dataset_dir = os.path.join(data_dir,dataset_name) #path to the dataset
    data_group = ['train','query','gallery']
    for group in data_group:
        if group == 'train':
            name_dir = os.path.join(dataset_dir , 'bounding_box_train') #path to dataset bounding box
        elif group == 'query':
            name_dir = os.path.join(dataset_dir, 'query') #path to dataset query
        else:
            name_dir = os.path.join(dataset_dir, 'bounding_box_test') #path to bounding box test
        file_list=sorted(os.listdir(name_dir)) #getting the images 
        globals()[group]={} #variable group now is a dictionary
        globals()[group]['data']=[] #key data is equat to a empty list
        globals()[group]['ids'] = [] #key ids is equal to a empty list
        for name in file_list: #loop throught all the files
            if name[-3:]=='jpg': #take 'jpg' files
                id = name.split('_')[0] #take de id, it can be 000, 001 or 002, etc.
                cam = int(name.split('_')[1][1]) #take the camera number i.e. C1 takes 1.
                images = os.path.join(name_dir,name) #takes a specific image
                if (id!='0000' and id !='-1'):
                    if id not in globals()[group]['ids']:
                        globals()[group]['ids'].append(id) #add the ids
                    globals()[group]['data'].append([images,globals()[group]['ids'].index(id),id,cam,name.split('.')[0]]) #save the data
    return train, query, gallery