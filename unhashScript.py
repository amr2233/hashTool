from readhw import readw
from testhashlib import hashtext
the_hash = str(input("the hash : "))
the_wordlist = str(input("the wordlist : "))
hash_type = str(input("hash type : "))
RR = readw()
readall = RR.readwlist(the_wordlist)
HH = hashtext()

for i in readall:
    i = i.rstrip("\n")
hashText = HH.hashingtext(i,hash_type)

if the_hash == hashText:
    print("{0}::{1}".format(the_hash,i))
else:
    print("not found")


