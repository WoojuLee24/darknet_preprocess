import os
import glob
from shutil import copyfile

path="/ws/data/Okutama_old_test/"
new_path="/ws/data/Okutama_test/"

folderlist=sorted(os.listdir(path))
for folder in folderlist:
    folderpath= os.path.join(path, folder)
    files = sorted(os.listdir(folderpath))
    foldername=os.path.basename(folder)
    print(foldername)
    for file in files:
        filename = os.path.basename(file)
        filepath = os.path.join(folderpath, filename)
        new_filename = folder+"."+filename
        new_filepath = os.path.join(new_path, new_filename)
        copyfile(filepath, new_filepath)