
f = open("sonlar.txt", "r")
matn = f.read()
f.close()

sonlar = matn.split()
yigindi = 0
for s in sonlar:
    yigindi = yigindi + int(s)

ortacha = yigindi / len(sonlar)
print(round(ortacha))
