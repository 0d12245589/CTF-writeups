import json
import base64
dada = json.load(open('newdada.txt'))

try:
    i = 0
    while 1:
        open('newdada' + str(i) + '.txt','wb').write(base64.b64decode(dada['payload']))
        dada = json.load(open('newdada' + str(i) + '.txt'))
        i+=1
except:
    pass