import json
import random
import os

os.system('clear')

print("""1 = Lotto 6/49
2 = LottoMax
3 = Grande Vie
4 = Tout Ou Rien""")
print()
lotto=int(input("What Lotto numbers do you wish to pick :"))

print()
num=int(input("1 - 4 Numbers :"))

def choose(i):
    switcher={
        1:'Lotto649.json',
        2:'LottoMax.json',
        3:'Grande_Vie.json',
        4:'ToutouRien.json'
    }
    return switcher.get(i,'Invalid Number')

jsonfile = choose(lotto)

with open(jsonfile,"rb") as f:
   data = json.load(f)

global count
count = len(data)

#Numbers = pd.DataFrame(data)

PickNumbers=True

def PickLottoNumbers(samenumber,total):
        samenumber=1 
        count2=0
        for number in numbers:
            if numbers[count2-1] == number and count2 !=0:
               rnd = random.randint(1,total)
               numbers[count2]=rnd
               rnd = random.randint(1,total)
               samenumber+=1
            else:
                samenumber-=1
            count2+=1
            numbers.sort()
        return numbers,samenumber

#Lotto 6/49 Drawings
if lotto == 1:
    while PickNumbers:

        numbers=[]

        for count in range(1,7):
            rnd = random.randint(1,49)
            samenumber=0
            numbers2 = PickLottoNumbers(samenumber,49)
            numbers2[0].append(rnd)
            numbers2[0].sort()
            samenumber=0
        while samenumber !=-5:
            numbers2 = PickLottoNumbers(samenumber,49)
            samenumber=numbers2[1]
        numbers=numbers2[0]

        for pan in data:
            if num==1:
                if numbers[0] == int(pan["P1"]):
                    PickNumbers=True
                else:
                    PickNumbers=False    
            elif num==2:
                if numbers[0] == int(pan["P1"]) and numbers[1] == int(pan["P2"]):
                    PickNumbers=True
                else:
                    PickNumbers=False      
            elif num==3:
                if numbers[0] == int(pan["P1"]) and numbers[1] == int(pan["P2"]) and numbers[2] == int(pan["P3"]):
                    PickNumbers=True
                else:
                    PickNumbers=False    
            elif num==4:
                if numbers[0] == int(pan["P1"]) and numbers[1] == int(pan["P2"]) and numbers[2] == int(pan["P3"]) and numbers[3] == int(pan["P4"]):
                    PickNumbers=True
                else:
                    PickNumbers=False            
        if numbers[0] == int(pan["P1"]) and numbers[1] == int(pan["P2"]) and numbers[2] == int(pan["P3"]) and numbers[3] == int(pan["P4"]) and numbers[4] == int(pan["P5"]) and numbers[5] == int(pan["P6"]):
            PickNumbers=True
        else:
            PickNumbers=False 
            #print(pan)

        print("The winning 6/49 numbers are "+str(numbers))

#LottoMax Drawings
if lotto == 2:
    while PickNumbers:

        numbers=[]

        for count in range(1,8):
            rnd = random.randint(1,50)
            samenumber=0
            numbers2 = PickLottoNumbers(samenumber,50)
            numbers2[0].append(rnd)
            numbers2[0].sort()
            samenumber=0
        while samenumber !=-6:
            numbers2 = PickLottoNumbers(samenumber,50)
            samenumber=numbers2[1]
        numbers=numbers2[0]

        for pan in data:
            if num==1:
                if numbers[0] == int(pan["P1"]):
                    PickNumbers=True
                else:
                    PickNumbers=False    
            elif num==2:
                if numbers[0] == int(pan["P1"]) and numbers[1] == int(pan["P2"]):
                    PickNumbers=True
                else:
                    PickNumbers=False      
            elif num==3:
                if numbers[0] == int(pan["P1"]) and numbers[1] == int(pan["P2"]) and numbers[2] == int(pan["P3"]):
                    PickNumbers=True
                else:
                    PickNumbers=False    
            elif num==4:
                if numbers[0] == int(pan["P1"]) and numbers[1] == int(pan["P2"]) and numbers[2] == int(pan["P3"]) and numbers[3] == int(pan["P4"]):
                    PickNumbers=True
                else:
                    PickNumbers=False            
        if numbers[0] == int(pan["P1"]) and numbers[1] == int(pan["P2"]) and numbers[2] == int(pan["P3"]) and numbers[3] == int(pan["P4"]) and numbers[4] == int(pan["P5"]) and numbers[5] == int(pan["P6"]) and numbers[6]==int(pan["P7"]):
            PickNumbers=True
        else:
            PickNumbers=False 
            #print(pan)

        print("The LottoMax winning numbers are "+str(numbers))

#Grande Vie Drawings
if lotto == 3:
    while PickNumbers:

        numbers=[]

        for count in range(1,6):
            rnd = random.randint(1,49)
            samenumber=0
            numbers2 = PickLottoNumbers(samenumber,49)
            numbers2[0].append(rnd)
            numbers2[0].sort()
            samenumber=0
        while samenumber !=-4:
            numbers2 = PickLottoNumbers(samenumber,49)
            samenumber=numbers2[1]
        numbers=numbers2[0]

        rnd = random.randint(1,6)
        numbers.append(rnd)

        for pan in data:
            if num==1:
                if numbers[0] == int(pan["p1"]):
                    PickNumbers=True
                else:
                    PickNumbers=False    
            elif num==2:
                if numbers[0] == int(pan["p1"]) and numbers[1] == int(pan["p2"]):
                    PickNumbers=True
                else:
                    PickNumbers=False      
            elif num==3:
                if numbers[0] == int(pan["p1"]) and numbers[1] == int(pan["p2"]) and numbers[2] == int(pan["p3"]):
                    PickNumbers=True
                else:
                    PickNumbers=False    
            elif num==4:
                if numbers[0] == int(pan["p1"]) and numbers[1] == int(pan["p2"]) and numbers[2] == int(pan["p3"]) and numbers[3] == int(pan["p4"]):
                    PickNumbers=True
                else:
                    PickNumbers=False
        if numbers[0] == int(pan["p1"]) and numbers[1] == int(pan["p2"]) and numbers[2] == int(pan["p3"]) and numbers[3] == int(pan["p4"]) and numbers[4] == int(pan["p5"]):
            PickNumbers=True
        else:
            PickNumbers=False         
        if numbers[0] == int(pan["p1"]) and numbers[1] == int(pan["p2"]) and numbers[2] == int(pan["p3"]) and numbers[3] == int(pan["p4"]) and numbers[4] == int(pan["p5"]) and numbers[5] == int(pan["gn"]):
            PickNumbers=True
        else:
            PickNumbers=False 
            #print(pan)

        print("The winning Grande Vie numbers are "+str(numbers))

#Tout ou Rien Drawings
if lotto == 4:
    while PickNumbers:

        numbers=[]

        for count in range(1,13):
            rnd = random.randint(1,24)
            samenumber=0
            numbers2 = PickLottoNumbers(samenumber,24)
            numbers2[0].append(rnd)
            numbers2[0].sort()
            samenumber=0
        while samenumber !=-11:
            numbers2 = PickLottoNumbers(samenumber,24)
            samenumber=numbers2[1]
        numbers=numbers2[0]

        
        for pan in data:
            if num==4:
                if numbers[0] == int(pan["p1"]) and numbers[1] == int(pan["p2"]) and numbers[2] == int(pan["p3"]) and numbers[3] == int(pan["p4"]) and numbers[4]:
                    PickNumbers=True
                else:
                    PickNumbers=False
                if numbers[0] == int(pan["p1"]) and numbers[1] == int(pan["p2"]) and numbers[2] == int(pan["p3"]) and numbers[3] == int(pan["p4"]) and numbers[4] == int(pan["p5"]) and numbers[5] == int(pan["p6"]) and numbers[6] == int(pan["p7"]) and numbers[7] == int(pan["p8"]):
                    PickNumbers=True
                else:
                    PickNumbers=False
        
        count =0
        hits=0

        for pan in data:
          for num in range(0,12):
            #print(numbers[num])
            #print (type(pan))
            if numbers[num] == int(pan["p1"]):          
             hits+=1
        #print(hits)

        if numbers[0] == int(pan["p1"]) and numbers[1] == int(pan["p2"]) and numbers[2] == int(pan["p3"]) and numbers[3] == int(pan["p4"]) and numbers[4] == int(pan["p5"]) and numbers[5] == int(pan["p6"]) and numbers[6] == int(pan["p7"]) and numbers[7] == int(pan["p8"]) and numbers[8] == int(pan["p9"]) and numbers[9] == int(pan["p10"]) and numbers[10] == int(pan["p11"]) and numbers[11] == int(pan["p12"]):
            PickNumbers=True
        else:
            PickNumbers=False         

    print("The winning Tout ou Rien numbers are "+str(numbers))