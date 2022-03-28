import random 

print("Mäng")
user_name = input("Pange oma karakteri nimi: ")

PrillPeedu = [100,10,5,15,0,25] 
IsandSten = [50,15,10,20,5,25] 
KoristajaKaspar = [150,5,5,10,5,15]  

while True:
    print("1. Prill Peedu: Health: ",PrillPeedu[0],"; rünnak 1:",PrillPeedu[1],"; rünnak 2:",PrillPeedu[2],"-",PrillPeedu[3],"; rünnak 3:",PrillPeedu[4],"-",PrillPeedu[5])
    print("2. Isand Sten: Health: ",IsandSten[0],"; rünnak 1:",IsandSten[1],"; rünnak 2:",IsandSten[2],"-",IsandSten[3],"; rünnak 3:",IsandSten[4],"-",IsandSten[5])
    print("3. Koristaja Kaspar : Health: ",KoristajaKaspar[0],"; rünnak 1:",KoristajaKaspar[1],"; rünnak 2:",KoristajaKaspar[2],"-",KoristajaKaspar[3],"; rünnak 3:",KoristajaKaspar[4],"-",KoristajaKaspar[5])
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
        ply_move = input("\nKas sa soovid rünnak (1), rünnak (2)või rünnak (3)?")
        if ply_move == "1":
            ply_dmg = user[1]
            ai[0] = ai[0]- ply_dmg
            print(user_name," tegi",ply_dmg,"valu!")
        elif ply_move == "2":
            ply_dmg = random.randint(user[2],user[3])
            ai[0] = ai[0]- ply_dmg
            print(user_name," tegi",ply_dmg,"valu!")
        elif ply_move == "3":
            ply_dmg = random.randint(user[4],user[5])
            ai[0] = ai[0]- ply_dmg
            print(user_name," tegi",ply_dmg,"valu!")
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
           
          
        print("\nSul on:",user[0],"elu")
        print("Su vastasel on",ai[0],"elu")
        
        if user[0]<=0:
            print("Sa võitsid vastase!:)")
            break
        
        elif ai[0]<=0:
            print("Sa Kaotasid! :(")
            break
    
        
