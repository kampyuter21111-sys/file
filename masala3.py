f = open("soz.txt", "r", encoding="utf-8")
matn = f.read()
f.close()

sozlar = matn.split()
yangi = []
for s in sozlar:
    yangi.append(s[0].upper() + s[1:])

natija = " ".join(yangi)

f = open("natija3.txt", "w", encoding="utf-8")
f.write(natija)
f.close()
print(natija)
