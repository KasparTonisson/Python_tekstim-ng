import random

#MÄNGUS VAJALIKUD MUUTUJAD
PrillPeedu = [100,15,5,18,6,23] 
IsandSten = [100,9,6,20,9,30] 
KoristajaKaspar = [100,8,8,25,7,25]
tase= 1
elud= 100
aielud=100


#MÄNGU START MENÜÜ
print()
print("                                       Mängu tegid: Peedu Erik Pajo, Kaspar Tõnisson ja Sten Veski")
print()
print("                        ██████╗░  ██╗░░██╗░█████╗░██╗░░░░░███████╗██╗░░░██╗██╗██████╗░░█████╗░███████╗░██████╗░░█████╗░")
print("                        ╚════██╗  ██║░██╔╝██╔══██╗██║░░░░░██╔════╝██║░░░██║██║██╔══██╗██╔══██╗██╔════╝██╔════╝░██╔══██╗")
print("                        ░█████╔╝  █████═╝░███████║██║░░░░░█████╗░░╚██╗░██╔╝██║██████╔╝██║░░██║█████╗░░██║░░██╗░███████║")
print("                        ░╚═══██╗  ██╔═██╗░██╔══██║██║░░░░░██╔══╝░░░╚████╔╝░██║██╔═══╝░██║░░██║██╔══╝░░██║░░╚██╗██╔══██║")
print("                        ██████╔╝  ██║░╚██╗██║░░██║███████╗███████╗░░╚██╔╝░░██║██║░░░░░╚█████╔╝███████╗╚██████╔╝██║░░██║")
print("                        ╚═════╝░  ╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝╚══════╝░░░╚═╝░░░╚═╝╚═╝░░░░░░╚════╝░╚══════╝░╚═════╝░╚═╝░░╚═╝")
print()
algus = int(input("                                              1. ALUSTA MÄNGU 2. LOAD 3. EXIT 4.xD DLC "))
print()
if algus == 4:
    print("NOT AVAILABLE IN FREE VERSION")
    print("TO PLAY SECRET VERSION BUY THE xD DLC FOR 29,99€")
    int(input("ENTER YOUR SOCIAL SECURITY NUMBER HERE: "))
    input("ENTER YOUR CREDIT CARD NUMBERS (both sides) ")
    print()
    print("HAHAHAHHAHAHAH GOT YO CREDIT CARD NUMBERS")
    scam = int(input("1. Rahatagstus 2. Oota kuni DLC tuleb "))
    if scam == 1:
        print()
        print("███████╗██╗")
        print("██╔════╝██║")
        print("█████╗░░██║")
        print("██╔══╝░░██║")
        print("███████╗██║")
        print("╚══════╝╚═╝")
        exit()
    elif scam == 2:
        exit()
    
    
    
#SALVESTAMINE
elif algus == 1:
    print("3 iidset kangelast läksid rindele.\n\nNende ülesandeks oli leida ja tappa teispoolsuset tulnud pahalased.\nTeekonnal ületasid nad maad ja mered.\nTeekond oli väga pikk kuid ilma tulemusteta.\nKuid ühel hommikul avastasid nad pahalased omas elemendis, nad olid parasjagu kogu Eesti metsa põlema panemas.\nEnne kui nad seda teha jõudsid andsid need 3 Kalevipoega neile kõva lahingu.\nHiilisid nad neile lähedale ja peksid neid puupalkidega, kuid see ei töötanud, palgid põlesid neid puudutades ära.\nNeil tekkis uus idee proovida pahalased järve saada.\nSelleks kulus neil väga palju jõudu ja aega.\nTuli pahalasi lüüa korda mööda järve suunas, saades iga kord neid puudutades said nad põletada.\nKuid jõudsid nad lõpuks nii kaugele, et nad said pahalased järve, kus nad kustusid ja kaotasid oma võimed.")
    print()
    user_name = input("Mis on sinu karakteri nimi? ")
     
elif algus == 2:
     with open(f"SAVE.txt", "r")as f:
         for rida in f:
             a = rida.split(" ")
             user_name = a[0]
             tase = int(a[1])
             elud = int(a[2])
             aielud = int(a[3])
             
#LAHKUMINE                       
elif algus == 3:
    exit()
#KARAKTERI VALIMINE
while True:
    print("1. Prill Peedu: Health: ",PrillPeedu[0],"; Õrn löök:",PrillPeedu[1],"; Uppercut:",PrillPeedu[2],"-",PrillPeedu[3],"; Fly kick:",PrillPeedu[4],"-",PrillPeedu[5])
    print("2. Isand Sten: Health: ",IsandSten[0],"; Õrn löök:",IsandSten[1],"; Uppercut:",IsandSten[2],"-",IsandSten[3],"; Fly Kick:",IsandSten[4],"-",IsandSten[5])
    print("3. Koristaja Kaspar : Health: ",KoristajaKaspar[0],"; Õrn löök:",KoristajaKaspar[1],"; Uppercut:",KoristajaKaspar[2],"-",KoristajaKaspar[3],"; Fly kick:",KoristajaKaspar[4],"-",KoristajaKaspar[5])
    user = input("\nVali karakter: 1, 2, or 3: ")
    if user == "1":
        user = PrillPeedu
        print("Sa oled valinud Prill Peedu")
        break
    if user == "2":
        user = IsandSten
        print("Sa oled valinud Isand Steni")
        break
    if user == "3":
        user = KoristajaKaspar
        print("Sa oled valinud Koristaja Kaspari")
        break
    else:
        print("Valige 1 karakteritest.")
        continue



    
print("----------------------- MÄNG ALGAB -----------------------")
#VASTANE
while True:
    ai = [100,10,5,15,0,25]
    
#VASTASE ELUD    
    if ai == 1:
        print("\nSu vastasel on",aielud,"elu!")

#COMBAT
#SINU LÖÖMINE
    while True:
        print("Sul on:",elud,"elu")
        print("Su vastasel on",aielud,"elu")
        ply_move = input("\nKas sa soovid Õrn löök (1), Uppercut (2)või Fly kick(3)? ")
        if ply_move == "1":
            ply_dmg = user[1]
            aielud = aielud- ply_dmg
            print("Sa tegid",ply_dmg,"damaget!")
        elif ply_move == "2":
            ply_dmg = random.randint(user[2],user[3])
            aielud = aielud- ply_dmg
            print("Sa tegid",ply_dmg,"damaget!")
        elif ply_move == "3":
            ply_dmg = random.randint(user[4],user[5])
            aielud = aielud- ply_dmg
            print("Sa tegid",ply_dmg,"damaget!")
        else:
            print("Valige üks käikudest.")
            continue
#VASTASE LÖÖMINE        
        ai_move = random.randint(1,3)
        if ai_move == 1:
            ai_dmg = ai[1]
            elud = elud- ai_dmg
            print("Sulle tehti",ai_dmg,"damaget!")
            print()
        elif ai_move == 2:
            ai_dmg = random.randint(ai[2],ai[3])
            elud = elud- ai_dmg
            print("Sulle tehti",ai_dmg,"damaget!")
            print()
        elif ai_move == 3:
            ai_dmg = random.randint(ai[4],ai[5])
            elud = elud- ai_dmg
            print("Sulle tehti",ai_dmg,"damaget!")
            print()
   
#MÄNGU KAOTAMINE
        if elud<=0:
            print("Sa Kaotasid! :(")
            print()
            print(f"Te jõudsite {tase}. tasemeni!")
            print("GAME OVER")
            valik = int(input("1. Välju: "))
            
            if valik == 1:
                exit()
            break
            
#MÄNGU VÕITMINE
        elif aielud<=0:
            print()
            print("Sa võitsid vastase!:)")
            print(f"Tase {tase} on läbitud.")
            tase += 1
            
#KARAKTERI UUEDAMINE
            while True:
                upgrade = int(input("1. +3 DAMAGE 2. +10 HP "))
                
   
                if upgrade == 1:
                    
                    elud=user[0]
                    user[1] += 3
                    user[2] += 3
                    user[3] += 3
                    user[4] += 3
                    user[5] += 3
                    
                
                    
                    
                    aielud = ai[0]
                    aielud+=7
                    ai[2] += 1
                    ai[3] += 1
                    ai[4] += 1
                    ai[5] += 1
                    
                elif upgrade == 2:
                    user[0] += 10
                    elud=user[0]
                    
                    ai[0]+=10
                    aielud = ai[0]
                    
                    ai[2] += 1
                    ai[3] += 1
                    ai[4] += 1
                    ai[5] += 1
                    
#MÄNGU SALVESTAMINE
                valik1 = int(input("1. Mängi edasi 2. Mängi edasi ja salvesta 3.Salvesta ja lahku "))
                if valik1 == 1:
                    break
                elif valik1 == 2:
                    with open(f"SAVE.txt", "w+")as f:
                        f.write(f"{user_name} ")
                        f.write(f"{tase} ")
                        f.write(f"{elud} ")
                        f.write(f"{aielud} ")
                        f.write(f"{user[1]} ")
                        f.write(f"{user[2]} ")
                        f.write(f"{user[3]} ")
                        f.write(f"{user[4]} ")
                        f.write(f"{user[5]} ")
                        f.write(f"{ai[1]} ")
                        f.write(f"{ai[2]} ")
                        f.write(f"{ai[3]} ")
                        f.write(f"{ai[4]} ")
                        f.write(f"{ai[5]} ")
                        
                        break
                elif valik1 == 3:
                    with open(f"SAVE.txt", "w+")as f:
                        f.write(f"{user_name} ")
                        f.write(f"{tase} ")
                        f.write(f"{elud} ")
                        f.write(f"{aielud} ")
                        f.write(f"{user[1]} ")
                        f.write(f"{user[2]} ")
                        f.write(f"{user[3]} ")
                        f.write(f"{user[4]} ")
                        f.write(f"{user[5]} ")
                        f.write(f"{ai[1]} ")
                        f.write(f"{ai[2]} ")
                        f.write(f"{ai[3]} ")
                        f.write(f"{ai[4]} ")
                        f.write(f"{ai[5]} ")
                        
                        exit()
                        break
                    
                    continue
