# SyriaCTF – 8 MILES

* **Category:** Malware Reverse Engineering
* **Points:** 50

## Solution

by decompiling the using IDA we see that the binary is checking for an argument using an equation by solving this equation we get a number 8
and then we see that the array is getting shifted by 8
so we just shift it by -8 and get the flag :

```
R3V3R53_Th3_W0rld_N0W
```

solved by b4n4n4s and thecarrot