#Lotto Drawing program using a class
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

with open(jsonfile,"rb") as f:
   data = json.load(f)

global count
count = len(data)

global drawnumbers
drawnumbers=[]

class LottoDrawings():

    def __init__(self,rangenum,drawingnum,same,drawnumbers):
        self.rangenum = rangenum
        self.drawingnum = drawingnum
        self.same = same
        self.drawnumbers=drawnumbers

        def PrintStatus():
            print("|\r",end="")
            print("/\r",end="")
            print("|\r",end="")
            print("\\\r",end="")
            print("|\r",end="")
            print("/\r",end="")

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

        PickNumbers=True

        hits=0
       
        while PickNumbers or hits>0:

            numbers=[]

            hits=0

            for count in range(1,rangenum):
                rnd = random.randint(1,drawingnum)
                samenumber=0
                numbers2 = PickLottoNumbers(samenumber,drawingnum)
                numbers2[0].append(rnd)
                numbers2[0].sort()
                samenumber=0
            while samenumber !=same:
                numbers2 = PickLottoNumbers(samenumber,drawingnum)
                samenumber=numbers2[1]
            numbers=numbers2[0]
            
            if same==-4:
               rnd = random.randint(1,6)
               numbers.append(rnd)
        
            self.drawnumbers=numbers

            with open("LottoDrawings.txt",'w+') as File:

                for pan in data:

                    PrintStatus()
                    
                    hit=0

                    #Lotto 6/49 Drawings
                    if lotto == 1:
                        
                        for num in range(0,6):
                            if numbers[num] == int(pan["P1"]) or numbers[num] == int(pan["P2"]) \
                            or numbers[num] == int(pan["P3"]) or numbers[num] == int(pan["P4"]) \
                            or numbers[num] == int(pan["P5"]) or numbers[num] == int(pan["P6"]) \
                            or numbers[num] == int(pan["P7"]):
                             hit+=1
                        if hit == 4 or hit == 6:
                            PickNumbers=True
                            File.write(pan["Drawdate"]+", ")
                            hits+=1
                        else:
                            PickNumbers=False

                    #LottoMax Drawings        
                    if lotto == 2:

                        for num in range(0,7):
                            if numbers[num] == int(pan["P1"]) or numbers[num] == int(pan["P2"]) \
                            or numbers[num] == int(pan["P3"]) or numbers[num] == int(pan["P4"]) \
                            or numbers[num] == int(pan["P5"]) or numbers[num] == int(pan["P6"] \
                            or numbers[num] == int(pan["P7"])):
                              hit+=1
                            if hit == 4 or hit == 7:
                               PickNumbers=True
                               File.write(pan["Drawdate"]+", ")
                               hits+=1
                            else:
                               PickNumbers=False 

                    #Grande Vie Drawings
                    elif lotto == 3:

                        if numbers[0] == int(pan["p1"]) and numbers[1] == int(pan["p2"]) \
                        and numbers[2] == int(pan["p3"]) and numbers[3] == int(pan["p4"])\
                        and numbers[4] == int(pan["p5"]):
                            PickNumbers=True
                            File.write(pan["Drawdate"]+", ")
                            hits=+1
                        else:
                            PickNumbers=False

                        if numbers[0] == int(pan["p1"]) and numbers[1] == int(pan["p2"]) \
                        and numbers[2] == int(pan["p3"]) and numbers[3] == int(pan["p4"]) \
                        and numbers[4] == int(pan["p5"]) and numbers[5] == int(pan["gn"]):
                            PickNumbers=True
                            File.write(pan["Drawdate"]+", ")
                            hits=+1
                        else:
                            PickNumbers=False 

                        for num in range(0,5):
                            if numbers[num] == int(pan["p1"]) or numbers[num] == int(pan["p2"]) \
                            or numbers[num] == int(pan["p3"]) or numbers[num] == int(pan["p4"]):       
                                hit+=1
                            if hit == 2:
                                PickNumbers=True
                                File.write(pan["Drawdate"]+", ")
                                hits+=1
                            else:
                                PickNumbers=False
            
                    #Tout ou Rien Drawings
                    if lotto == 4:
                        for num in range(0,12):
                            if numbers[num] == int(pan["p1"]) or numbers[num] == int(pan["p2"]) \
                            or numbers[num] == int(pan["p3"]) or numbers[num] == int(pan["p4"]) \
                            or numbers[num] == int(pan["p5"]) or numbers[num] == int(pan["p6"]) \
                            or numbers[num] == int(pan["p7"]) or numbers[num] == int(pan["p8"]) \
                            or numbers[num] == int(pan["p9"]) or numbers[num] == int(pan["p10"]) \
                            or numbers[num] == int(pan["p11"]) or numbers[num] == int(pan["p12"]):          
                                hit+=1
                            if hit == 12:
                                PickNumbers=True
                                File.write(pan["Drawdate"]+", ")
                                hits+=1
                            else:
                                PickNumbers=False
 
#Lotto 6/49 Drawings
if lotto == 1:
    lottonumbers=LottoDrawings(7,49,-5,drawnumbers)    
    print("The winning 6/49 numbers are "+str(lottonumbers.drawnumbers))

#LottoMax Drawings
if lotto == 2:
    lottonumbers=LottoDrawings(8,50,-6,drawnumbers)    
    print("The LottoMax winning numbers are "+str(lottonumbers.drawnumbers))

#Grande Vie Drawings
if lotto == 3:
    lottonumbers=LottoDrawings(6,49,-4,drawnumbers)    
    print("The winning Grande Vie numbers are "+str(lottonumbers.drawnumbers))

#Tout ou Rien Drawings
if lotto == 4:
    lottonumbers=LottoDrawings(13,24,-11,drawnumbers)    
    print("The winning Tout ou Rien numbers are "+str(lottonumbers.drawnumbers))