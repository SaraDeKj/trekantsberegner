crazyliste=[1,2,3,4,5,6,7,8,9,10]
print(len(crazyliste))

crazyliste.append(11)
print(crazyliste)

crazyliste.insert(0,0)
print(crazyliste )

crazyliste.remove(len(crazyliste )-1)
print(crazyliste )

if 11 in crazyliste:
    print("11 er i liste")
else:
    print("11 er ikke i liste")

crazyliste.sort(reverse=True)
print(crazyliste )

crazyliste.sort()
print(crazyliste )

crazyliste= [x**2 for x in crazyliste]
print(crazyliste)

#Funktion der giver sum af alle elemnter i listen
def summning(liste):
    sum=0
    for element in liste:
        sum += element
        x= element
    return sum

res=summning(crazyliste )
print("summen af listen =",res)