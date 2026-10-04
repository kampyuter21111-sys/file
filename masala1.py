
f = open("ascii.txt", "r")
matn = f.read()
f.close()

raqamlar = matn.split()
gap = ""
for r in raqamlar:
    gap = gap + chr(int(r))

f = open("natija1.txt", "w")
f.write(gap)
f.close()
print(gap)

