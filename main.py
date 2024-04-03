import math

vinkelsum = 180

print("velkommen til trekantsberegneren")
print("hvilke af følgende sætning beskriver de kendte værdier i trekanten du vil beregne?")
print("1.  en vinkel den modstående side og en side mere")
print("2.  3 sider")
print("3.  1 side, den modstånde vinkel og en vinkel mere")
print("4.  1 side og de to hosliggende vinkler")
print("5.  en vinkel og de to hosliggende sider")

while True:
    valg = input("Indsæt sætningens nummer fra 1-5")
    def sinusrelationfunktionA(C, a, c):
        A=float(math.asin((math.sin(C) * a) / c))
        print(math.degrees(A))
    def vinkelsumfunktionB(A, C):
        B=float(vinkelsum-A-C)
        print(B)
    def sinusrelationfuktionb(B, C, c):
        b=float((c*math.sin(B))/math.sin(C))
        print(b)
    def cosinusrelationfunktionC(a, b, c):
        C=float(math.acos((a**2+b**2-c**2)/(2*a*b)))
        print(C)

    if "1" in valg:
        C=math.radians(float(input("værdi af vinklen=")))
        c=float(input("værdi af modstånde side="))
        a=float(input("værdi af hossligende side="))
        print("2. vinkel =")
        A=sinusrelationfunktionA(C, a, c)
        print(A)
        #sinusrelationA skal finde vinkel A
        print("3. vinkel=")
        B=vinkelsumfunktionB(A, C)
        print(B)
        print("3. side =")
        b=sinusrelationfuktionb(B, c, C)
        print(b)
        break

    elif "2" in valg:
        a=float(input("værdi af første side"))
        b=float(input("anden side"))
        c=float(input("sidste side"))
        print("1. vinkel = ")
        C=cosinusrelationfunktionC(a, b, c)
        print(C)
        #cosinusrelation funktion finder vinkel C
        print ("2. vinkel =")
        A=sinusrelationfunktionA(C, a, c)
        print(A)
        print("3. vinkel = ")
        B=vinkelsumfunktionB(A, C)
        print(B)
        break


    elif "3" in valg:
        c=int(input("værdi af den 1. sidelængde"))
        C=int(input("værdi af modstånde vinkel"))
        B=int(input("værdi af anden vinkel"))
        print("sidste vinkel = vinkelsumsfunktionA")
        print("modstånde side til anden vinkel = sinusrelationfunktionb")
        print (" sidste side = sinusrelationfunktiona")
        #check om alle værdier er positive hvis ikke print fejl og start forfra.
        break

    elif "4" in valg:
        a=int(input("værdi for sidelængde"))
        B=int(input("værdi for første vinkel"))
        C=int(input ("værdi for anden vinkel"))
        print("sidste vinkel = vinkelsumfunktionA")
        print("modstående sidelængde til første vinkel = sinusrelationfunktionb")
        print("modstånde sidelængde til anden vinkel = sinusrelationc")
        break

    elif "5" in valg:
        C=int(input("værdi af vinkel"))
        a=int(input("værdi af første sidelængde"))
        b=int(input("værdi af anden sidelængde"))
        print("værdi af sidste sidelængde = cosrelationfunktionc")
        print("2. vinkel =sinusrelationfunktionB")
        print("3. vinkel = vinkelsumfunktionA")
        break
    else:
        print("ikke gyldigt svar, skriv et tal mellem 1-5")