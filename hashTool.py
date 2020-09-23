from readhw import readw
from testhashlib import hashtext
print("1 = hash message")
print("2 = unhash message")
choose = int(input("choose 1 or 2 : "))
      
if choose == 1:
    the_wordlist = str(input("the wordlist : "))
    hash_type = str(input("hash type : "))
    RR = readw()
    readall = RR.readwlist(the_wordlist)
    HH = hashtext()
    for i in readall:
        i = i.rstrip("\n")
        print(HH.hashingtext(i,hash_type))
    again = input("do you want to use again (yes \"or\" no) : ")
    while again == "yes":
        print("1 = hash message")
        print("2 = unhash message")
        choose = int(input("choose 1 or 2 : "))
        if choose == 1:
            the_wordlist = str(input("the wordlist : "))
            hash_type = str(input("hash type : "))
            RR = readw()
            readall = RR.readwlist(the_wordlist)
            HH = hashtext()
            for i in readall:
                i = i.rstrip("\n")
                print(HH.hashingtext(i,hash_type))
        elif choose == 2:
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

       
elif choose == 2:
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
    again == input("do you want to use again (yes or no) : ")
    while again == "yes":
        
        print("1 = hash message")
        print("2 = unhash message")
        choose = int(input("choose 1 or 2 : "))
        if choose == 1:
            the_wordlist = str(input("the wordlist : "))
            hash_type = str(input("hash type : "))
            RR = readw()
            readall = RR.readwlist(the_wordlist)
            HH = hashtext()
            for i in readall:
                i = i.rstrip("\n")
                print(HH.hashingtext(i,hash_type))
        elif choose == 2:
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
        
