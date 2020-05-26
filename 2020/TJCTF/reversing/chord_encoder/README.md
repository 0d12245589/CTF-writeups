# TJCTF – Chord Encoder

* **Category:** reversing
* **Points:** 40

## Challenge

> I tried creating my own chords, but my encoded sheet music is a little hard to read. Please play me my song!
>
> Attachments :
> > chords
> >
> > encoded sheet music
> >
> > chord_encoder.py

## Solution

we open the chord_encoder.py file :

```python
f = open('song.txt').read()

l = {'1':'A', '2':'B', '3':'C', '4':'D', '5':'E', '6':'F', '7':'G'}
chords = {}
for i in open('chords.txt').readlines():
	c, n = i.strip().split()
	chords[c] = n

s = ''
for i in f:
	c1, c2 = hex(ord(i))[2:]
	if c1 in l:
		c1 = l[c1]
	if c2 in l:
		c2 = l[c2]
	s += chords[c1] + chords[c2]
open('notes.txt', 'w').write(s)
```

we see that its reading the song.txt and hexifying each byte and replacing it with a string from this file :

```
A 0112
B 2110
C 1012
D 020
E 0200
F 1121
G 001
a 0122
b 2100
c 1002
d 010
e 0100
f 1011
g 000
```

so as we can see we can't immediately recover the song because D,E and d,e are very similar

so I used my competitive programming skillz to write a backtrack algorithim to recover the flag : [solve.py](https://github.com/0d12245589/CTF-writeups/raw/master/2020/TJCTF/reversing/chord_encoder/solve.py)

```
flag{zats_wot_1_call_a_meloD}
```
