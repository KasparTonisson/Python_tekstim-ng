import random


        


print("KOLM AUTISTI")
algus = int(input("1. ALUSTA MÄNGU 2. LOAD 3. EXIT 4.SECRET LEVEL"))
print()
if algus == 4:
    print("NOT AVAILABLE IN FREE VERSION")
    print("TO PLAY SECRET VERSION BUY THE xD DLC FOR 29,99€")
    int(input("ENTER YOUR SOCIAL SECURITY NUMBER HERE: "))
    input("ENTER YOUR CREDIT CARD NUMBERS (both sides)")
    
    exit()
    #KUNAGI TULEB SAVE
elif algus == 3:
    exit()

    




PrillPeedu = [100,10,5,18,8,25] 
IsandSten = [100,7,5,23,10,23] 
KoristajaKaspar = [100,7,2,25,8,30]
tase= 1
elud= 100
aielud=100

while True:
    print("1. Prill Peedu: Health: ",PrillPeedu[0],"; Õrn löök:",PrillPeedu[1],"; Uppercut:",PrillPeedu[2],"-",PrillPeedu[3],"; Fly kick:",PrillPeedu[4],"-",PrillPeedu[5])
    print("2. Isand Sten: Health: ",IsandSten[0],"; Õrn löök:",IsandSten[1],"; Uppercut:",IsandSten[2],"-",IsandSten[3],"; Fly Kick:",IsandSten[4],"-",IsandSten[5])
    print("3. Koristaja Kaspar : Health: ",KoristajaKaspar[0],"; Õrn löök:",KoristajaKaspar[1],"; Uppercut:",KoristajaKaspar[2],"-",KoristajaKaspar[3],"; Fly kick:",KoristajaKaspar[4],"-",KoristajaKaspar[5])
    user = input("\nSelect your class: 1, 2, or 3: ")
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

while True:
    ai = [100,10,5,15,0,25] 
    
    if ai == 1:
        print("\nSu vastasel on",ai[0],"elu!")
    if ai == 2:
        print("\nSu vastasel on",ai[0],"elu!")
    if ai == 3:
        print("\nSu vastasel on",ai[0],"elu!")
    
    
    while True:
        print("\nSul on:",user[0],"elu")
        print("Su vastasel on",ai[0],"elu")
        ply_move = input("\nKas sa soovid Õrn löök (1), Uppercut (2)või Fly kick(3)?")
        if ply_move == "1":
            ply_dmg = user[1]
            ai[0] = ai[0]- ply_dmg
            print("Sa tegid",ply_dmg,"valu!")
        elif ply_move == "2":
            ply_dmg = random.randint(user[2],user[3])
            ai[0] = ai[0]- ply_dmg
            print("Sa tegid",ply_dmg,"valu!")
        elif ply_move == "3":
            ply_dmg = random.randint(user[4],user[5])
            ai[0] = ai[0]- ply_dmg
            print("Sa tegid",ply_dmg,"valu!")
        else:
            print("Valige üks käikudest.")
            continue
        
        ai_move = random.randint(1,3)
        if ai_move == 1:
            ai_dmg = ai[1]
            user[0] = user[0]- ai_dmg
            print("Sulle tehti",ai_dmg,"valu!")
        elif ai_move == 2:
            ai_dmg = random.randint(ai[2],ai[3])
            user[0] = user[0]- ai_dmg
            print("Sulle tehti",ai_dmg,"valu!")
        elif ai_move == 3:
            ai_dmg = random.randint(ai[4],ai[5])
            user[0] = user[0]- ai_dmg
            print("Sulle tehti",ai_dmg,"valu!")
           
          
       
        
        if user[0]<=0:
            print("Sa Kaotasid! :(")
            print()
            print(f"Te jõudsite {tase}. tasemeni!")
            print("GAME OVER")
            valik = int(input("1. EXIT: "))
            
            if valik == 1:
                exit()
            break
        
        elif ai[0]<=0:
            print()
            print("Sa võitsid vastase!:)")
            print(f"Tase {tase} on läbitud.")
            tase += 1
            upgrade = int(input("1. +3 DAMAGE 2. +10 HP "))
            while True:
                upgrade = int(input("1. +3 DAMAGE 2. +10 HP "))
                if upgrade == 1:
                    
                    user[0]=elud
                    user[1] += 3
                    user[2] += 3
                    user[3] += 3
                
                    
                    aielud+=7
                    ai[0]=aielud
                    ai[1] += 1
                    ai[2] += 1
                    ai[3] += 1
                    break
                elif upgrade == 2:
                    elud += 10
                    user[0]=elud
                    aielud+=15
                    ai[0]=aielud
                    ai[1] += 1
                    ai[2] += 1
                    ai[3] += 1
                    break
                else:
                    
                    continue
