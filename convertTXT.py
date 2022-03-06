import re
from config import *
f = open("set_cob.txt", "r")
x = re.split("\s", f.read())
for a in range(len(keyIVT_config)):
    for i in range(len(x)):
        if x[i]==keyIVT_config[a]:
            for y in range(15):
                print(x[y+i+1])
        
print(len(x))