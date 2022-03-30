import re # filtrite jaoks
def save(user_name, user_class):
    f = open(f"{user_name}.txt","w+", encoding="UTF-8")
    f.write(f"{user_name}\n")
    f.write(f"{user_class}")
    f.close()
def load(user_name):    
    with open(f"{user_name}.txt","r", encoding="UTF-8") as fp: #avab faili
        line_numbers = [0] # line number
        a1 = [] # tühjendab
        for i, line in enumerate(fp): # midagi
            if i in line_numbers: # võtab teatud numbri järgi rea ette
                a1.append(line.strip()) # stripib välja teatud lineid ainult
                a2 = a1[0];
                print(a2)
    return a2

load("Sten")


