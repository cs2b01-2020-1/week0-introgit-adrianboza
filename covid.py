genName = ["AY274119","AY278488.2","MN908947","MN988668","MN988669"]

def virus(genomaName):
  gen = open(genomaName + ".txt","r")
  codigo = gen.read()
  gen.close()
  return codigo

virus = [virus(genName[0]),virus(genName[1]),virus(genName[2]),virus(genName[3]),virus(genName[4])]

def comparar(v1, v2):
  p = 0
  for i in range(min(len(v1),len(v2))):
    if(v1[i]==v2[i]):
      p +=1
  return round(p*100/len(v1),2)

for i in genName:
    print("          ", i, end = "")
print("\n")
for j in range(len(genName)):
    if j == 1:
        print(genName[j], end = " ")
    else:
        print(genName[j], end = "   ")
    for i in range(len(genName)):
        print(round(comparar(virus[j],virus[i]),2),"               ", end = "")
    print("\n")
