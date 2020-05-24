f = open('notes.txt').read()

l = {'A':'1', 'B':'2', 'C':'3', 'D':'4', 'E':'5', 'F':'6', 'G':'7'}
chords = {}
for i in open('chords.txt').readlines():
    c, n = i.strip().split()
    if c in l: c = l[c]
    chords[n] = c

ss = ""
res = []

def BT(i):
    global ss,res
    if i == len(f):
        res.append(ss)
        return
    elif i > len(f):
        return

    # trying to take 3 chars
    if f[i:i+3] in chords:
        ss += chords[f[i:i+3]]
        BT(i+3)
        ss = ss[:-1]

    # trying to take 4 chars
    if f[i:i+4] in chords:
        ss += chords[f[i:i+4]]
        BT(i+4)
        ss = ss[:-1]

BT(0)
res = res[0]
print(bytes.fromhex(res).decode('utf-8'))

