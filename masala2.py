f = open("matn.txt", "r", encoding="utf-8")
matn = f.read()
f.close()

soz = input("So'z kiriting: ")

if matn.lower().find(soz.lower()) != -1:
    print("Siz kiritgan so'z faylda bor.")
else:
    print("Siz kiritgan so'z faylda yo'q.")