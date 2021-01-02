import time
import itertools

s = time.time()
ans1 = []
ans2 = []
x = 0
r = 0
list = [100,200,330,470,1000,4700,5600,10000,47000,100000]

for honoka in range(2,len(list)+1):
    kotori = itertools.permutations(list,honoka)#teikou kumiawase 2Dhairetsu

    for umi in kotori:#2Dhairetsu ikozutu toridasu

        for i in range(2 ** len(umi)):  #bit zentansaku
            two = '1' + '{:b}'.format(i).zfill(len(umi) - 1) + '1'  #nisinsuu henkan
            z = 0  #shokika
            a = [] #
            b = [] #
            c = [] #

            for j in range(len(umi)):  #tansaku start

                if two[j] == '1' and two[j+1] == '1':  #chokuretsu
                    z += umi[j]
                    a.append(umi[j]) 
                    

                elif two[j] == '0' and two[j+1] == '1':  #heiretsu end
                    b.append(1 / umi[j])
                    c.append(umi[j])  
                    z += 1 / sum(b)
                    b = []

                else:  #heiretsu count start
                    b.append(1 / umi[j])
                    c.append(umi[j]) 

                    if z > 2022:
                        continue

            if abs(2021 - z) < abs(2021 - x):#2021 ni chikai atai hikaku
                x = z      #atai kiroku
                ans1 = a   #
                ans2 = c   #
                twoo = two #

print("数値 ",x)
print("直列に使ったやつ ",ans1)
print("並列に使ったやつ ",ans2)
print("繋げる順番",twoo)
print("かかった時間 ",(time.time() - s))