import os
import glob

path = "/ws/data/Okutama/Test-Set/Labels/SingleActionLabels/3840x2160/*.txt"
new_path= "/ws/new_data/"

filelist = sorted(glob.glob(path))
for file in filelist:
    try:
        f=open(file, 'r')
        lines=f.readlines()
        for line in lines:
            l = line.split()
            w = round((int(l[3])-int(l[1]))/3840,6)
            h = round((int(l[4])-int(l[2]))/2160,6)
            x = round((int(l[3])+int(l[1]))/2/3840,6)
            y = round((int(l[4])+int(l[2]))/2/2160,6)
            frame = l[5]
            new_file= new_path + os.path.splitext(os.path.basename(file))[0] + "." + str(frame) + ".txt"
            with open(new_file, 'a+') as nf:
                data = str(0)+" "+str(x) + " " + str(y) + " " + str(w) + " " + str(h)+"\n"
                nf.write(data)
    except FileNotFoundError as e:
        print(e)
    finally:
        f.close()

    