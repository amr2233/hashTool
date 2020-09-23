from readhw import readw
from testhashlib import hashtext
the_wordlist = str(input("the wordlist : "))
hash_type = str(input("hash type : "))
RR = readw()
readall = RR.readwlist(the_wordlist)
HH = hashtext()

for i in readall:
    i = i.rstrip("\n")
    print(HH.hashingtext(i,hash_type))

