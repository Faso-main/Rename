import os

path = "C:/----/" # путь до папки
count =  0
for file in os.listdir(path):
    if (os.path.basename(file)[0] == 'C' and os.path.basename(file)[1] == 'C'):
        name = os.path.basename(file)
        new_name = "S_"+str(count)+".mrk.json"
        os.rename(os.path.join(path, name), os.path.join(path, new_name))
        
        count += 1
