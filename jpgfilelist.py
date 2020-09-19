import os
import glob
import random

path = "/ws/data/Okutama2"
jpgFilenamesList = sorted(glob.glob(path+'/*.jpg'))

for j in jpgFilenamesList:cd 

    j = os.path.basename(j)
    j = os.path.join("data/Okutama2", j)
    k = random.random()
    if k > 0.2:
        with open("/ws/data/Okutama2_train.txt", 'a') as f:
            data = j + "\n"
            f.write(data)
    else:
        with open("/ws/data/Okutama2_test.txt", 'a') as f:
            data = j + "\n"
            f.write(data)


