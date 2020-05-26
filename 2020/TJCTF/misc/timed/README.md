# TJCTF – Timed

* **Category:** misc
* **Points:** 50

## Challenge

> I found this cool program that times how long Python commands take to run! Unfortunately, the owner seems very paranoid, so there's not really much that you can test. The flag is located in the file flag.txt on the server.
>
> Attachments:
> > nc p1.tjctf.org 8005

## Solution

they only gave us a netcat to connect to so lets see what does it actually do ?

![screenshot1](https://github.com/0d12245589/CTF-writeups/raw/master/2020/TJCTF/misc/timed/images/screenshot1.png)

it seems it runs python commands and returns their runtime, maybe we can use it to pop a shell lets try :

![screenshot2](https://github.com/0d12245589/CTF-writeups/raw/master/2020/TJCTF/misc/timed/images/screenshot2.png)

WTH ? no hacking ! ok fine lets see what does this filter do, lets try opening the flag.txt file and read it :

![screenshot2](https://github.com/0d12245589/CTF-writeups/raw/master/2020/TJCTF/misc/timed/images/screenshot3.png)

hmmm, what ?? they filtered the brackets : `()`, but not the read command XD, lets use that to our advantage

I was inspired by the title of the challenge and thought of a timing attack, so we can run a big for loop if a certain condition is True

![screenshot2](https://github.com/0d12245589/CTF-writeups/raw/master/2020/TJCTF/misc/timed/images/screenshot4.png)

see the timings are different so we can do something like this :

![screenshot2](https://github.com/0d12245589/CTF-writeups/raw/master/2020/TJCTF/misc/timed/images/screenshot5.png)

thats how we gonna extract the flag by trying every character for each position I wrote this [script](https://github.com/0d12245589/CTF-writeups/raw/master/2020/TJCTF/misc/timed/solve.py) to do exactly that

```
tjctf{iTs_T1m3_f0r_a_flaggg}
```
