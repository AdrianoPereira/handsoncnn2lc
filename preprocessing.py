import os
import numpy as np
import subprocess as sp
import geopandas as gpd

OUTPUT = "./data/area_test/input"
PATH = "./data/test1/buffer"
SEP = os.sep

def get_files_tiff():
    all_files = list()

    for root, dirs, files in os.walk(PATH):
        for file in files:
            all_files.append(os.path.join(root, file))
    all_files = np.asarray(all_files)

    return np.asarray(list(filter(lambda x: x.endswith('.tif'), all_files)))


# def generate_true_color():
#     files = get_files_tiff()
#     output = "true_color"
#     output = os.path.join(OUTPUT, output)
    
#     if not os.path.exists(output):
#         os.makedirs(output)
        
#     for file in files: 
#         filename = file.split(SEP)
#         filename = "%s_%s"%(filename[3], filename[-1])
#         filename = os.path.join(output,  filename)
        
#         cmd = "gdal_translate -of GTiff -b 3 -b 2 -b 1 %s %s"%(file.replace(' ', '\ '), filename.replace(' ', '\ '))
#         print(cmd)
#         out = sp.Popen([cmd], shell=True, stdout=sp.PIPE) 
#         _ = out.communicate()[0]
        
#         os.remove("%s.aux.xml"%filename)

def generate_true_color():
    files = get_files_tiff()
    output = "true_color"
    output = os.path.join(OUTPUT, output)
    
    if not os.path.exists(output):
        os.makedirs(output)
        
    for file in files: 
        filename = file.split(SEP)
        filename = "%s_%s"%(filename[4], filename[-1])
        filename = os.path.join(output,  filename)
        print(filename)    
        cmd = "gdal_translate -of GTiff -b 3 -b 2 -b 1 %s %s"%(file.replace(' ', '\ '), filename.replace(' ', '\ '))
        print(cmd)
        out = sp.Popen([cmd], shell=True, stdout=sp.PIPE) 
        _ = out.communicate()[0]
        
        os.remove("%s.aux.xml"%filename)
    
if __name__ == "__main__":
    generate_true_color()
    
            