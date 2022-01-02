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

def choose(i):
    switcher={
        1:'Lotto649.json',
        2:'LottoMax.json',
        3:'Grande_Vie.json',
        4:'ToutouRien.json'
    }
    return switcher.get(i,'Invalid Number')

jsonfile = choose(lotto)

with open("/home/richard/Documents/sambashare/"+jsonfile,"rb") as f:
   data = json.load(f)

global count
count = len(data)

PickNumbers=True

hits=0

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

def PrintStatus():
    print("|\r",end="")
    print("/\r",end="")
    print("|\r",end="")
    print("\\\r",end="")
    print("|\r",end="")
    print("/\r",end="")



#Lotto 6/49 Drawings
if lotto == 1:
    while PickNumbers or hits>0:

        numbers=[]

        hits=0

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

        with open("LottoDrawings.txt",'w+') as File:

          for pan in data:

            PrintStatus()

            hit=0
            
            for num in range(0,6):
              if numbers[num] == int(pan["P1"]) or numbers[num] == int(pan["P2"]) or numbers[num] == int(pan["P3"]) or numbers[num] == int(pan["P4"]) or numbers[num] == int(pan["P5"]) or numbers[num] == int(pan["P6"]):
                 hit+=1
              if hit == 4 or hit == 6:
               PickNumbers=True
               File.write(pan["Drawdate"]+", ")
               hits+=1
              else:
               PickNumbers=False
          
    print("The winning 6/49 numbers are "+str(numbers))

#LottoMax Drawings
if lotto == 2:
    while PickNumbers or hits>0:

        numbers=[]

        hits=0

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

        with open("LottoDrawings.txt",'w+') as File:

          for pan in data:
           
           PrintStatus()

           hit=0
           for num in range(0,7):
            if numbers[num] == int(pan["P1"]) or numbers[num] == int(pan["P2"]) or numbers[num] == int(pan["P3"]) or numbers[num] == int(pan["P4"]) or numbers[num] == int(pan["P5"]) or numbers[num] == int(pan["P6"] or numbers[num] == int(pan["P7"])):
               hit+=1
            if hit == 4 or hit == 7:
               PickNumbers=True
               File.write(pan["Drawdate"]+", ")
               hits+=1
            else:
               PickNumbers=False

    print("The LottoMax winning numbers are "+str(numbers))

#Grande Vie Drawings
if lotto == 3:

  with open("LottoDrawings.txt",'w+') as File:

    while PickNumbers or hits>0:

        numbers=[]

        hits=0

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

        with open("LottoDrawings.txt",'w+') as File:

          for pan in data:

            PrintStatus()

            hit=0
            if numbers[0] == int(pan["p1"]) and numbers[1] == int(pan["p2"]) and numbers[2] == int(pan["p3"]) and numbers[3] == int(pan["p4"]) and numbers[4] == int(pan["p5"]):
              PickNumbers=True
              File.write(pan["Drawdate"]+", ")
              hits=+1
            else:
              PickNumbers=False

            if numbers[0] == int(pan["p1"]) and numbers[1] == int(pan["p2"]) and numbers[2] == int(pan["p3"]) and numbers[3] == int(pan["p4"]) and numbers[4] == int(pan["p5"]) and numbers[5] == int(pan["gn"]):
              PickNumbers=True
              File.write(pan["Drawdate"]+", ")
              hits=+1
            else:
              PickNumbers=False 

            for num in range(0,5):
              if numbers[num] == int(pan["p1"]) or numbers[num] == int(pan["p2"]) or numbers[num] == int(pan["p3"]) or numbers[num] == int(pan["p4"]):       
                hit+=1
              if hit == 2:
                PickNumbers=True
                File.write(pan["Drawdate"]+", ")
                hits+=1
              else:
                PickNumbers=False

    print("The winning Grande Vie numbers are "+str(numbers))

#Tout ou Rien Drawings
if lotto == 4:
    while PickNumbers or hits>0:

        numbers=[]

        hits=0

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

        with open("LottoDrawings.txt",'w+') as File:

          for pan in data:

             PrintStatus()

             hit=0
             for num in range(0,12):
                 if numbers[num] == int(pan["p1"]) or numbers[num] == int(pan["p2"]) or numbers[num] == int(pan["p3"]) or numbers[num] == int(pan["p4"]) or numbers[num] == int(pan["p5"]) or numbers[num] == int(pan["p6"]) or numbers[num] == int(pan["p7"]) or numbers[num] == int(pan["p8"]) or numbers[num] == int(pan["p9"]) or numbers[num] == int(pan["p10"]) or numbers[num] == int(pan["p11"]) or numbers[num] == int(pan["p12"]):          
                  hit+=1
                 if hit == 8 or hit == 12:
                  PickNumbers=True
                  File.write(pan["Drawdate"]+", ")
                  hits+=1
                 else:
                  PickNumbers=False

    print("The winning Tout ou Rien numbers are "+str(numbers))