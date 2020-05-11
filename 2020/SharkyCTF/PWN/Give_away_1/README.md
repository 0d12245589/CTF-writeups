# SharkyCTF – Give Away 1

* **Category:** PWN
* **Points:** 275

## Challenge

> Make good use of this gracious give away.
> 
> nc sharkyctf.xyz 20334
> 
> Attachments :
> > binary : give_away_1
> >
> > shared library : libc-2.27.so
> 
> Creator: Hackhim
## Solution

Well first of all we mark the binary as executable with 'chmod +x give_away_1'

then we run the binary and it gives us a cool give away (not yet ^_^)
and receives som input after it :

![screenshot1](https://github.com/0d12245589/CTF-writeups/raw/master/2020/SharkyCTF/PWN/Give_away_1/images/screenshot1.png)

so what can we do with this giveaway ?

lets first find out what is it by dissassembling the binary using binary ninja :

![screenshot2](https://github.com/0d12245589/CTF-writeups/raw/master/2020/SharkyCTF/PWN/Give_away_1/images/screenshot2.png)

We see that the `system@GOT` address is leaked to us so we can easily determine the libc base address and initiate a ret2libc attack

I used pwntools to do this using python : [solve.py](https://github.com/0d12245589/CTF-writeups/raw/master/2020/SharkyCTF/PWN/Give_away_1/solve.py)

we run it and get the flag:

![screenshot2](https://github.com/0d12245589/CTF-writeups/raw/master/2020/SharkyCTF/PWN/Give_away_1/images/screenshot3.png)

```
shkCTF{I_h0PE_U_Fl4g3d_tHat_1n_L3ss_Th4n_4_m1nuT3s}
```

Yeah I hope you did :)
