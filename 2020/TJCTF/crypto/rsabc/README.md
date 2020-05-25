# TJCTF – RSABC

* **Category:** crpyot
* **Points:** 50

## Challenge

> I was just listening to some relaxing ASMR(https://youtu.be/J2g3lvNkAfI) when a notification popped up with this.
>
> ???
>
> Attachments:
> > n=57772961349879658023983283615621490728299498090674385733830087914838280699121
> >
> > e=65537
> >
> > c=36913885366666102438288732953977798352561146298725524881805840497762448828130

## Solution

hmmm I guess its a regular RSA and we don't need any hints because the numbers are small enough to factorize

so I used this handy dandy (website)[https://www.alpertron.com.ar/ECM.HTM] to factorize N : (it took me a couple minutes though)

```
p = 202049603951664548551555274464815496697
q = 285934543893985722871321330457714807993
```

and from there it's easy to decrypt the ciphertext, I used a python (script)[solve.py] to do that

```
tjctf{BOLm1QMWi3c}
```
