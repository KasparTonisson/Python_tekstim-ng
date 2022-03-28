if user[0]<=0:
            print("Sa Kaotasid! :(")
            print()
            print("GAME OVER")
            valik = int(input("1. START OVER 2. EXIT: "))
            if valik == 1:
                #Reload
            else:
                exit()
            break
        
        elif ai[0]<=0:
            print("Sa võitsid vastase!:)")
            valik1 = int(input("1. CONTINUE 2. SAVE AND EXIT 3. SAVE: "))
            
            if valik1 == 1:
                continue
            
                
            break