import re
import copy
import sys
hurap_file = open(sys.argv[1], "r")
schuckscii_file = open(sys.argv[2], "r")
virus_codes_file = open(sys.argv[3], "r")

huraplist=[]      #hurapfile nin liste hali
huraplist1=[]
deneme=[]

for i in hurap_file: #hurapfile listeye atmak
    i=i.rstrip("\n")
    huraplist.append(i)

x=0
while x < int(len(huraplist)):  # key haric listeleme
     for i in huraplist[x]:

         if i!="1":
             if i!="0":
                key=huraplist.pop(x)
     x=x+1


huraplist1=copy.copy(huraplist)      # huraplist1 kopyalama
for i in huraplist:                  #huraplistin str seklinde ayirma
    for q in i:
        deneme.append(q)
    deneme.append("♫")


list1=[]
list2=[]
hekza=[]   # 1 2 4 8 
for i in deneme:
    list1.append(i)
    if(i=='♫'):
        list1.reverse()
        list2.extend(list1)
        list1=[]


Hak=4
for i in list2:
    if Hak==0:
        Hak=4
    if i== "♫":
        hekza.append(i)
    elif Hak==1 and i!="♫":
        a=((2**3)*int(i))
        hekza.append(a)
        Hak=Hak-1

    elif Hak==2 and i!="♫":
        a=((2**2)*int(i))
        hekza.append(a)
        Hak=Hak-1
    elif Hak==3 and i!="♫":
        a=((2**1)*int(i))
        hekza.append(a)
        Hak=Hak-1
    elif Hak==4 and i!="♫":
        a= (1 * int(i))
        hekza.append(a)
        Hak=Hak-1

hektop=[]
sayac=0
toplam=0


for i in hekza:

    if i == "♫":
        hektop.append(i)
    elif sayac==0:
        toplam=toplam+i
        sayac=sayac+1
    elif sayac ==1:
        toplam=toplam+i
        sayac=sayac+1
    elif sayac ==2:
        toplam=toplam+i
        sayac=sayac+1
    elif sayac ==3:
        toplam=toplam+i
        sayac=sayac+1
    if sayac==4:
        hektop.append(toplam)
        sayac=0
        toplam=0


for i in hektop:
    b=int(hektop.index(i))

    if i== 10:
        hektop[b]="A"
    if i== 11:
        hektop[b]="B"
    if i==12:
        hektop[b]="C"
    if i ==13:
        hektop[b]="D"
    if i ==14:
        hektop[b]="E"
    if i==15:
        hektop[b]="F"


bos1=[]
tohex=[]
hektop.remove("♫")
for i in hektop:
    bos1.append(i)
    if(i=='♫'):
        bos1.reverse()
        tohex.extend(bos1)
        bos1=[]
tohex.append("♫")
bos1.reverse()
tohex.extend(bos1)


print("*********************")
print("      Mission00      ")
print("*********************")
schuckscii_file1=[]

for i in schuckscii_file:
    i=i.rstrip("\n")
    schuckscii_file1.append(i)

schuckscii_file2=[]
for i in schuckscii_file1:
    i=i.split( )
    schuckscii_file2.append(i)

dic={}
for i in schuckscii_file2:
    if len(i)==2:                    #space icin
        i.insert(0," ")
    dic[i[1]]=i[0]



encry=[]
sayac=0

for i in tohex:
    if i=="♫":
        encry.append(i)

    elif sayac==1:
        b=str(i)
        c=a+b
        encry.append(c)
        sayac=0
    elif sayac==0:
        a=str(i)
        sayac=sayac+1
encry1=[]
print()
print("--- hex of encrypted code ---")
print("-----------------------------")
hex_of_encrypted_code=copy.copy(encry)

for i in hex_of_encrypted_code: #1.sorunun cevabı bin to hex
    if i=="♫":
        print()
    else:
        sys.stdout.write(str(i))

for i in encry:
    for j in dic.keys():
        if i==j:
            a=encry.index(i)
            b=dic[j]
            encry[a]=b

encrypted_code=copy.copy(encry) #2.sorunun cevap listesi
print()
print()
print("--- encrypted code ----")
print("-----------------------")
for i in encrypted_code: #1.sorunun cevabı bin to hex
    if i=="♫":
        print()
    else:
        sys.stdout.write(str(i)) #hex of encrypted code
keylist=[]

for i in key:
        if i=="1":
            keylist.append(i)
        elif i=="0":
            keylist.append(i)


a=len(keylist)-1
sum=0
x=0
keylist.reverse()

for i in keylist:
    if x==a:
        b= -(2**x * int(i))
        sum=sum+b
    else:
        b= (2**x * int(i))
        sum=sum+b
        x=x+1

sum = sum + len(schuckscii_file2)
sum= sum%len(schuckscii_file2)

schuckscii_file3=copy.copy(schuckscii_file2)

sch=[]

for j in schuckscii_file3:
    sch.append(j[0])

encry12=[]
for i in encry:
    if i in sch:
            c=encry.index(i)
            a=sch.index(i)
            b= a - sum
            encry12.append(sch[b])
    elif i=="♫":
        encry12.append(i)

print()
print()
print("--- decrypted code ---")
print("----------------------")

for i in encry12:
    if i=="♫":
        print()
    else:
        x=sys.stdout.write(str(i))



print()
print()
virus=[]
virus1=[]  # en son splitli hali
dicvirus={}

for i in virus_codes_file:
    i=i.rstrip("\n")
    virus.append(i)
for i in virus:
    i=i.split(":")
    virus1.append(i)
for i in virus1:           #virus degerlerini dic e aktardik
    dicvirus[i[0]]=i[1]

encry13=[]


def kombine(ilk):
    son = []
    ifade = ''
    in_ifade = False

    for e in ilk:
        if e == '♫':
            if in_ifade:
                son.append(ifade)
                in_ifade = False
                ifade = ''
            son.append(e)
        else:
            in_ifade = True
            ifade += e
    if in_ifade:
        son.append(ifade)
    return son


encry12=kombine(encry12)

viruss=[]

for i in encry12:

        viruss.append(i)


viruson=[]
for i in virus:
    i=i.split(':')
    viruson.append(i)

for e in viruson:
    for i in range(len(viruss)):
        viruss[i] = viruss[i].replace(e[0], e[1])

print("*********************")
print("     Mission 01      ")
print("*********************")


for i in viruss:
    if i=="♫":
        print()
    else:
        x=sys.stdout.write(str(i))
donus=[]

for i in viruss:
    for j in i:
        donus.append(j)

hekof=[]

for i in donus:
    if i in sch:
            c=donus.index(i)
            a=sch.index(i)
            b= a + sum
            b= b%len(schuckscii_file2)

            hekof.append(sch[b])
    elif i=="♫":
        hekof.append(i)


donus1=[]

for i in hekof:
    if i=='♫':
        donus1.append(i)
    else:
        for j in schuckscii_file2:
             if i == j[0]:
                 i=j[1]
                 donus1.append(i)

print()
print()
print("*********************")
print("      Mission 10     ")
print("*********************")
print()
print("--- encrypted code ---")
print("----------------------")
for i in hekof:
    if i=="♫":
        print()
    else:
        x=sys.stdout.write(str(i))

print()
print()
print("--- hex of encrypted code ---")
print("-----------------------------")

for i in donus1:
    if i=="♫":
        print()
    else:
        x=sys.stdout.write(str(i))

donus2=[]


for i in donus1:
    for j in i:
        donus2.append(j)


for i in donus2:

    b=int(donus2.index(i))

    if i== "A":
        donus2[b]="10"
    if i== "B":
        donus2[b]="11"
    if i== "C":
        donus2[b]="12"
    if i =="D":
        donus2[b]="13"
    if i =="E":
        donus2[b]="14"
    if i=="F":
        donus2[b]="15"


binarylist={}
binarylist["0"]="0000"
binarylist["1"]="0001"
binarylist["2"]="0010"
binarylist["3"]="0011"
binarylist["4"]="0100"
binarylist["5"]="0101"
binarylist["6"]="0110"
binarylist["7"]="0111"
binarylist["8"]="1000"
binarylist["9"]="1001"
binarylist["10"]="1010"
binarylist["11"]="1011"
binarylist["12"]="1100"
binarylist["13"]="1101"
binarylist["14"]="1110"
binarylist["15"]="1111"
donus3=[]
binarylist1=[]

for i in donus2:
    a=donus2.index(i)
    if i in binarylist:
        donus2[a]=binarylist[i]
print()
print()
print("--- bin of encrypted code ---")
print("-----------------------------")

for i in donus2:
    for j in i:
        donus3.append(j)

for i in donus3:
    if i=="♫":
        print()
    else:
        x=sys.stdout.write(str(i))

