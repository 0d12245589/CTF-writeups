p = open("out.txt","w+")
for i in range(201):
    if i%2==1:
        continue
    if i == 0:
        f = open('%'+"2f","r")
    else:
        f = open('%'+'2f(%s)'%(str(i)),"r")
    s = f.read()
    s = str(s)
    if i >= 200:
        s = s[4:]
    elif i >= 20:
        s = s[3:]
    else:
        s = s[2:]
    p.write(s)
    f.close()
