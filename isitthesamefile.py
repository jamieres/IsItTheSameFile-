
#!/usr/bin/env python
# -*- coding: utf-8 -*-

__description__ = "Is it the same file?"
__contact__ = "jamieres-[at]-gmail-[dot]-com"

import os,sys,stat,hashlib,time,colorama
from stat import * 
from colorama import Fore, Style, init
init() 

if len(sys.argv) != 3:
    print("You must compare two files for know if are the same. Please choose another file to compare with the one you have already chosen.")
    exit(0)

fname  = sys.argv[1]
fnameb = sys.argv[2]
st = os.stat(sys.argv[1])
stb = os.stat(sys.argv[2])
md5 = hashlib.md5(open(fname, "rb").read()).hexdigest() 
sha1 = hashlib.sha1(open(fname, "rb").read()).hexdigest() 
sha256 = hashlib.sha256(open(fname, "rb").read()).hexdigest()
md5b = hashlib.md5(open(fnameb, "rb").read()).hexdigest() 
sha1b = hashlib.sha1(open(fname, "rb").read()).hexdigest() 
sha256b = hashlib.sha256(open(fnameb, "rb").read()).hexdigest()

print Fore.CYAN + "\n IS IT THE SAME FILE?:"
if md5 == md5b: 
    print Fore.GREEN + "  * File one and file two ARE the same."
    print Fore.GREEN + "  * Note, in following information, that file one & file two HAVE same values."

else:
    print Fore.GREEN + "  * File one and file two ARE NOT the same."
    print Fore.GREEN + "  * Note, in following information, that file one & file two HAVE NOT same values."

print Fore.CYAN + "\n FILE ONE INFORMATION:"
fdata = {"fname": fname}
md5 = hashlib.md5(open(fname, "rb").read()).hexdigest() 
sha1 = hashlib.sha1(open(fname, "rb").read()).hexdigest() 
print Fore.WHITE + "  Filename:... %(fname)s" % fdata
print Fore.WHITE + "  Filesize:...", st[ST_SIZE]
print Fore.WHITE + "  MD5:........ %s" % md5
print Fore.WHITE + "  SHA1:....... %s" % sha1
print Fore.WHITE + "  SHA256:..... %s" % sha256

print Fore.CYAN + "\n FILE TWO INFORMATION:"
fdatab = {"fname": fnameb}
md5b = hashlib.md5(open(fnameb, "rb").read()).hexdigest() 
sha1b = hashlib.sha1(open(fnameb, "rb").read()).hexdigest() 
print Fore.WHITE + "  Filename:... %(fname)s" % fdatab
print Fore.WHITE + "  Filesize:...", stb[ST_SIZE]
print Fore.WHITE + "  MD5:........ %s" % md5b
print Fore.WHITE + "  SHA1:....... %s" % sha1b
print Fore.WHITE + "  SHA256:..... %s\n" % sha256b

print Fore.CYAN + " FOR OBTAIN MORE SPECIFIC INFORMATION ABOUT THERE FILES, YOU CAN USE MZ-Data-Extract: https://github.com/jamieres/mz-data-extract"
print Fore.CYAN + " Write me: " + Fore.GREEN + " jamieres-[at]-gmail-[dot]-com"
print Fore.CYAN + " Follow me: " + Fore.GREEN + "@jorgemieres"

