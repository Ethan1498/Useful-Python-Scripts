# Python script to remove all files in directory, I'm too lazy to clear EE cache by hand
import os 

dir = 'REPLACE WITH NEEDED DIR'
for f in os.listdir(dir):
    os.remove(os.path.join(dir, f))