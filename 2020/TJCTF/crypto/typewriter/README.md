# TJCTF – Typewriter

* **Category:** crypto
* **Points:** 30

## Challenge

> Oh no! I thought I typed down the correct flag for this problem on my typewriter, but it came out all jumbled on the paper. Someone must have switched the inner hammers around! According to the paper, the flag is `zpezy{fg_dgkt_atn_pqdl}`.
>
> hint : 
> > a becomes q, b becomes w, c becomes e, f becomes y, j becomes p, t becomes z, and z becomes m. Do you see the pattern?


## Solution

As we can see from the description its a substituion cipher

by looking at the hint we see that the key is `qwertyuiopasdfghjklzxcvbnm`

and thats how we recover the flag :

```
tjctf{no_more_key_jams}
```
